#!/usr/bin/env python
from time import sleep
from e_drone.drone import *
from e_drone.protocol import *

import rospy
from geometry_msgs.msg import Pose

mode_flight = 0
def eventState(state):
    print("-modeSystem        : {0}".format(state.modeSystem))
    print("-modeFlight        : {0}".format(state.modeFlight))
    print("-modeControlFligh  : {0}".format(state.modeControlFlight))
    print("-modeMovement      : {0}".format(state.modeMovement))
    print("-headless          : {0}".format(state.headless))
    print("-controlSpeed      : {0}".format(state.controlSpeed))
    print("-sensorOrientation : {0}".format(state.sensorOrientation))
    print("-battery           : {0}".format(state.battery))
    mode_flight = state.modeFlight

def xyzw(msg):
    rospy.loginfo("x, y, z, w: [%f, %f, %f, %f]"%(msg.orientation.x, msg.orientation.y, msg.orientation.z, msg.orientation.w))
    if msg.orientation.w == 1:
        print("takeoff")
        drone.sendTakeOff()
        sleep(3)
    elif msg.orientation.w == -1:
        print("landing")
        drone.sendLanding()
        sleep(3)
    else:
        drone.sendControl(msg.orientation.x*10, msg.orientation.y*10, msg.orientation.z*10,0)
        # drone.sendControlPosition(msg.orientation.x/100, msg.orientation.y/100, msg.orientation.z/100,1,0,0)
        sleep(0.1)



if __name__ == '__main__':

    drone = Drone()
    drone.open()

    drone.setEventHandler(DataType.State, eventState)

    drone.sendRequest(DeviceType.Drone, DataType.State)
    sleep(0.1)

    rospy.init_node('drone_control', anonymous=True)
    
    rospy.Subscriber("xyzw", Pose, xyzw)
    rospy.spin()



    drone.close()