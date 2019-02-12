import handtouchcheck

def on():
    print("grab handle")

def off():
    print("grabbed handle")

t = handtouchcheck.handtouchcheck(on, off)
t.start()

while True :
    pass
