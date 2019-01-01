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
    #writable = yes #쓰기 가능 여부
    browseable = yes #공유 폴더의 목록을 보여줌

삼바 재실행

    $sudo service samba restart 또는
    $sudo /etc/init.d/samba restart
