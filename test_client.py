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
LATITUDE = 47.608013
LONGITUDE = -122.335167
LANGUAGE = "en"
UNITS = "I" # M = Metric (Default), I = Imperial, S = Scientific

async def main() -> None:
    """Create the aiohttp session and run the example."""
    logging.basicConfig(level=logging.DEBUG)

    wbit = Weatherbit(API_KEY,LATITUDE,LONGITUDE,LANGUAGE, UNITS)

    start = time.time()

    try:
        # _LOGGER.info("GETTING CITY NAME:")
        # city_name = await wbit.async_get_city_name()
        # _LOGGER.info(f"CITY: {city_name}")

        _LOGGER.info("GETTING CURRENT DATA:")
        data = await wbit.async_get_current_data()
        for row in data:
            _LOGGER.info(f"{row.obs_time_local} - {row.datetime} - {row.timestamp} - {row.sunrise} - {row.sunset} - {row.is_night} - {row.timezone} - {row.pod}")

        _LOGGER.info("GETTING DAILY FORECAST DATA:")
        data = await wbit.async_get_forecast_daily()
        for row in data:
            _LOGGER.info(f"{row.city_name} - {row.timestamp} - {row.valid_date} - {row.ts_utc} - {row.weather_text} - {row.max_temp}")

        # NOTE: Unmark if you have a paid API Key
        # _LOGGER.info("GETTING HOURLY FORECAST DATA:")
        # data = await wbit.async_get_forecast_hourly()
        # for row in data:
        #     _LOGGER.info(f"{row.city_name} - {row.timestamp} - {row.weather_text} - {row.temp}")

        # _LOGGER.info("GETTING WEATHER ALERTS:")
        # data = await wbit.async_get_weather_alerts()
        # for row in data:
        #     _LOGGER.info(f"{row.city_name} - {row.title}")

    except WeatherbitError as err:
        _LOGGER.info(err)

    end = time.time()

    _LOGGER.info("Execution time: %s seconds", end - start)


asyncio.run(main())
