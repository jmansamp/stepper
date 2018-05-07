from Adafruit_MotorHAT import Adafruit_MotorHAT

import time 
import atexit

mh =  Adafruit_MotorHAT(addr = 0x60)

def turnOFFMotors():
	mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOFFMotors)

myStepper = mh.getStepper(200,1)

myStepper.setSpeed(255)



myStepper.step(1000, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.DOUBLE)

