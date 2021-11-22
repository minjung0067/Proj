import paramiko
import getpass
import time
 
cli = paramiko.SSHClient()
cli.set_missing_host_key_policy(paramiko.AutoAddPolicy)
cli.connect("test.com", username="user", password="pwd")
 
# 새로운 interactive shell session 생성
channel = cli.invoke_shell()
 
# 명령 송신
channel.send("ls -la\n")
time.sleep(1.0)
# 결과 수신
output = channel.recv(65535).decode("utf-8")
print(output)
 
cli.close()