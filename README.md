# SpheroBB8-python
**Sphero's BB8 droid** 
*The droid you've been looking for.*

Now even better with a python API library!

Use "sudo hcitool lescan" to find BB8's MAC address 
input it at "`deviceAddress =`" (line 244) in the Sphero class in BB8_driver.py

**

***Included Scripts:***

**
**BB8Test.py**
A simple program that connects to BB8 and flashes the internal RGB LED red to green to blue. You can take it a step further and add `bb8.roll` commands to make him move using the API. 

**BB8joyDrive.py**
*requires PyGame library* 

Allow you to drive BB8 with a joystick/gamepad.
Shows on screen feedback of analog stick as well as speed and heading
Currently setup for a Xbox 360 controller.

 - Left analog stick controls BB8's movement, much the like app!   
 - Holding the Left trigger stops BB8.
 - Tapping the Left bumper changes BB8's heading - used to calibration.   
 -  Holding the Right bumper turns on BB8's blue 'tail light' to aid in calibration.

> Adapted the sphero driver library from:
> https://github.com/mmwise/sphero_ros/tree/groovy-devel/sphero_driver/src/sphero_driver
> 
> Used the bluetooth 'stuff' from:
> https://gist.github.com/ali1234/5e5758d9c591090291d6

**TODO:**
Tie in the btle handleNotifcations to Sphero response API
    

 - getting sensor info, command responses, etc. back from BB8

