from djitellopy import Tello

tello = Tello()

try:
    tello.connect()
except:
    print("Unable to connect")

tello.takeoff()
tello.land()