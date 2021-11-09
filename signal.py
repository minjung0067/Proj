import os
import psutil

print(" Original Process ID : %s" % os.getpid()) 
pid = os.fork()              

if pid :
    print('I am Parent Process(PID: %s), My Child Process(PID: %s)' % (os.getpid(), pid))
else :
    print('I am Child Process(PID: %s), My Parent Prcess(PID: %s)' % (os.getpid(), os.getppid()))


# child 킬
os.killpg(os.getpid(), signal.SIGTERM)
# signal 받기


print('Finish : PID=%s' % os.getpid())


def kill_all_child_processes(pid=None):
    # get current process if pid not provided
    include_parent = True
    if not pid:
        pid = os.getpid()
        include_parent = False
    print("\nLeaving process id {}".format(pid))
    try:
        parent = psutil.Process(pid)
    except psutil.Error:
        # could not find parent process id
        return
    for child in parent.children(recursive=True):
        child.kill()
    if include_parent:
        parent.kill() 