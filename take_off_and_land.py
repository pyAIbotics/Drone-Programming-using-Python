from djitellopy import Tello
import time


drone = Tello()
drone.connect()

print("Battery: ", str(drone.get_battery()))

drone.takeoff()
time.sleep(1)
drone.land()


