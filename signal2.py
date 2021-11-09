import os  
import signal  
from time import sleep  

def receiveSignal(signalNumber, frame):  
    status = os.wait()
    print("\nIn parent process-")
    print("Terminated child's process id:", status[0])
    print("Signal number that killed the child process:", status[1])
    print(' received SIGTERM signal ', signalNumber)  
    return
    
def onsigchld():  
    print (' Received end of child process signal '  )
    signal.signal(signal.SIGCHLD,receiveSignal)  

onsigchld()    # setting "Now, I am start to receive signal"
    
pid = os.fork()  
if pid == 0:  
    parent_pid = os.getpid()
    print(' I am a child process ,pid is ',parent_pid)
    while True:
        sleep(20)
    quit()
else:  
    child_pid = os.getpid()
    print(' I am the parent process ,pid is ',child_pid)
    # os.wait() # Wait for the child process to finish  
    while True:
        sleep(1)
        print("1s")

# os.kill(child_pid,signal.SIGTERM)  
# os.kill(66384,signal.SIGUSR1)
