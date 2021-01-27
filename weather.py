import re
import json
import urllib.request as ur


def get_ip():
    """
    Returns: IP Address in 123.456.789.12 format
    """
    text = str(ur.urlopen('http://checkip.dyndns.com/').read())
    pattern = r'(\d+.\d+.\d+.\d+)'
    return re.search(pattern, text).group()


IP = str(get_ip())

# Get Location
response = ur.urlopen(url='http://ipinfo.io/' + IP + '/json')
data = json.load(response)
city = data['city']

# Get Weather
api_key = "GET_YOUR_API_KEY"
response = ur.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&APPID=' + api_key)
data = json.load(response)

print(f"""
City                 - {city}
Weather condition    - {data['weather'][0]['description']}
Temperature          - {round(data['main']['temp']-273, 2)}°C
Minimum temperature  - {data['main']['temp_min']}°C
Maximum temperature  - {data['main']['temp_max']}°C
Atmospheric pressure - {data['main']['pressure']}hPa
Humidity             - {data['main']['humidity']}%
Wind speed           - {data['wind']['speed']}m/s
Wind direction       - {data['wind']['deg']}m/s
Cloudiness           - {data['clouds']['all']}%
""")
