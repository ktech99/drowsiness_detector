import time

start_time = int(round(time.time() * 1000))
stop_time = int(round(time.time() * 1000))
while True:
        execfile('detector.py')
        time.sleep(3)
