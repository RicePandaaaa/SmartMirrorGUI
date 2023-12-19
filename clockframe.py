import tkinter as tk
import time


def current_iso8601():
    """Get current date and time in ISO8601"""
    # https://en.wikipedia.org/wiki/ISO_8601
    # https://xkcd.com/1179/
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

