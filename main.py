from gpiozero import DistanceSensor
import time
from gpiozero import LED # LED is actually relay
import statistics

sensor = DistanceSensor(echo=14, trigger=15, max_distance=2, threshold_distance=0.05)

CALIBRATION = 0.025
MAX_DIST = 1.40
TANK_HEIGHT = 1.8

relay = LED(18)
relay.on()

loop_num = 30

log_file = "/home/pi/Desktop/log.txt"

i = 0

while True:
    i += 1
    if i > 100:
        i = 0
        #open(log_file, 'w').close()
        continue
            
    distance = []
    for j in range(loop_num):
        distance.append(sensor.distance + CALIBRATION)
        time.sleep(0.2)
        
    #print(distance)
    distance = statistics.median(distance)
    time_rn = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())

    if distance > MAX_DIST:
        relay.on()
        pump_status = "OFF"
        #print(f"{time_rn} Tank:OFF {distance:.3}m {100*(1-distance/TANK_HEIGHT):.3}%")
    else:
        relay.off()
        pump_status = "ON"
        #print(f"{time_rn} Tank:ON {distance:.3}m {100*(1-distance/TANK_HEIGHT):.3}%")

        
    with open(log_file,'a') as log:
        log.write(f"{i} {time_rn} Tank:{pump_status} {distance:.3}m {100*(1-distance/TANK_HEIGHT):.3}%\n")
    time.sleep(1)