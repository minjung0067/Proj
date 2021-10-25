import socket
from contextlib import closing

def check_socket(host, port):
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
      if sock.connect_ex((host, port)) == 0:
        return "True"
      else:
        return "False"

# i = 11100
# while i<11112:
#     if check_socket('192.168.1.123',i):
#         print(i,'Port open')
#     if i == 19999:
#         print("finish")
#         break
#     i = i + 1

print(check_socket('192.168.1.123',11111))