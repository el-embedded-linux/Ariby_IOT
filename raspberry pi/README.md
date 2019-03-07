# EL_IOT\_Raspberry Pi

----
## 라즈비안 OS 설치
1. 라즈베리 파이 공식사이트 [링크](https://www.raspberrypi.org/downloads/raspbian/)에서 라즈비안 이미지 다운로드
2. sd카드에 이미지 작성을 위한 프로그램 [링크](https://sourceforge.net/projects/win32diskimager/) 다운로드
3. sd카드에 다운받은 이미지를 올림
4. 라즈베리파이에 sd카드 장착 전원 공급

----
## VNC 사용
    $vncserver -geometry 1280x720

----
## SAMBA 설치 및 사용
SAMBA 설치

    $sudo apt-get update
    $sudo apt-get install samba samba-common-bin

페스워드 설정

    $ sudo smbpasswd -a pi

삼바 접속 설정
    
    $ sudo vi /etc/samba/smb.conf

    #아래 내용 추가
    [pi]
    comment = comment
    path = /home/pi #공유할 디렉토리
    valid user = pi #사용자
    writable = yes #쓰기 가능 여부
    browseable = yes #공유 폴더의 목록을 보여줌

삼바 재실행

    $sudo service samba restart 또는
    $sudo /etc/init.d/samba restart

5인치 터치스크린용 드라이버 설치

    git clone https://github.com/waveshare/LCD-show.git
    sudo ./LCD5-show
    


라즈베리파이에 설치되는 opencv 페키지는 2.4버전으로 파이썬 2버전 까지만 지원되기때문에
파이썬3에서 opencv 라이브러리를 설치하기 위해서는 opencv 3.x 버전을 설치해야한다
원래는 opencv git에서 clone을 받아 build를 해야하지만 시간이 3시간 이상으로 오래 걸리기 때문에
미리 빌드되어있는 페키지를 구해서 설치한다

https://blog.xcoda.net/97 를 참고했습니다.


git clone https://github.com/dltpdn/opencv-for-rpi.git

cd opencv-for-rpi/stetch/3.3.0

sudo apt install -y ./OpenCV*.deb

pkg-config ?modversion opencv
