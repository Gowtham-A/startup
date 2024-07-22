from tkinter import Label, Tk 
import time

app_window = Tk() 
app_window.title("Digital Clock") 
app_window.geometry("420x150") 
app_window.resizable(1, 1)

text_font = ("Boulder", 68, 'bold')
background = "#f2e750"
foreground = "#363529"
border_width = 25

label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width) 
label.grid(row=0, column=1)

def digital_clock(): 
    # Get current time in 12-hour format with AM/PM indicator
    time_live = time.strftime("%I:%M:%S %p")  # %I for 12-hour format, %p for AM/PM
    label.config(text=time_live) 
    label.after(200, digital_clock)

digital_clock()
app_window.mainloop()
