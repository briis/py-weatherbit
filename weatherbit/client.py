"""Define a client to interact with Weatherbit."""
import asyncio
import logging
from typing import Optional

from aiohttp import ClientSession, ClientTimeout
from aiohttp.client_exceptions import ClientError

from weatherbit.errors import InvalidApiKey, RequestError, ResultError, WeatherbitError
from weatherbit.const import (
    BASE_URL,
    DEFAULT_TIMEOUT,
)

_LOGGER = logging.getLogger(__name__)

class Api:
    """Weatherbit Current Conditions Client."""

    def __init__(
        self,
        api_key: str,
        latitude: float,
        longitude: float,
        language: str="en",
        units: str = "M",
        session: Optional[ClientSession] = None
        ):
        self._api_key = api_key
        self._latitude = latitude
        self._longitude = longitude
        self._language = language
        self._units = units
        self._session: ClientSession = session
        self.req = session

    async def async_update_current_data(self) -> None:
        return await self._get_current_data()

    async def _get_current_data(self) -> None:
        """Return Current Data for Location."""

        endpoint = f"current?lat={self._latitude}&lon={self._longitude}&lang={self._language}&units={self._units}&key={self._api_key}"
        json_data = await self.async_request("get", endpoint)
        return json_data

    async def async_request(self, method: str, endpoint: str) -> dict:
        """Make a request against the Weatherbit API."""

        use_running_session = self._session and not self._session.closed

        if use_running_session:
            session = self._session
        else:
            session = ClientSession(timeout=ClientTimeout(total=DEFAULT_TIMEOUT))

        try:
            async with session.request(
                method, f"{BASE_URL}/{endpoint}"
            ) as resp:
                resp.raise_for_status()
                data = await resp.json()
                return data
        except asyncio.TimeoutError:
            raise RequestError("Request to endpoint timed out: {endpoint}")
        except ClientError as err:
            raise RequestError(
                f"Error requesting data from {endpoint}: {err}"
            ) from None
        finally:
            if not use_running_session:
                await session.close()
