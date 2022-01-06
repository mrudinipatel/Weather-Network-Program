import tkinter as tk
import requests
import time
from dotenv import load_dotenv
import os

load_dotenv() # environment variables from .env

API_KEY = os.getenv("API_KEY") # searches entire computer for path that contains API_KEY

# Function that retrieves JSON data from API
def getWeather(layout):
    city = textfield.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + API_KEY
    json_data = requests.get(api).json()

    if json_data['cod'] == '404': # handles if user enters an invalid city name
        label1.config(text = "")
        label2.config(text = "Uh oh! Sorry, we could not find that city.")
        label3.config(text = "Please try again.")
        label4.config(text = "")

    desc = json_data['weather'][0]['description']
    temp = int(json_data['main']['temp'] - 273.15) # subtracting 273.15 to obtain celcius temp
    
    minTemp = int(json_data['main']['temp_min'] - 273.15)
    maxTemp = int(json_data['main']['temp_max'] - 273.15)
    feelsLike = int(json_data['main']['feels_like'] - 273.15)
    
    humidity = json_data['main']['humidity']
    wind = float("{:.2f}".format(json_data['wind']['speed'] * 3.6)) # multiplying by 3.6 to convert m/s into km/h
    
    sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise'])) # formatting time to hours/minutes/seconds (12-hour clock format)
    sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset'])) # sunrise/sunset are already in EST time zone (so no arithmetic)

    # formatting retrieved information
    mainInfo = desc + "\n" + str(temp) + "°C\n"
    details = "Max: " + str(maxTemp) + "°C\n" + "Min: " + str(minTemp) + "°C\n" + "Feels Like: " + str(feelsLike) + "°C\n"
    atmosphere = "Humidity: " + str(humidity) + "%\n" + "Wind: " + str(wind) + " km/h\n"
    solar = "Sunrise: " + str(sunrise) + " a.m.\n" + "Sunset: " + str(sunset) + " p.m.\n"

    # setting labels
    label1.config(text = mainInfo)
    label2.config(text = details)
    label3.config(text = atmosphere)
    label4.config(text = solar)

# Creating GUI window layout
layout = tk.Tk()
layout.geometry("600x500")
layout.title("Weather Network Program")
layout.config(bg = "#b4cbff")

normal = ("Garamond", 18, "bold")
headings = ("Garamond", 36, "bold")

textfield = tk.Entry(layout, justify='center', font = headings)
textfield.config(bg = "#dac4ff")
textfield.pack(pady = 20)
textfield.focus()
textfield.bind('<Return>', getWeather) # each 'return/enter' hit, calls the function in the textfield

label1 = tk.Label(layout, font = headings)
label1.config(bg = "#b4cbff")
label1.pack()

label2 = tk.Label(layout, font = normal)
label2.config(bg = "#b4cbff")
label2.pack()

label3 = tk.Label(layout, font = normal)
label3.config(bg = "#b4cbff")
label3.pack()

label4 = tk.Label(layout, font = normal)
label4.config(bg = "#b4cbff")
label4.pack()

layout.mainloop()


