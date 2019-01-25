import blecomm

# speedmeterStart 의 첫번째 인자로 블루투스 디바이스의 주소를 입력
# 두번째 인자로는 콜백 함수를 등록해줌
# 블루투스로부터 스피드값이 올때마다 콜백 함수가 실행됨

def getSpeed(data):
    print("speed : "+data)

blecomm.speedmeterStart('F0:45:DA:10:B9:C1',getSpeed)
