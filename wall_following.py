import brickpi
import time
from collections import deque

interface=brickpi.Interface()
interface.initialize()

port = 0
motors = [2,3]
speed = 4.0

interface.sensorEnable(port, brickpi.SensorType.SENSOR_ULTRASONIC);
interface.motorEnable(motors[0])
interface.motorEnable(motors[1])

motorParams = interface.MotorAngleControllerParameters()
motorParams.maxRotationAcceleration = 8.0
motorParams.maxRotationSpeed = 16.0
motorParams.feedForwardGain = 255/20.0
motorParams.minPWM = 18.0
motorParams.pidParameters.minOutput = -255.0
motorParams.pidParameters.maxOutput = 255.0
motorParams.pidParameters.k_p = 240.0
motorParams.pidParameters.k_i = 109.0909
motorParams.pidParameters.k_d = 11.0

motorParams2 = interface.MotorAngleControllerParameters()
motorParams2.maxRotationAcceleration = 8.0
motorParams2.maxRotationSpeed = 16.0
motorParams2.feedForwardGain = 255/20.0
motorParams2.minPWM = 18.0
motorParams2.pidParameters.minOutput = -255.0
motorParams2.pidParameters.maxOutput = 255.0
motorParams2.pidParameters.k_p = 240.0
motorParams2.pidParameters.k_i = 152.1739
motorParams2.pidParameters.k_d = 11.5

interface.setMotorAngleControllerParameters(motors[0],motorParams)
interface.setMotorAngleControllerParameters(motors[1],motorParams)

interface.setMotorRotationSpeedReferences(motors,[speed,speed])

speed0 = speed
speed1 = speed

k_p_wall = 0.01

desired = 25
readings = deque([])

print "Press Ctrl+C to exit"

#look left or look right
#360 sonar or just on top
while True:
    usReading = interface.getSensorValue(port)
    print usReading
    
    if(usReading[0] < 250):
        if(len(readings) < 3):
            readings.append(usReading[0])
            error = usReading[0]-desired   # why take usReading[0] as default?
        else:
            readings.append(usReading[0])
            readings.popleft()
            error = readings[1] - desired
            print error    
            
        speed0 = speed - 0.5 * k_p_wall * error
        speed1 = speed + 0.5 * k_p_wall * error

        
#    else:
#        speed0 = speed0Last
#        speed1 = speed1Last
    
    print speed0, speed1
    interface.setMotorRotationSpeedReferences(motors,[speed0,speed1])
    
    time.sleep(0.1)
