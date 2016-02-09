# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 16:34:01 2016

@author:
"""

import brickpi
import time
import random
import math


def initInterface(interface, motors):
    interface.initialize()

    interface.motorEnable(motors[0])
    interface.motorEnable(motors[1])

    motorParams = interface.MotorAngleControllerParameters()
    motorParams.maxRotationAcceleration = 8.0
    motorParams.maxRotationSpeed = 13.0
    motorParams.feedForwardGain = 255/20.0
    motorParams.minPWM = 18.0
    motorParams.pidParameters.minOutput = -255.0
    motorParams.pidParameters.maxOutput = 255.0
    motorParams.pidParameters.k_p = 250.0
    motorParams.pidParameters.k_i = 809.0909
    motorParams.pidParameters.k_d = 11.0

    motorParams2 = interface.MotorAngleControllerParameters()
    motorParams2.maxRotationAcceleration = 8.0
    motorParams2.maxRotationSpeed = 13.0
    motorParams2.feedForwardGain = 255/20.0
    motorParams2.minPWM = 18.0
    motorParams2.pidParameters.minOutput = -255.0
    motorParams2.pidParameters.maxOutput = 255.0
    motorParams2.pidParameters.k_p = 250.0
    motorParams2.pidParameters.k_i = 852.1739
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

def initParticles(NUMBER_OF_PARTICLES):
    particleSet=[]
    weight = 1/NUMBER_OF_PARTICLES
    tuple =(200,200,0)
    for i in range(NUMBER_OF_PARTICLES):
        particleSet.append(tuple)
        
    return particleSet

def go10Cm(interface, motors, particleSet):
    ePer10cm=1
    fPer10cm=1
    sc = 5
    D=40
    newparticleSet=[]
    
    goStraight(D, interface, motors)
    for particle in particleSet:
        error = random.gauss(0,ePer10cm)
        
        x = particle[0]+((D+error)*math.cos(particle[2]/(360)*2*3.14))*sc
        y = particle[1]+((D+error)*math.sin(particle[2]/(360)*2*3.14))*sc
        theta = (particle[2]+random.gauss(0,fPer10cm))%360
        particle = (x, y, theta)
        newparticleSet.append(particle)
        
    return (newparticleSet)

            
def turn90Deg(interface, motors, particleSet):
    gPer90=5
    newparticleSet=[]
    angle = 90

    turn(angle, interface, motors)
    for particle in particleSet:
        new_angle = (particle[2] + angle + random.gauss(0,gPer90))%360
        new_particle = (particle[0], particle[1], new_angle)
        newparticleSet.append(new_particle)

    return (newparticleSet)
