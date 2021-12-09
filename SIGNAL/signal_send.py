import os  
import signal  
    
# Sending signals, 16175 It's the one that binds the signal handler pid , need to modify themselves   
os.kill(66384,signal.SIGTERM)  
# Sending signals, 16175 It's the one that binds the signal handler pid , need to modify themselves   
os.kill(66384,signal.SIGUSR1)