"""WeatherBit Data Wrapper."""
from __future__ import annotations

import logging
from typing import List, Optional

from aiohttp import ClientSession, ClientTimeout, client_exceptions

from weatherbitpypi.const import (
    BASE_URL,
    DEFAULT_TIMEOUT,
    LANGUAGE_EN,
    UNIT_TYPE_METRIC,
    VALID_LANGUAGES,
    VALID_UNIT_TYPES
)
from weatherbitpypi.data import (
    BaseDataDescription,
    BeaufortDescription,
    ForecastDescription,
    ObservationDescription,
)
from weatherbitpypi.exceptions import ResultError

_LOGGER = logging.getLogger(__name__)


class WeatherBitApiClient:
    """Base class for WeatherBit Api."""

    req: ClientSession

    def __init__(
        self,
        api_key: str,
        latitude: float,
        longitude: float,
        units: Optional[str] = UNIT_TYPE_METRIC,
        language: Optional[str] = LANGUAGE_EN,
        homeassistant: Optional(bool) = True,
        session: Optional[ClientSession] = None,
    ) -> None:
        """Initialize Api Class."""
        self.api_key = api_key
        self.latitude = latitude
        self.longitude = longitude
        self.units = units
        self.language = language
        self.homeassistant = homeassistant

        if self.units not in VALID_UNIT_TYPES:
            self.units = UNIT_TYPE_METRIC

        if self.language not in VALID_LANGUAGES:
            self.language = LANGUAGE_EN

        if session is None:
            session = ClientSession()
        self.req = session

        self._station_data: BaseDataDescription = None

    @property
    def station_data(self) -> BaseDataDescription:
        """Return Station Data."""
        return self._station_data

    async def initialize(self) -> None:
        """Initialize data tables."""
        endpoint = f"{BASE_URL}/current?lat={self.latitude}&lon={self.longitude}&key={self.api_key}"
        endpoint += f"&lang={self.language}&units={self.units}&include=alerts"
        data = await self._async_request("get", endpoint)

        base_data = data["data"][0]
        entity_data = BaseDataDescription(
            key=base_data["station"],
            country_code=base_data["country_code"],
            city_name=base_data["city_name"],
            latitude=base_data["lat"],
            longitude=base_data["lon"],
            timezone=base_data["timezone"],
        )
        self._station_data = entity_data

    async def _async_request(
        self,
        method: str,
        endpoint: str,
    ) -> dict:
        """Make a request against the SmartWeather API."""
        use_running_session = self.req and not self.req.closed

        if use_running_session:
            session = self.req
        else:
            session = ClientSession(timeout=ClientTimeout(total=DEFAULT_TIMEOUT))

        try:
            async with session.request(method, endpoint) as resp:
                resp.raise_for_status()
                data = await resp.json()
                return data

        except client_exceptions.ClientError as err:
            raise ResultError(f"Error requesting data from Meteobridge: {err}") from None

        finally:
            if not use_running_session:
                await session.close()
