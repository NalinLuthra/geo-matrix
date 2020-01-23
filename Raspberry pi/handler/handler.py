import os
import signal
import subprocess
import time 

# The os.setsid() is passed in the argument preexec_fn so
# it's run after the fork() and before  exec() to run the shell.
pro = subprocess.Popen('rosrun velodyne_driver vdump final-test-last enp0s31f6', shell=True) 
#time.sleep(5)
print(os.getpgid(pro.pid))
while True:
  q = raw_input("Enter option for handler")
  print(q)
  if q == 'r':
    #os.killpg(os.getpgid(pro.pid), signal.SIGTERM)  # Send the signal to all the process groups
    #os.kill(os.getpgid(pro.pid), signal.SIGTERM)  # Send the signal to all the process groups
    pro.send_signal(signal.SIGTERM)
    print(os.getpgid(pro.pid))
    #os.killpg(os.getpgid(pro.pid), signal.SIGINT)  # Send the signal to all the process groups