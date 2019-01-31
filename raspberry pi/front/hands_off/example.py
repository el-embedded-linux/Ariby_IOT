import handsoff

def handson():
    print("손잡이를 잡아주세요")

def handsoff():
    print("손잡이를 다시 잡았습니다.")

t = touch.handsoff(handson, handsoff)
t.start()

while True:
    pass
