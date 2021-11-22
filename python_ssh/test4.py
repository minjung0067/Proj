import paramiko, time

def main():
    ssh_client = None 
    recv_size = 9999 
    
    try: 
        ssh_client = paramiko.SSHClient() 
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # host keys 관련 설정 
        ssh_client.connect('192.168.0.190', username='vraptor', password='vraptor') 
        channel = ssh_client.invoke_shell() 
        channel.send('su -\n') 
        outdata, errdata = waitStrems(channel) 
        print(outdata) 
            
        channel.send('pass\n') 
        outdata, errdata = waitStrems(channel) 
        print(outdata) 
        
        channel.send('whoami\n') 
        outdata, errdata = waitStrems(channel)
        print(outdata) 
    
    finally: 
        
        if ssh_client is not None: 
            ssh_client.close() 

def waitStrems(chan): 
    time.sleep(1) 
    outdata=errdata = "" 
    
    while chan.recv_ready(): 
        outdata += chan.recv(1000)
    
    while chan.recv_stderr_ready(): 
        errdata += chan.recv_stderr(1000) 
    
    return outdata, errdata 
    
if __name__ == "__main__":
    main() 
