import tkinter as ui
import time

window = ui.Tk()
window.title("Clock")

def update_clock():
    time_in_sec = int(time.time())
    sec_in_day = 24 * 60 * 60
    sec_in_hour = 60 * 60
    sec_in_minute = 60
    
    hours = (time_in_sec % sec_in_day) // sec_in_hour
    hours = hours + 8
    minutes = (time_in_sec % sec_in_hour) // sec_in_minute
    seconds = time_in_sec % sec_in_minute
    
    now = str(hours) + ":" + str(minutes) + ":" + str(seconds)
    digitalText.config(text = now)
    digitalText.after(1000, update_clock)

digitalText = ui.Label(window,text = "00:00:00", font = ("Helvetica", 50), background = "black", foreground="#e48af2")
digitalText.pack(pady = 40)

update_clock()
window.mainloop()