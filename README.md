# Arduino_Robot

**Version 1.0.0**

A robot will find a way to get out of a maze using an ultrasonic sensor and various motors. 

Serial communication between Python and Arduino will be established in order to use Arduino as a data adquisition program and Python as a computation program.

## Contributors 

- Mateo Caso <https://github.com/CasoMateo>
- Eduardo L. Santos <https://github.com/EduardoSantos7> 

## Components 

- Arduino Uno. 
- Driver L298N. 
- 6 AA Bateries. 
- A set of jumpers. 
- 4 DC Motors. 
- Servomotor.
- Ultrasonic Sensor. 

## Demo Code 

If distance_obs < min_distance:
  move_forward()
Else: 
  Serial.write(distance_sides().encode()) 
  if Serial.read() == left: 
     move_left() 
  else: 
     move_right() 
 
## Installation Details 

Arduino, itself, and its drivers were installed through <https://www.arduino.cc/en/software>.

Serial needs to be installed through Python with the use of the **_PiP_** command. 
If the file is not found, creating a virtual environment will be necessary..

## Robot and Results 

<img src="66A5C48E-E8BE-4795-9D71-1F0A839B0C17.jpeg" width = "400" >
<img src="E4900B3D-6750-4402-B9D2-69E130328BBD.jpeg" width = "400" >
<img src="F2C9DC3C-65B6-49E2-88D4-807DC04BCCBC.jpeg" width = "400" >
