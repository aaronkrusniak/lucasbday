'''
A class that allows text to be printed on the screen in an old-school game format (with sound!).
'''

import subprocess, time
import thread, sys, multiprocessing
from Playsound import Playsound

CRAZY = 0.001 #For super-fast text
DEAD = 0.2 #For super-slow text
DEFAULT = 0.03

class Printer(object):
        
    
    def __playblip():
        s = 'Resources/textblip.wav'
        return_code = subprocess.call(["afplay", s])

    @staticmethod
    def out(text, speed = 'DEFAULT', flag = True):
        if speed is 'CRAZY':
            delay = CRAZY
        elif speed is 'DEAD':
            delay = DEAD
        else:
            delay=DEFAULT
        
        miniflag = True
        for c in text:
            sys.stdout.write(c)
            sys.stdout.flush()
            if c != ' ' and flag and miniflag:
                s = Playsound('text')
                #thread.start_new_thread(playblip,())
            if miniflag:
                miniflag = False
            else:
                miniflag = True
            time.sleep(delay)
        print