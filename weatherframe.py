import tkinter as tk
import requests
import json


class WeatherFrame(tk.Frame):
    def __init__(self, master=None):
        # Set up the frame
        tk.Frame.__init__(self, master, height=256, width=320,
                          highlightbackground="black", highlightthickness=1)
        self.pack(fill="both", expand=1)
        self.pack_propagate(0)

        # Set up the AccuWeather API
        self.high_temperature = "N/A"
        self.low_temperature = "N/A"
        self.day_weather = "N/A"
        self.night_weather = "N/A"
        self.day_rain = "N/A"
        self.night_rain = "N/A"

        # Show the text
        self.displayElements()
        self.updateWeatherInfo()

    def displayElements(self):
        """ Displays the message within the frame """

        # Set up the label itself
        self.message = tk.StringVar()
        self.message_label = tk.Label(self, font=('Helvetica', 16), wraplength=318)
        self.message_label.pack(fill="both", expand=1)
        self.message_label["textvariable"] = self.message

        # Set the message to be displayed

    def updateWeatherInfo(self):
        """ Gets information from the AccuWeather API """
        # Fetch the JSON data
        response = requests.get(url="http://dataservice.accuweather.com/forecasts/v1/daily/1day/346069?apikey=APIKEY")
        response_json = json.loads(response.content)

        # Extract the daily low temperature
        low_temp_info = response_json["DailyForecasts"][0]["Temperature"]["Minimum"]
        self.low_temperature = f"Low: {low_temp_info['Value']}\u00B0 {low_temp_info['Unit']}"

        # Extract the daily high temperature
        high_temp_info = response_json["DailyForecasts"][0]["Temperature"]["Maximum"]
        self.high_temperature = f"High: {high_temp_info['Value']}\u00B0 {high_temp_info['Unit']}"

        # Extract the daytime weather
        daytime_info = response_json["DailyForecasts"][0]["Day"]
        self.day_weather = f"Daytime: {daytime_info['IconPhrase']}"
        could_rain_response = "Yes" if daytime_info["HasPrecipitation"] else "No"
        self.day_rain = f"Could it rain? {could_rain_response}!"

        # Extract the nighttime weather
        nighttime_info = response_json["DailyForecasts"][0]["Night"]
        self.night_weather = f"Nighttime: {nighttime_info['IconPhrase']}"
        could_rain_response = "Yes" if nighttime_info["HasPrecipitation"] else "No"
        self.night_rain = f"Could it rain? {could_rain_response}!"

        # Set the weather widget text
        weather_text = "Weather at College Station\n" + \
                       self.low_temperature + " | " + self.high_temperature + "\n\n" + \
                       self.day_weather + "\n" + self.day_rain + "\n\n" + \
                       self.night_weather + "\n" + self.night_rain
        self.message.set(weather_text)