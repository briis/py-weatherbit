"""Helper Class for Weatherflow Rest module."""
from __future__ import annotations

import datetime as dt
import logging

from weatherbitpypi.const import UNIT_TYPE_METRIC
from weatherbitpypi.data import BeaufortDescription

UTC = dt.timezone.utc

_LOGGER = logging.getLogger(__name__)

class Conversions:
    """Conversion functions."""

    def __init__(self, units: str, homeassistant: bool) -> None:
        """Initialize class."""
        self.units = units
        self.homeassistant = homeassistant

    def temperature(self, value) -> float:
        """Return celcius to Fahrenheit."""
        if value is None or self.units == UNIT_TYPE_METRIC or self.homeassistant:
            return value
        return round(value * 1.8 + 32, 1)

    def pressure(self, value) -> float:
        """Return inHg from mb/hPa."""
        if value is None or self.units == UNIT_TYPE_METRIC:
            return value
        return round(value * 0.029530, 1)

    def rain(self, value) -> float:
        """Convert rain units."""
        if value is None:
            return None

        if self.units == UNIT_TYPE_METRIC:
            return round(value, 2)
        return round(value * 0.03937007874, 2)

    def density(self, value) -> float:
        """Convert air density."""
        if value is None:
            return None

        if self.units == UNIT_TYPE_METRIC:
            return round(value, 1)

        return round(value * 0.06243, 1)

    def distance(self, value) -> float:
        """Convert km to mi."""
        if value is None:
            return None

        if self.units == UNIT_TYPE_METRIC:
            return round(value, 1)

        return round(value * 0.6213688756, 1)

    def windspeed(self, value, wind_unit_kmh: bool = False) -> float:
        """Return miles per hour from m/s."""
        if value is None:
            return value

        if self.units == UNIT_TYPE_METRIC:
            if wind_unit_kmh:
                return round(value * 3.6, 1)
            return round(value, 1)

        return round(value * 2.236936292, 1)

    def utc_from_timestamp(self, timestamp: int) -> dt.datetime:
        """Return a UTC time from a timestamp."""
        return dt.datetime.utcfromtimestamp(timestamp).replace(tzinfo=UTC)


class Calculations:
    """Calculate entity values."""

    def is_raining(self, rain):
        """Return true if it is raining."""
        if rain is None:
            return None

        rain_rate = rain * 60
        return rain_rate > 0

    def is_freezing(self, temperature):
        """Return true if temperature below 0."""
        if temperature is None:
            return None

        return temperature < 0

    def uv_description(self, uv: float) -> str:
        """Return a Description based on uv value."""
        if uv is None:
            return None

        if uv >= 10.5:
            return "extreme"
        if uv >= 7.5:
            return "very-high"
        if uv >= 5.5:
            return "high"
        if uv >= 2.5:
            return "moderate"
        if uv > 0:
            return "low"

        return "none"

    def wind_direction(self, wind_bearing: int) -> str:
        """Return Wind Directions String from Wind Bearing."""
        if wind_bearing is None:
            return None

        direction_array = [
            "n",
            "nne",
            "ne",
            "ene",
            "e",
            "ese",
            "se",
            "sse",
            "s",
            "ssw",
            "sw",
            "wsw",
            "w",
            "wnw",
            "nw",
            "nnw",
            "n",
        ]
        return direction_array[int((wind_bearing + 11.25) / 22.5)]

    def beaufort(self, wind_speed: float) -> BeaufortDescription:
        """Return data structure with Beaufort values."""
        if wind_speed is None:
            return None

        if wind_speed > 32.7:
            bft = BeaufortDescription(
                value=12,
                description="hurricane"
            )
        elif wind_speed >= 28.5:
            bft = BeaufortDescription(
                value=11,
                description="violent_storm"
            )
        elif wind_speed >= 24.5:
            bft = BeaufortDescription(
                value=10,
                description="storm"
            )
        elif wind_speed >= 20.8:
            bft = BeaufortDescription(
                value=9,
                description="strong_gale"
            )
        elif wind_speed >= 17.2:
            bft = BeaufortDescription(
                value=8,
                description="fresh_gale"
            )
        elif wind_speed >= 13.9:
            bft = BeaufortDescription(
                value=7,
                description="moderate_gale"
            )
        elif wind_speed >= 10.8:
            bft = BeaufortDescription(
                value=6,
                description="strong_breeze"
            )
        elif wind_speed >= 8.0:
            bft = BeaufortDescription(
                value=5,
                description="fresh_breeze"
            )
        elif wind_speed >= 5.5:
            bft = BeaufortDescription(
                value=4,
                description="moderate_breeze"
            )
        elif wind_speed >= 3.4:
            bft = BeaufortDescription(
                value=3,
                description="gentle_breeze"
            )
        elif wind_speed >= 1.6:
            bft = BeaufortDescription(
                value=2,
                description="light_breeze"
            )
        elif wind_speed >= 0.3:
            bft = BeaufortDescription(
                value=1,
                description="light_air"
            )
        else:
            bft = BeaufortDescription(
                value=0,
                description="calm"
            )

        return bft