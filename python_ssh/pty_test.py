import paramiko as paramiko
from paramiko import AutoAddPolicy
import time

# for input without enter
import sys
import tty
import termios

sshClient = paramiko.SSHClient()
sshClient.load_system_host_keys() #시스템(읽기 전용) 파일에서 호스트 키를 로드
sshClient.set_missing_host_key_policy(AutoAddPolicy()) #알려진 호스트 키 없이 서버에 연결할 때 사용할 정책을 설정 -> 호스트 이름과 키를 로컬 HostKeys개체 에 자동으로 추가 하고 저장
sshClient.connect('0.0.0.0', username='minjung', password='dlalswjd')

channel = sshClient.get_transport().open_session() #서버에 새 채널 요청
channel.get_pty() # 이 줄 없으면 Welcome to Ubuntu는 뜨고 그 뒤로 쉘이 무반응
channel.invoke_shell()  #이 줄 없으면 아예 첨부터 아무것도 안 뜸

def getkey():
    """단일키 누르는 것을 받아옴"""
    fd = sys.stdin.fileno()
    original_attributes = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, original_attributes)
    return ch

while True:
    command = getkey()
    channel.send(command)

    while True:
        if channel.recv_ready():
            output = channel.recv(1024)
            print(output.decode('utf-8'), end='')
        else:
            time.sleep(0.1)
            if not(channel.recv_ready()):
                break

        sshClient.close()

