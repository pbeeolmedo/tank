from gpiozero import DistanceSensor
from time import sleep
from gpiozero import LED # LED is actually relay

sensor = DistanceSensor(echo=14, trigger=15, max_distance=2, threshold_distance=0.05)

CALIBRATION = 0.025
MAX_DIST = 1.35

relay = LED(18)
relay.on()

while True:
    distance = sensor.distance + CALIBRATION
    if distance > MAX_DIST:
        relay.on()
        print("Tank:OFF")
    else:
        relay.off()
        print('Tank:ON -- Dist = ',distance, 'm')
    sleep(5)