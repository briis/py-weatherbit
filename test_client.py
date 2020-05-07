""" The test for the API """
"""Run an example script to quickly test."""
import asyncio
import logging
import time
import json

from weatherbitpypi.client import Weatherbit
from weatherbitpypi.errors import WeatherbitError

_LOGGER = logging.getLogger(__name__)


API_KEY = "YOUR-API-KEY"
LATITUDE = 55.625053
LONGITUDE = 12.136619
LANGUAGE = "da"

async def main() -> None:
    """Create the aiohttp session and run the example."""
    logging.basicConfig(level=logging.DEBUG)

    wbit = Weatherbit(API_KEY,LATITUDE,LONGITUDE,LANGUAGE)

    start = time.time()

    try:
        _LOGGER.info("GETTING CURRENT DATA:")
        data = await wbit.async_get_current_data()
        for row in data:
            _LOGGER.info(f"{row.city_name} - {row.ob_time} - {row.weather_text} - {row.timezone}")

        _LOGGER.info("GETTING DAILY FORECAST DATA:")
        data = await wbit.async_get_forecast_daily()
        for row in data:
            _LOGGER.info(f"{row.city_name} - {row.valid_date} - {row.weather_text} - {row.max_temp}")

        # NOTE: Unmark if you have a paid API Key
        # _LOGGER.info("GETTING HOURLY FORECAST DATA:")
        # data = await wbit.async_get_forecast_hourly()
        # for row in data:
        #     _LOGGER.info(f"{row.city_name} - {row.timestamp} - {row.weather_text} - {row.temp}")

        _LOGGER.info("GETTING WEATHER ALERTS:")
        data = await wbit.async_get_weather_alerts()
        for row in data:
            _LOGGER.info(f"{row.city_name} - {row.title}")

    except WeatherbitError as err:
        _LOGGER.info(err)

    end = time.time()

    _LOGGER.info("Execution time: %s seconds", end - start)


asyncio.run(main())
