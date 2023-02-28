import python_weather
import asyncio
import os
import geocoder
import openpyxl

g = geocoder.ip('me')
city = g.city
print(city)
import requests, json

# Enter your API key here
api_key = "536cfb7b8639cae2fbb201110ca7b7e8"

# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Give city name
city_name = city

# complete_url variable to store
# complete url address
complete_url = base_url + "appid=" + api_key + "&q=" + city_name + "&lang=pt_br"

# get method of requests module
# return response object
response = requests.get(complete_url)

# json method of response object
# convert json format data into
# python format data
x = response.json()

# Now x contains list of nested dictionaries
# Check the value of "cod" key is equal to
# "404", means city is found otherwise,
# city is not found
if x["cod"] != "404":

    # store the value of "main"
    # key in variable y
    y = x["main"]

    # store the value corresponding
    # to the "temp" key of y
    current_temperature = y["temp"] - 273.15 # convert to Celsius

    # store the value corresponding
    # to the "pressure" key of y
    current_pressure = y["pressure"]

    # store the value corresponding
    # to the "humidity" key of y
    current_humidity = y["humidity"]

    # store the value of "weather"
    # key in variable z
    z = x["weather"]

    # store the value corresponding
    # to the "description" key at
    # the 0th index of z
    weather_description = z[0]["description"]

    # print following values
    print(" temperatura = " +
                    str( '%.2s' %  current_temperature)+ "C°"
          "\n pressão atimosferica = " +
                    str(current_pressure) +
          "\n umidade (in percentage) = " +
                    str(current_humidity) +
          "\n descrição = " +
                    str(weather_description))

else:
    print(" City Not Found ")

