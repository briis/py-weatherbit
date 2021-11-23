"""System Wide Constants for pymeteobridgedata."""
from __future__ import annotations

BASE_URL = "https://api.weatherbit.io/v2.0"

ALERT_ADVISORY = "Advisory"
ALERT_WATCH = "Watch"
ALERT_WARNING = "Warning"

DATA_TYPES = [
    "current",
    "forecast",
    "alert",
]

LANGUAGE_EN = "en"
VALID_LANGUAGES = [
    LANGUAGE_EN,
    "ar",
    "az",
    "be",
    "bg",
    "bs",
    "ca",
    "cz",
    "da",
    "de",
    "fi",
    "fr",
    "el",
    "es",
    "ja",
    "hr",
    "hu",
    "id",
    "it",
    "is",
    "iw",
    "kw",
    "lt",
    "nb",
    "nl",
    "pl",
    "pt",
    "ro",
    "ru",
    "sk",
    "sl",
    "sr",
    "sv",
    "tr",
    "uk",
    "zh",
    "zh-tw",

]

DEFAULT_TIMEOUT = 10

UNIT_TYPE_METRIC = "metric"
UNIT_TYPE_IMPERIAL = "imperial"

VALID_UNIT_TYPES = [
    UNIT_TYPE_IMPERIAL,
    UNIT_TYPE_METRIC,
]

WEATHER_ALERTS = [
    ALERT_ADVISORY,
    ALERT_WATCH,
    ALERT_WARNING
]
