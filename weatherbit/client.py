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
from weatherbit.data_classes import (
    CurrentData,
    ForecastData,
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

    async def async_forecast_data(self) -> None:
        return await self._get_forecast_data()

    async def _get_current_data(self) -> None:
        """Return Current Data for Location."""

        endpoint = f"current?lat={self._latitude}&lon={self._longitude}&lang={self._language}&units={self._units}&key={self._api_key}"
        json_data = await self.async_request("get", endpoint)

        items = []
        for row in json_data["data"]:
            item = {
                "station": row["station"],
                "ob_time": row["ob_time"],
                "temp": row["temp"],
                "city_name": row["city_name"],
                "app_temp": row["app_temp"],
                "rh": row["rh"],
                "pres": row["pres"],
                "clouds": row["clouds"],
                "solar_rad": row["solar_rad"],
                "wind_spd": row["wind_spd"],
                "wind_cdir": row["wind_cdir"],
                "wind_dir": row["wind_dir"],
                "dewpt": row["dewpt"],
                "pod": row["pod"],
                "weather_icon": row["weather"]["icon"],
                "weather_code": row["weather"]["code"],
                "weather_text": row["weather"]["description"],
                "vis": row["vis"],
                "precip": row["precip"],
                "snow": row["snow"],
                "uv": row["uv"],
                "aqi": row["aqi"],
                "timezone": row["timezone"],
            }
            items.append(CurrentData(item))

        return items

    async def _get_forecast_data(self) -> None:
        """Return Forecast Data for Location."""

        endpoint = f"forecast/daily?lat={self._latitude}&lon={self._longitude}&lang={self._language}&units={self._units}&key={self._api_key}"
        json_data = await self.async_request("get", endpoint)

        items = []

        for row in json_data:
            item = {
                "timezone": row["timezone"],
                "city_name": row["city_name"],
                "valid_date": row["data"]["valid_date"],
                "temp": row["data"]["temp"],
                "max_temp": row["data"]["max_temp"],
                "min_temp": row["data"]["min_temp"],
                "app_max_temp": row["data"]["app_max_temp"],
                "app_min_temp": row["data"]["app_min_temp"],
                "rh": row["data"]["rh"],
                "pres": row["data"]["pres"],
                "clouds": row["data"]["clouds"],
                "wind_spd": row["data"]["wind_spd"],
                "wind_gust_spd": row["data"]["wind_gust_spd"],
                "wind_cdir": row["data"]["wind_cdir"],
                "wind_dir": row["data"]["wind_dir"],
                "dewpt": row["data"]["dewpt"],
                "pod": row["data"]["pod"],
                "weather_icon": row["data"]["weather"]["icon"],
                "weather_code": row["data"]["weather"]["code"],
                "weather_text": row["data"]["weather"]["description"],
                "vis": row["data"]["vis"],
                "precip": row["data"]["precip"],
                "snow": row["data"]["snow"],
                "uv": row["data"]["uv"],
                "ozone": row["data"]["ozone"],
            }
            items.append(ForecastData(item))

        return items

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
