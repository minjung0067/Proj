import socket
from contextlib import closing

def check_socket(host, port):
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
      if sock.connect_ex((host, port)) == 0:
        return True
      else:
        return False

i = 0
while i<20000:
    if check_socket('192.168.100.107',i):
        print(i,'Port open')
    if i == 19999:
        print("finish")
    # else:
    # print('Port closed')