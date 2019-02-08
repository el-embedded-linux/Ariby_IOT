import handtouchcheck

def onR():
    print("R on")

def onL():
    print("L on")

def offR():
    print("R off")

def offL():
    print("L off")

t = handtouchcheck.handtouchcheck(onR, onL, offR, offL)
t.start()

while True :
    pass
