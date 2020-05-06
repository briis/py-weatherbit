"""Define a client to interact with Weatherbit."""
import asyncio
import logging
from typing import Optional

from aiohttp import ClientSession, ClientTimeout
from aiohttp.client_exceptions import ClientError

from weatherbit.errors import InvalidApiKey, RequestError, ResultError, WeatherbitError


_LOGGER = logging.getLogger(__name__)

class Client:
    """A Weatherbit Client."""

    
