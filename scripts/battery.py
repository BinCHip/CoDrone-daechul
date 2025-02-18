from time import sleep
from e_drone.drone import *
from e_drone.protocol import *

def eventState(state, agr_print=0):
    if agr_print:
        print("battery remain()")
        print("-modeSystem        : {0}".format(state.modeSystem))
        print("-modeFlight        : {0}".format(state.modeFlight))
        print("-modeControlFligh  : {0}".format(state.modeControlFlight))
        print("-modeMovement      : {0}".format(state.modeMovement))
        print("-headless          : {0}".format(state.headless))
        print("-controlSpeed      : {0}".format(state.controlSpeed))
        print("-sensorOrientation : {0}".format(state.sensorOrientation))
        print("-battery           : {0}".format(state.battery))
    return state

if __name__ == '__main__':

    drone = Drone()
    drone.open()

    drone.setEventHandler(DataType.State, eventState)

    data = drone.sendRequest(DeviceType.Drone, DataType.State)
    sleep(0.1)
    print(data)

    drone.close()