import paramiko
import getpass #암호는 입력되는 문자를 숨기기 위해
 
cli = paramiko.SSHClient()
cli.set_missing_host_key_policy(paramiko.AutoAddPolicy)
 
server = input("Server: ")  # 호스트명이나 IP 주소
user = input("Username: ")  
pwd = getpass.getpass("Password: ") # 암호입력 숨김
 
cli.connect(server, port=22, username=user, password=pwd) # 리턴값이 stdin, stdout, sterr의 튜플로 결과가 반환

# connect parameter 중 timeout (float) – an optional timeout (in seconds) for the TCP connect

# -----------exec_command---------------
# >>>>>> SSH 서버에 어떤 명령을 실행하도록 할 때 사용
# stdin, stdout, stderr = cli.exec_command("ls -la")
# lines = stdout.readlines()
# print(''.join(lines))
 
cli.close()