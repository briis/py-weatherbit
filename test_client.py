""" The test for the API """
"""Run an example script to quickly test."""
import asyncio
import logging
import time
import json

from weatherbitpypi.client import Weatherbit
from weatherbitpypi.errors import WeatherbitError

_LOGGER = logging.getLogger(__name__)

LATITUDE = 55.625053
LONGITUDE = 12.136619
LANGUAGE = "da"
UNITS = "M" # M = Metric (Default), I = Imperial, S = Scientific

async def main() -> None:
    """Create the aiohttp session and run the example."""

    # Get the API Key from secrets.json
    path_index = __file__.rfind("/")
    top_path = __file__[0:path_index]
    filepath = f"{top_path}/secrets.json"
    with open(filepath) as json_file:
        data = json.load(json_file)
        api_key = data["connection"]["api_key"]

    logging.basicConfig(level=logging.DEBUG)

    wbit = Weatherbit(api_key,LATITUDE,LONGITUDE,LANGUAGE, UNITS)

    start = time.time()

    try:
        # _LOGGER.info("GETTING CITY NAME:")
        # city_name = await wbit.async_get_city_name()
        # _LOGGER.info(f"CITY: {city_name}")

        _LOGGER.info("GETTING CURRENT DATA:")
        data = await wbit.async_get_current_data()
        for row in data:
            _LOGGER.info(f"{row.beaufort_value} - {row.beaufort_text} - {row.weather_text} - {row.wind_cdir} - {row.wind_dir} - {row.is_night} - {row.timezone} - {row.pod}")

        # _LOGGER.info("GETTING DAILY FORECAST DATA:")
        # data = await wbit.async_get_forecast_daily()
        # for row in data:
        #     _LOGGER.info(f"{row.city_name} - {row.timestamp} - {row.timezone} - {row.local_time} - {row.weather_text} - {row.max_temp}")

        # NOTE: Unmark if you have a paid API Key
        # _LOGGER.info("GETTING HOURLY FORECAST DATA:")
        # data = await wbit.async_get_forecast_hourly()
        # for row in data:
        #     _LOGGER.info(f"{row.city_name} - {row.timestamp} - {row.weather_text} - {row.temp}")

        # _LOGGER.info("GETTING WEATHER ALERTS:")
        # data = await wbit.async_get_weather_alerts()
        # for row in data:
        #     _LOGGER.info("\n" +
        #         f"ALERT COUNT: {row.alert_count}" + "\n" +
        #         f"CITY: {row.city_name}" + "\n" +
        #         f"SEVERITY: {row.severity}" + "\n" +
        #         f"TITLE: {row.title}" + "\n" +
        #         f"REGIONS: {row.regions}" + "\n" +
        #         f"DESCRIPTION: {row.description}" + "\n"
        #     )

    except WeatherbitError as err:
        _LOGGER.info(err)

    end = time.time()

    _LOGGER.info("Execution time: %s seconds", end - start)


asyncio.run(main())
