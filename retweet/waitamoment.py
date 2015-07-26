'''Wait a moment before going on'''
import time
from random import randint

class WaitAMoment:
    '''Wait a moment before going on'''
    def __init__(self):
        '''Constructor of the WaitAMoment class'''
        waitsec = randint(60,600)
        time.sleep(waitsec)
