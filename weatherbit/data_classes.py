"""Defines the Data Classes used."""

class CurrentData:
    """A representation of Current Weather Data."""

    def __init__(self, data):
        self._station = data["station"]
        self._city_name = data["city_name"]
        self._ob_time = data["ob_time"]
        self._temp = data["temp"]
        self._app_temp = data["app_temp"]
        self._humidity = data["rh"]
        self._pres = data["pres"]
        self._clouds = data["clouds"]
        self._solar_rad = data["solar_rad"]
        self._wind_spd = data["wind_spd"]
        self._wind_cdir = data["wind_cdir"]
        self._wind_dir = data["wind_dir"]
        self._dewpt = data["dewpt"]
        self._pod = data["pod"]
        self._weather_icon = data["weather_icon"]
        self._weather_code = data["weather_code"]
        self._weather_text = data["weather_text"]
        self._vis = data["vis"]
        self._precip = data["precip"]
        self._snow = data["snow"]
        self._uv = data["uv"]
        self._aqi = data["aqi"]
        self._timezone = data["timezone"]

    @property
    def station(self):
        """Source station ID."""
        return self._station

    @property
    def city_name(self):
        """City Name."""
        return self._city_name

    @property
    def ob_time(self):
        """Last observation time (YYYY-MM-DD HH:MM)."""
        return self._ob_time

    @property
    def temp(self):
        """Temperature."""
        return self._temp

    @property
    def app_temp(self):
        """Apparent/"Feels Like" temperature."""
        return self._app_temp

    @property
    def humidity(self):
        """Relative humidity (%)."""
        return self._humidity

    @property
    def pres(self):
        """Pressure."""
        return self._pres

    @property
    def clouds(self):
        """Cloud coverage (%)."""
        return self._clouds

    @property
    def solar_rad(self):
        """Estimated Solar Radiation (W/m^2)."""
        return self._solar_rad

    @property
    def wind_spd(self):
        """Wind speed."""
        return self._wind_spd

    @property
    def wind_cdir(self):
        """Abbreviated wind direction.."""
        return self._wind_cdir

    @property
    def wind_dir(self):
        """Wind direction (degrees)."""
        return self._wind_dir

    @property
    def dewpt(self):
        """Dew point."""
        return self._dewpt

    @property
    def pod(self):
        """Part of the day (d = day / n = night)."""
        return self._pod

    @property
    def weather_icon(self):
        """Weather icon code."""
        return self._weather_icon

    @property
    def weather_code(self):
        """Weather code."""
        return self._weather_code

    @property
    def weather_text(self):
        """Weather Description."""
        return self._weather_text

    @property
    def vis(self):
        """Visibility (default KM)."""
        return self._vis

    @property
    def precip(self):
        """Liquid equivalent precipitation rate."""
        return self._precip

    @property
    def snow(self):
        """Snowfall."""
        return self._snow

    @property
    def uv(self):
        """UV Index."""
        return self._uv

    @property
    def aqi(self):
        """Air Quality Index [US - EPA standard 0 - +500]."""
        return self._aqi

    @property
    def timezone(self):
        """Local IANA Timezone."""
        return self._timezone
