import RPi.GPIO as GPIO
import time
import threading
import signal
import subprocess
import os

GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(16, GPIO.OUT)


global pro
 
class Job(threading.Thread):
 
    def __init__(self):
        threading.Thread.__init__(self)
 
        # The shutdown_flag is a threading.Event object that
        # indicates whether the thread should be terminated.
        self.shutdown_flag = threading.Event()
 
        # ... Other thread setup code here ...
 
    def run(self):
        global pro
        print('Thread #%s started' % self.ident)
        pro = subprocess.Popen('rosrun velodyne_driver vdump capture- enp0s31f6', shell=True)
 
        while not self.shutdown_flag.is_set():
            # ... Job code here ...
            time.sleep(0.5)
 
        # ... Clean shutdown code here ...
        print('Thread #%s stopped' % self.ident)
 
 
class ServiceExit(Exception):
    """
    Custom exception which is used to trigger the clean exit
    of all running threads and the main program.
    """
    pass
 
 
def service_shutdown(signum, frame):
    print('Caught signal %d' % signum)
    raise ServiceExit
 
def service_shutdown_1():
    global pro
    #print('Caught signal %d' % signum)
    os.killpg(os.getpgid(pro.pid), signal.SIGINT)
    raise ServiceExit

def main():
 
    # Register the signal handlers
    signal.signal(signal.SIGTERM, service_shutdown)
    signal.signal(signal.SIGINT, service_shutdown)
 
    print('Starting main program')
 
    # Start the job threads
    try:
        j1 = Job()
        j1.start()
 
        # Keep the main thread running, otherwise signals are ignored.
        while True:
            #time.sleep(0.5)
            #temp = input()
            #if temp == 1:
              #service_shutdown_1()
            if GPIO.input(10) == GPIO.LOW:
                GPIO.output(16,0)
                service_shutdown_1()
 
    except ServiceExit:
        # Terminate the running threads.
        # Set the shutdown flag on each thread to trigger a clean shutdown of each thread.
        j1.shutdown_flag.set()
        # Wait for the threads to close...
        j1.join()
 
    print('Exiting capture program')
 
 
if __name__ == '__main__':
    while True:
      #temp = input()
      #if temp == 1:
          #main()
      if GPIO.input(10) == GPIO.HIGH:
          GPIO.output(16,1)
          main()