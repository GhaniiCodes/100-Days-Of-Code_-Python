import time
import ctypes

def remind_to_drink_water():

    message = "Time to drink water! Stay hydrated."
    title = "Drink Water Reminder"
    
    
    ctypes.windll.user32.MessageBoxW(0, message, title, 0x40 | 0x1)
    
remind_to_drink_water()