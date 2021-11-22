import paramiko, time

def waitStrems(chan): 
    time.sleep(1) 
    outdata=errdata = "" 
    while chan.recv_ready(): 
        outdata += str(chan.recv(1000))      
    while chan.recv_stderr_ready(): 
        errdata += str(chan.recv_stderr(1000)) 
    return outdata, errdata


passwd=input("pw:")

connection = paramiko.SSHClient()

connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())

connection.connect('192.168.0.190', username='vraptor', password=passwd, look_for_keys=False, allow_agent=False)
# look_for_keys: set to False to disable searching for discoverable private key files in ~/.ssh/
# allow_agent: set to False to disable connecting to the SSH agent

channel = connection.invoke_shell()
channel.settimeout(30)

channel.send("cd /WORK\n")
outdata, errdata = waitStrems(channel)
print(outdata)

channel.send("python helloworld.py\n")
status='Normal'
while status!='End':
    time.sleep(1)
    resp = str(channel.recv(30))
    print(resp)
    if resp.count('termination')>0:
        status='End'

print('Thank you!')

channel.close()