# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 16:34:01 2016

@author:
"""

import brickpi
import time

def initInterface(interface, motors):
    interface.initialize()

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
    motorParams.pidParameters.k_i = 1309.0909
    motorParams.pidParameters.k_d = 11.0

    motorParams2 = interface.MotorAngleControllerParameters()
    motorParams2.maxRotationAcceleration = 8.0
    motorParams2.maxRotationSpeed = 16.0
    motorParams2.feedForwardGain = 255/20.0
    motorParams2.minPWM = 18.0
    motorParams2.pidParameters.minOutput = -255.0
    motorParams2.pidParameters.maxOutput = 255.0
    motorParams2.pidParameters.k_p = 240.0
    motorParams2.pidParameters.k_i = 1252.1739
    motorParams2.pidParameters.k_d = 11.5

    interface.setMotorAngleControllerParameters(motors[0],motorParams)
    interface.setMotorAngleControllerParameters(motors[1],motorParams2)


def goStraight(distCm, interface, motors):
    radianPerCm = 0.3625
    angle = distCm * radianPerCm 
    interface.increaseMotorAngleReferences(motors, [angle, angle])

    while not interface.motorAngleReferencesReached(motors) :
        motorAngles = interface.getMotorAngles(motors)
        time.sleep(0.1)
        ## Maybe add a break after x seconds
	

def turn(angleDeg, interface, motors):
    radianPerDegre = 0.05622222222
    angle = angleDeg * radianPerDegre 
    interface.increaseMotorAngleReferences(motors, [angle, -angle])

    while not interface.motorAngleReferencesReached(motors) :
        motorAngles = interface.getMotorAngles(motors)
        time.sleep(0.1)
