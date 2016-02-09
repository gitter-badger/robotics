import brickpi
import time

interface=brickpi.Interface()
interface.initialize()

motors = [2,0]

interface.motorEnable(motors[0])
interface.motorEnable(motors[1])

gain =100.0

motorParams = interface.MotorAngleControllerParameters()
motorParams.maxRotationAcceleration = 10.0
motorParams.maxRotationSpeed = 16.0
motorParams.feedForwardGain = 255/20.0
motorParams.minPWM = 18.0
motorParams.pidParameters.minOutput = -255
motorParams.pidParameters.maxOutput = 255
motorParams.pidParameters.k_p = gain
motorParams.pidParameters.k_i = 0.0
motorParams.pidParameters.k_d = 0.0

motorParams3 = interface.MotorAngleControllerParameters()
motorParams3.maxRotationAcceleration = 10.0
motorParams3.maxRotationSpeed = 16.0
motorParams3.feedForwardGain = 255/20.0
motorParams3.minPWM = 18.0
motorParams3.pidParameters.minOutput = -255
motorParams3.pidParameters.maxOutput = 255
motorParams3.pidParameters.k_p = gain
motorParams3.pidParameters.k_i = 0.0
motorParams3.pidParameters.k_d = 0.0

interface.setMotorAngleControllerParameters(motors[0],motorParams)
interface.setMotorAngleControllerParameters(motors[1],motorParams3)

brickpi.Interface.startLogging(interface,"moter3_"+str(gain)+".txt")

while True:
	angle = float(input("Enter a angle to rotate (in radians): "))

	interface.increaseMotorAngleReferences(motors,[angle,angle])

	while not interface.motorAngleReferencesReached(motors) :
		motorAngles = interface.getMotorAngles(motors)
		if motorAngles :
			print "Motor angles: ", motorAngles[0][0], ", ", motorAngles[1][0]

		time.sleep(0.1)

	print "Destination reached!"
	brickpi.Interface.stopLogging(interface)
	

interface.terminate()
