import tkinter as tk
import time

"""
This code is based on this Stack Overflow answer:
https://stackoverflow.com/a/34022680

Changes are made to fit the formatting that I want.
"""


def current_iso8601():
    """Get current date and time"""

    return time.strftime("%B %d, %Y\n%H:%M:%S\n%A", time.localtime())

class ClockFrame(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.displayElements()

    def displayElements(self):
        self.now = tk.StringVar()
        self.time = tk.Label(self, font=('Helvetica', 24))
        self.time.pack(side="left")
        self.time["textvariable"] = self.now

        self.onUpdate()

    def onUpdate(self):
        # update displayed time
        self.now.set(current_iso8601())
        # schedule timer to call myself after 1 second
        self.after(1000, self.onUpdate)

