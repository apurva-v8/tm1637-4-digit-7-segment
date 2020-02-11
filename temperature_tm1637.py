#code developed by apurva singh[Embedded Engineer]
# rev 10.2.2020

from gpiozero import CPUTemperature #pull temperature from board of raspberry pi
import time #importing time makes no sense.
import datetime #importing this also makes no sense.
import sys #this is required to pull temperature from the system
import RPi.GPIO as GPIO #this is required inorder for the tm1637 to run
import tm1637 #this pulls the main library so we can use prebui3lt functions.
#CLK -> GPIO23 (Pin 16)
#Di0 -> GPIO24 (Pin 18)
##GUI DEFINITIONS ##
Display = tm1637.TM1637(23,24,tm1637.BRIGHT_TYPICAL) #inititating display
Display.Clear() #clear display
Display.SetBrightnes(7) #setting the brightness of the display
while(True): 
    b = CPUTemperature()
    cpu = CPUTemperature() 
    a = int(cpu.temperature) #converting temperature in integers as it can be in decimal
    c = [ 0, 0, int(a / 10), a % 10 ] #logic to print temperature on 7segment 4 digit
    print(c) #print temperature on display
    Display.Show(c) #display temperature on display using function
    time.sleep(2) #delay of 2 sec. You can increase this as per your requirement.
    