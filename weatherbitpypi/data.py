"""Dataclasses for weatherbit."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class BaseDataDescription:
    """A class describing base data for the Weather location."""

    key: str

    city_name: str
    latitude: float
    longitude: float
    country_code: str
    timezone: str


@dataclass
class ObservationDescription:
    """A class describing current weather data."""

    key: str

    utc_time: str | None = None
    station: str | None = None
    city_name: str | None = None
    temp: float | None = None
    app_temp: float | None = None
    pres: float | None = None
    slp: float | None = None
    clouds: int | None = None
    solar_rad: float | None = None
    wind_spd: float | None = None
    wind_cdir: str | None = None
    wind_dir: int | None = None
    dewpt: float | None = None
    pod: str | None = None
    weather_icon: str | None = None
    weather_code: int | None = None
    weather_text: str | None = None
    vis: float | None = None
    precip: float | None = None
    snow: float | None = None
    uv: float | None = None
    aqi: float | None = None
    dhi: float | None = None
    dni: float | None = None
    ghi: float | None = None
    elev_angle: int | None = None
    h_angle: int | None = None
    timezone: str | None = None
    sunrise: str | None = None
    sunset: str | None = None
    is_night: bool | None = None
    beaufort_value: int | None = None
    beaufort_text: str | None = None


@dataclass
class ForecastDescription:
    """A class describing forecast weather data."""

    key: str

    utc_time: str | None = None
    city_name: str | None = None
    temp: float | None = None
    max_temp: float | None = None
    min_temp: float | None = None
    app_max_temp: float | None = None
    app_min_temp: float | None = None
    humidity: int | None = None
    pres: float | None = None
    slp: float | None = None
    clouds: int | None = None
    wind_spd: float | None = None
    wind_gust_spd: float | None = None
    wind_cdir: str | None = None
    wind_dir: int | None = None
    dewpt: float | None = None
    pop: int | None = None
    weather_icon: str | None = None
    weather_code: int | None = None
    weather_text: str | None = None
    vis: float | None = None
    precip: float | None = None
    snow: float | None = None
    ozone: float | None = None


@dataclass
class BeaufortDescription:
    """A class that describes beaufort values."""

    value: int
    description: str