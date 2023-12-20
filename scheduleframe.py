import tkinter as tk
import time


class ScheduleFrame(tk.Frame):
    def __init__(self, master=None):
        # Set up the frame
        tk.Frame.__init__(self, master, height=384, width=480,
                          highlightbackground="black", highlightthickness=1)
        self.pack(fill="both")
        self.pack_propagate(0)

        # Set up schedule information
        self.classes = {"ESET-349 LEC": {"Room": "THOM-107A", "Time": "8:00am-8:50am",   "Days": "M/W/F"},
                        "ESET-349 LAB": {"Room": "THOM-101A", "Time": "2:00am-4:30pm",   "Days": "M"},
                        "ESET-359 LEC": {"Room": "THOM-107A", "Time": "11:10am-12:25pm", "Days": "T/Th"},
                        "ESET-359 LAB": {"Room": "THOM-204",  "Time": "8:00am-10:30am",  "Days": "Th"},
                        "MXET-300 LEC": {"Room": "ZACH-442",  "Time": "12:45pm-1:35pm",  "Days": "T/Th"},
                        "MXET-300 LAB": {"Room": "FERM-006",  "Time": "2:00pm-4:30pm",   "Days": "W"},
                        "MMET-361 LEC": {"Room": "FRAN-102",  "Time": "12:40pm-1:30pm",  "Days": "M/W"},
                        "MMET-361 LAB": {"Room": "THOM-115B", "Time": "8:00am-9:50pm",   "Days": "T"}}

        # Show the text
        self.displayElements()

    def displayElements(self):
        """ Displays the message within the frame """

        # Set up title label
        self.title_label = tk.Label(self, font=('Helvetica', 20), text="Schedule")
        self.title_label.pack(fill="both")

        # Set up schedule label
        self.schedule_message = tk.StringVar(value="No classes today!")
        self.schedule_label = tk.Label(self, font=('Helvetica', 15), wraplength=372, justify=tk.LEFT)
        self.schedule_label.pack(fill="both", expand=1)
        self.schedule_label["textvariable"] = self.schedule_message

        # Prepare text for schedule
        schedule_text = []
        valid_classes = self.getClassesForDay()

        # If no classes today, don't change text
        if valid_classes is None:
            return
        
        # Else, set up the new schedule text
        for class_name in valid_classes:
            class_room = self.classes[class_name]["Room"]
            class_time = self.classes[class_name]["Time"]
            schedule_text.append(f"Subject: {class_name}\nRoom: {class_room}\nTime: {class_time}")

        schedule_text = "\n\n".join(schedule_text)
        self.schedule_message.set(schedule_text)

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
