import requests

from datetime import datetime

api_key = '2a7df8a01b28c34cf596c27de6279795'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

temp_city = ((api_data['main']['temp']) - 273.15)
presure_city = api_data['main']['pressure']
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

fh = open('TodayWeather.txt', 'w')


fh.write("\n-------------------------------------------------------------")
fh.write("\nWeather Stats for - {}  || {}".format(location.upper(), date_time))
fh.write("\n-------------------------------------------------------------")

fh.write("\n\nCurrent temperature is: {:.2f} deg C".format(temp_city))
fh.write("\nCurrent pressure is   : {:.2f} hPa ".format(presure_city))
fh.write("\nCurrent Humidity      : %d percent" %hmdt)
fh.write("\nCurrent wind speed    : %d kmph" %wind_spd)
fh.write("\nCurrent weather desc  : %s" %weather_desc)


fh.close()
print("")