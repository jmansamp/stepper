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

myMotor = mh.getMotor(3)

myMotor.setSpeed(300)

while(True):
	myMotor.run(Adafruit_MotorHAT.BACKWARD)
	time.sleep(1.0)
