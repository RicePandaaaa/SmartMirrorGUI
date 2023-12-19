import tkinter as tk
import clockframe

# Set up the screen
screen = tk.Tk()
screen.attributes('-fullscreen', True)

# Create a clock
current_time = clockframe.ClockFrame(master=screen)

# Loop the screen
screen.mainloop()