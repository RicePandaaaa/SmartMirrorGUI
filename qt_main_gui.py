import sys, time, requests, json
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6 import uic


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("mirror.ui", self)

        # Set up schedule information
        self.classes = {"ESET-349 LEC": {"Room": "THOM-107A", "Time": "8:00am-8:50am",   "Days": "M/W/F"},
                        "ESET-349 LAB": {"Room": "THOM-101A", "Time": "2:00am-4:30pm",   "Days": "M"},
                        "ESET-359 LEC": {"Room": "THOM-107A", "Time": "11:10am-12:25pm", "Days": "T/Th"},
                        "ESET-359 LAB": {"Room": "THOM-204",  "Time": "8:00am-10:30am",  "Days": "Th"},
                        "MXET-300 LEC": {"Room": "ZACH-442",  "Time": "12:45pm-1:35pm",  "Days": "T/Th"},
                        "MXET-300 LAB": {"Room": "FERM-006",  "Time": "2:00pm-4:30pm",   "Days": "W"},
                        "MMET-361 LEC": {"Room": "FRAN-102",  "Time": "12:40pm-1:30pm",  "Days": "M/W"},
                        "MMET-361 LAB": {"Room": "THOM-115B", "Time": "8:00am-9:50pm",   "Days": "T"}}

        # Set the values immediately
        self.updateTime()
        self.updateClasses()
        self.updateWeatherInfo()

        # Timer to update clock every second
        self.clock_timer = QtCore.QTimer(self)
        self.clock_timer.timeout.connect(self.updateTime)
        self.clock_timer.start(1000)

        # Timer to update classes every hour
        # *An one hour error of margin is fine because I don't have class at midnight
        self.class_timer = QtCore.QTimer(self)
        self.class_timer.timeout.connect(self.updateClasses)
        self.class_timer.start(3600 * 1000)

        # Timer to update weather every hour
        # *Weather API grabs data for the whole day so every hour is fine
        # *especially when I am limited to 50 calls per day
        self.weather_timer = QtCore.QTimer(self)
        self.weather_timer.timeout.connect(self.updateWeatherInfo)
        self.weather_timer.start(1800 * 1000)
        
    def updateTime(self):
        """ Update the main time widgets """

        # Fetch the time info
        date = time.strftime("%B %d, %Y", time.localtime())
        current_time = time.strftime("%H:%M:%S", time.localtime())
        weekday = time.strftime("%A", time.localtime())

        # Set the clock label texts
        self.date.setText(date)
        self.time.setText(current_time)
        self.weekday.setText(weekday)

    def updateClasses(self):
        """ Update the class schedule widgets """
        # Get the classes for the day
        valid_classes = self.getClassesForDay()

        # Loop through each set of widgets
        class_widgets = [[self.class_left,  self.time_left,  self.room_left],
                         [self.class_mid,   self.time_mid,   self.room_mid],
                         [self.class_right, self.time_right, self.room_right]]
        
        for index in range(len(class_widgets)):
            # Default to filler text
            class_name = "-------"
            time_text = "-------"
            room_text = "-------"

            # Edit text if class exists
            if index < len(valid_classes):
                class_name = valid_classes[index]
                time_text = self.classes[class_name]["Time"]
                room_text = self.classes[class_name]["Room"]

            # Set the widget text
            class_widgets[index][0].setText(class_name)
            class_widgets[index][1].setText(time_text)
            class_widgets[index][2].setText(room_text)

    def getClassesForDay(self):
        """ Extracts classes that have times for current local day """
        days = {"Monday": "M", "Tuesday": "T", "Wednesday": "W",
                "Thursday": "Th", "Friday": "F"}
        current_day = time.strftime("%A", time.localtime())
        classes = []

        # Check if day is not a weekday
        if current_day not in days:
            return None
        
        # Find classes with proper day
        for class_name in self.classes:
            class_days = self.classes[class_name]["Days"]
            if days[current_day] in class_days:
                classes.append(class_name)

        return classes
    
    def updateWeatherInfo(self):
        """ Gets information from the AccuWeather API and updates weather widgets """
        # Fetch the JSON data
        response = requests.get(url="http://dataservice.accuweather.com/forecasts/v1/daily/1day/346069?apikey=APIKEY")
        response_json = json.loads(response.content)

        # Extract the daily low temperature
        low_temp_info = response_json["DailyForecasts"][0]["Temperature"]["Minimum"]
        self.low_temperature = f"{low_temp_info['Value']}\u00B0 {low_temp_info['Unit']}"

        # Extract the daily high temperature
        high_temp_info = response_json["DailyForecasts"][0]["Temperature"]["Maximum"]
        self.high_temperature = f"{high_temp_info['Value']}\u00B0 {high_temp_info['Unit']}"

        # Extract the rain chances
        has_daytime_rain = response_json["DailyForecasts"][0]["Day"]["HasPrecipitation"]
        has_nighttime_rain = response_json["DailyForecasts"][0]["Night"]["HasPrecipitation"]

        # Select correct rain text
        rain_text = "No chance for rain for all of today!"
        if has_daytime_rain and has_nighttime_rain:
            rain_text = "There's a chance for rain during the day and the night!"
        elif has_daytime_rain:
            rain_text = "There's a chance for rain during the day!"
        elif has_nighttime_rain:
            rain_text = "There's a chance for rain during the night!"

        # Set weather widget texts
        self.temp.setText(f"{self.high_temperature} / {self.low_temperature}")
        self.rain.setText(rain_text)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()