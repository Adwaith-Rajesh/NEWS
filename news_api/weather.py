try:
    from api_key import Keys

except ImportError:
    from .api_key import Keys

finally:
    import geocoder
    import requests


class Weather(Keys):

    def __init__(self):

        cord = geocoder.ip('me')
        cord = cord.latlng

        appid = self.weather_api_key

        url = f'https://api.openweathermap.org/data/2.5/weather?lat={cord[0]}&lon={cord[1]}&appid={appid}'
        self.json_file = requests.get(url).json()

    def get_info(self):
        clouds = self.json_file['weather'][0]['description']
        f_temp = self.json_file['main']['feels_like']

        c_temp = str(f_temp - 273.15)[0: 5]

        return [clouds, c_temp]

