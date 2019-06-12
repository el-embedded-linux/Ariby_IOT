import handsoff

def on():
    print("Please grab the handle")

def off():
    print("grabbed the handle again")

t = handsoff.handsoff(on, off)
t.start()

while True:
    pass
