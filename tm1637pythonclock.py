#code revised by Apurva Singh [embedded engineer]
#rev 10.2.2020

import sys #imports from system
import time #imports time from the system
import datetime #imports date from system. We are not using this though
import RPi.GPIO as GPIO #imports GPIO library for tm1637
import tm1637 #imports the tm1637 library

#CLK -> GPIO23 (Pin 16)
#Di0 -> GPIO24 (Pin 18)

Display = tm1637.TM1637(23,24,tm1637.BRIGHT_TYPICAL)
Display.Clear()
Display.SetBrightnes(7) #tm1637 supports brightness from 0-7

while(True): 
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute   #all these are declared for pulling time
    second = now.second
    currenttime = [ int(hour / 10), hour % 10, int(minute / 10), minute % 10 ] 
    #tm1637 needs each digit to be printed seperately
    print(currenttime)#printing the current time on output screen
    Display.Show(currenttime)#printing the current time on tm1637
    Display.ShowDoublepoint(second % 2) # this is for showing the double point

time.sleep(2)
#this gives delay of 2 sec. You can increase depending on your requirement.
# Hope you like the Code
  # If you face any issue feel free to mail at singhapurva55@gmail.com  