import handtouch

def on():
    print("grab handle")

def off():
    print("grabbed handle")

t = handtouch.handtouchcheck(on, off)
t.start()

while True :
    pass
