from django.shortcuts import render

from django.http import HttpResponse
from django.template import Context, loader

from sensor import *

import time, sys, signal, atexit

import pyupm_mma7660 as upmMMA7660

def turn(request):
	
#    signal.signal(signal.SIGINT, SIGINTHandler)
    myDigitalAccelerometer = upmMMA7660.MMA7660(

                    upmMMA7660.MMA7660_I2C_BUS,

                    upmMMA7660.MMA7660_DEFAULT_I2C_ADDR);

# place device in standby mode so we can write registers
    myDigitalAccelerometer.setModeStandby()

# enable 64 samples per second
    myDigitalAccelerometer.setSampleRate(upmMMA7660.MMA7660.AUTOSLEEP_1)

# place device into active mode
    myDigitalAccelerometer.setModeActive()

    x = upmMMA7660.new_intp()
    y = upmMMA7660.new_intp()
    z = upmMMA7660.new_intp()
 
    ax = upmMMA7660.new_floatp()
    ay = upmMMA7660.new_floatp()
    az = upmMMA7660.new_floatp()
    if (1):
        myDigitalAccelerometer.getRawValues(x, y, z)
        #print(x,y,z)
        outputStr = ("Raw values: x = {0}"
                     " y = {1}"
                     " z = {2}").format(upmMMA7660.intp_value(x),
                                        upmMMA7660.intp_value(y),

                                        upmMMA7660.intp_value(z))

        var1 = int(upmMMA7660.intp_value(x))
        var2 = int(upmMMA7660.intp_value(y))
        var3 = int(upmMMA7660.intp_value(z))

        print(output_command(var1, var2, var3))
 

        #time.sleep(.5)
    	return HttpResponse("New Value Here")

