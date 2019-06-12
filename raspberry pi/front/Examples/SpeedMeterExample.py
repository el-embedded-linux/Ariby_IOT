import SpeedMeter

def SpeedUpdate(data):
    print("speed : "+data)

speedmeter = SpeedMeter.SpeedMeter('F0:45:DA:10:B9:C1',SpeedUpdate)
speedmeter.start_b()

while True:
    pass
