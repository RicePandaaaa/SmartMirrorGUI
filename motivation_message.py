import tkinter as tk


class MotivationalMessageFrame(tk.Frame):
    def __init__(self, master=None):
        # Set up the frame
        tk.Frame.__init__(self, master, height=96, width=480,
                          highlightbackground="black", highlightthickness=1)
        self.pack(fill="both", expand=1)
        self.pack_propagate(0)

        # Show the text
        self.displayElements()

    def displayElements(self):
        """ Displays the message within the frame """

        # Set up the label itself
        self.message = tk.StringVar()
        self.message_label = tk.Label(self, font=('Helvetica', 20))
        self.message_label.pack(fill="both", expand=1)
        self.message_label["textvariable"] = self.message

        # Set the message to be displayed
        self.setMessage("Be the teacher you always wanted!")

    def setMessage(self, message):
        """ Sets the displayed message """
        self.message.set(message)