import tkinter as tk
import clockframe, motivation_message, weatherframe, scheduleframe

# Set up the screen
screen = tk.Tk()
screen.geometry("800x415")
screen.title("PandaPi")

# Create a clock frame
clock_frame = clockframe.ClockFrame(master=screen)
clock_frame.place(x=0, y=0)

# Create the motivational message frame
message_frame = motivation_message.MotivationalMessageFrame(master=screen)
message_frame.place(x=320, y=0)

# Create the weather frame
weather_frame = weatherframe.WeatherFrame(master=screen)
weather_frame.place(x=0, y=160)

# Create the schedule frame
schedule_frame = scheduleframe.ScheduleFrame(master=screen)
schedule_frame.place(x=320, y=96)

# Loop the screen
screen.mainloop()
