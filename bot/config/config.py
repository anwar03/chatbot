import configparser


class Config:
    def __init__(self):
        self.filename = "config.ini"
        self.config = configparser.ConfigParser()
        self.config.read(self.filename)
        self._config_data = self.config["DEFAULT"]

    @property
    def luis_app_id(self):
        return self._config_data["LUIS_APP_ID"]

    @property
    def luis_endpoint_key(self):
        return self._config_data["LUIS_ENDPOINT_KEY"]

    @property
    def luis_endpoint(self):
        return self._config_data["LUIS_ENDPOINT"]

    @property
    def weather_api_key(self):
        return self._config_data["WEATHER_API_KEY"]
