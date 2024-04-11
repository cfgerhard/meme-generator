import requests

class WeatherService:
    base_url = 'https://api.openweathermap.org/data/2.5/'
    app_id = 'c1233a153af1248f54bb09bcc2701a71'

    @classmethod
    def getForecast(cls, city='new york', country='us'):
        url = f'{cls.base_url}forecast'

        params = {
            'q': f'{city},{country}',
            'appid': cls.app_id,
            'mode': 'json'}
        response = requests.get(url, params=params)
        data = response.json()
        return data['list']

if __name__ == "__main__":
    print(WeatherService.get_weather())