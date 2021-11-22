import tty, sys, termios

filedescriptors = termios.tcgetattr(sys.stdin)
tty.setcbreak(sys.stdin)
x = 0
command = ""
while 1:
  x = sys.stdin.read(1)[0]
  if x == "\n":
    print("command :",command)
    command = ""
    break
  command += x

  termios.tcsetattr(sys.stdin, termios.TCSADRAIN,filedescriptors)