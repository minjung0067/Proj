import sys
import time
from signal import signal, SIGINT, SIGTERM, SIGQUIT
import multiprocessing


#  부모 프로세스가 살아있는 한 자식 프로세스가 죽으면(SIGKILL 또는 SIGTERM 수신) 자동으로 다시 시작되도록
#  상위 프로세스가 SIGTERM/SIGINT를 수신하면 모든 하위 프로세스를 종료한 다음 종료

class HelloWorld(multiprocessing.Process):    
    def run(self):
        signal(SIGTERM, SIG_DFL)
        while True:
            print("Hello World")
            time.sleep(1)

class Counter(multiprocessing.Process):
    def __init__(self):
        super(Counter, self).__init__()
        self.counter = 1

    def run(self):
        signal(SIGTERM, SIG_DFL)
        while True:
            print(self.counter)
            time.sleep(1)
            self.counter += 1

def term_child(_, __):
    for child in children:
        child.terminate()
        child.join()
    sys.exit(0)

if __name__ == '__main__':

    children = [HelloWorld(), Counter()]
    for child in children:
        child.start()

    for signame in (SIGINT, SIGTERM, SIGQUIT):
        signal(signame, term_child)

    while True:
        for i, child in enumerate(children):
            if not child.is_alive():
                children[i] = type(child)()
                children[i].start()
        time.sleep(1)