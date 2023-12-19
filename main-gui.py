import tkinter as tk
import clockframe

# Set up the screen
screen = tk.Tk()
screen.geometry("800x480")
screen.title("PandaPi")

# Create a clock
current_time = clockframe.ClockFrame(master=screen)
current_time.place(x=0, y=0)

# Loop the screen
screen.mainloop()