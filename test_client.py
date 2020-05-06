""" The test for the API """
"""Run an example script to quickly test."""
import asyncio
import logging
import time
import json

from weatherbit.client import Api
from weatherbit.errors import WeatherbitError

_LOGGER = logging.getLogger(__name__)


API_KEY = "2efc1231d69c41099e7f8e8356414d68"
LATITUDE = 55.625053
LONGITUDE = 12.136619
LANGUAGE = "da"

async def main() -> None:
    """Create the aiohttp session and run the example."""
    logging.basicConfig(level=logging.DEBUG)

    wbit = Api(API_KEY,LATITUDE,LONGITUDE,LANGUAGE)

    start = time.time()

    try:
        # Login:
        _LOGGER.info("GETTING CURRENT DATA:")
        _LOGGER.info(await wbit.async_update_current_data())
        
    except WeatherbitError as err:
        _LOGGER.info(err)

    end = time.time()

    _LOGGER.info("Execution time: %s seconds", end - start)


asyncio.run(main())