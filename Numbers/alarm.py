"""
A simple clock where it plays a sound after X number of
minutes/seconds or at a particular time.
"""

import time
import pyglet

def passedTime(t, typetime):
    """
    Returns time passed since t (seconds)
    typetime can be <m> or <s> to specify
    the returning type (minutes or seconds)
    """
    try:
        passed = time.time() - t
    except TypeError:
        "Argument is not a time"

    if typetime == "m":
        # minutes
        return passed / 60.0
    elif typetime == "s":
        # seconds
        return passed
    else:
        print "Type not valid"
        


mario = pyglet.media.load("oneup.wav", streaming=False)

def playSound():
    
    mario.play()

def cronometer(t, typetime):

    start = time.time()

    flag = True # for counter

    while 1:
        
        p = passedTime(start, typetime)

        if flag:
            # get first p
            r = p
            flag = False

        if int(r) != int(p):
            print "Remaining " + str(int(t) - int(p)) + typetime
            r = p

        if t < p:
            print "END of cronometer!"
            break
    
    playSound()
    time.sleep(1)


def alarm(hours, minutes):

    h = int(hours)
    m = int(minutes)

    if not (h in range(24) and m in range(60)):
        print "Wrong time values"
        return


    flag = True
    
    while 1:
        t = time.localtime() # gmtime is UTC
        
        if t.tm_hour == int(h) and t.tm_min == int(m):
            break
            
        if flag:
            # get first p
            past_hr = t.tm_hour
            past_min = t.tm_min
            flag = False

        if past_hr != t.tm_hour or past_min != t.tm_min:
            remaining = ((h - t.tm_hour) * 60) + (m - t.tm_min) # mmm
            print "Remamining minutes: " + str(remaining)
            past_hr = t.tm_hour
            past_min = t.tm_min
        
    playSound()
    time.sleep(1)
    

    

def main():

    inp = raw_input("Cronometer or Alarm? [c/a] ")

    if inp == "C" or inp == "c":

        typetime = raw_input("Minutes or seconds? [s/m] ")
        t = float(raw_input("How many minutes/seconds? "))

        cronometer(t, typetime)

    elif inp == "A" or inp == "a":

        print "When would you like the alarm to go off?"
        hours = raw_input("Hours[0-23]> ")
        minutes = raw_input("Minutes[0-59]> ")
        alarm(hours, minutes)
        


if __name__ == "__main__":

    main()
    
    