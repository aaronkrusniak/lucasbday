# -*- coding: utf-8 -*-
'''
Don't look here.  You'll regret it later.
'''
#import Python libraries:
import unittest, time, re, sys

import subprocess
import thread

# Import webdriver from the selenium library
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Latest Selenium only works with Firefox's dev edition or nightly edition.
# Use these lines to hook it up to the developer edition.
caps = DesiredCapabilities.FIREFOX
caps["marionette"] = True
caps["binary"] = "/Applications/FirefoxDeveloperEdition.app/Contents/MacOS/firefox-bin"

NEWGAME = 1
LEVEL = 1
POW = 9
FRIENDS = 4
LIFE = 3

REDCODE = '000'
SAVE = 0


CRAZY = 0.001
DEAD = 0.2

def playblip():
    s = 'textblip.wav'
    return_code = subprocess.call(["afplay", s])

def printer(text, delay=0.025, flag = True):
    miniflag = True
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        if c != ' ' and flag and miniflag:
            thread.start_new_thread(playblip,())
        if miniflag:
            miniflag = False
        else:
            miniflag = True
        time.sleep(delay)
    print

def linehelper(linekey, lineend):
    section = []
    flag = -1
    track = -1
    for line in game:
        track = track + 1
        if line.find(linekey) > -1:
            flag = track
            break
    if flag >= 0:
        curline = game[flag + 1]
        helper = 2
        while curline.find(lineend) == -1 :
            section.append(curline)
            curline = game[flag + helper]
            helper += 1
        return section
    
def initialize(game):
    section = linehelper('000','001')
    for line in section:
        if section.index(line) == 0 or len(section) - section.index(line) == 1:
            printer(line)
        elif len(section) - section.index(line) < 4:
            printer(line, DEAD)
        else:
            printer(line, CRAZY, False)
'''
NEED TO ACTUALLY IMPLEMENT RED SYSTEM
'''
def intro(game, startkey, endkey):
    section = linehelper(startkey, endkey)
    raw_input()
    for line in section:
        if line.find('REDERROR') == -1 and line.find('REDCOMPLETE') == -1:
            if line.find('/') > -1 or line.find('. . .  ') > -1:
                printer(line, DEAD)
            elif line.find('nifty') > -1:
                printer(line)
                x = raw_input()
                while x != 'RED':
                    printer('Uh, I don’t think you quite got it, kid. Wanna try again?')
                    x = raw_input()
            elif (len(section) - section.index(line)) < 5:
                printer(line, CRAZY)
                if line.find('ORIGINS') > -1:
                    driver.get('https://soundcloud.com/maxwei1125/super-mario-galaxy-wind-garden-gusty-garden-galaxy')
            elif line.find('cheating') > -1 or line.find('And I') > -1:
                printer(line)
            elif line.find('kitchy') > -1:
                printer(line)
                driver.get('https://soundcloud.com/bobby-monello/undertale-ost-enemy-approaching-extended')
                raw_input()
            elif line.find('saving') > -1:
                printer(line)
                driver.get('https://www.google.com/')
                raw_input()
            else:
                printer(line)
                raw_input()
                
def displaystats():
    printer('Here are your current stats:')
    print 'LEVEL: %d' % LEVEL
    print 'POW: %d' % POW
    print 'FRIENDS: %d' % FRIENDS
    
def changestats(LV, PW, FR):
    LEVEL = LV
    POW = PW
    FRIENDS = FR
    
def redgame(curline):
    save.seek(0)
    save.truncate()
    save.write(str(NEWGAME) + "\n")
    save.write(str(LEVEL)+ "\n")
    save.write(str(POW)+ "\n")
    save.write(str(FRIENDS)+ "\n")
    save.write(curline)
    
    
def gamecode():
    printer('Alright, let\'s hear that favorite number!')
    x = raw_input()
    if x == '24601':
        return True
    else:
        printer('Sorry, kid. I don\'t recognize that number.')
        return False

def inreader(curline):
    x = raw_input()
    if x == 'STATS':
        displaystats()
        printer('Now, where were we. . . Oh yes.')
    elif x == 'RED':
        redgame(curline)
        printer('You successfully used the move RED! You really encoded that data.')
        printer('Now, where were we. . . Oh yes.')
    elif x == 'CODE':
        printer('Great! What\'s your code?')
        gamecode()
    elif x != '':
        printer('Did you hear something? . . .Must\'ve just been the wind. Huh.')
        
def biggame(startkey, endkey):
    section = linehelper(startkey, endkey)
    raw_input()
    for line in section:
        if line.find('STATS before') > -1:
            printer(line)
            x = raw_input()
            while x != 'STATS':
                printer('Not quite, kid, Try again.')
                x = raw_input()
            displaystats()
        elif line.find('Oh?') > -1:
            driver.get('https://www.google.com/')
            printer(line)
            inreader(line)
        elif line.find('. . .    ') > -1:
            printer(line, DEAD)
            raw_input()
        elif line.find('CODE') > -1:
            printer(line)
            x = raw_input()
            flag = False
            while not flag:
                while x != 'CODE':
                    printer(line)
                    x = raw_input()
                flag = gamecode()
        elif line.find('gone up') > -1:
            LEVEL = 2
            FRIENDS = 5
            printer(line)
            inreader(line)
        elif line.find('QUEST COMPLETE') > -1:
            driver.get('https://soundcloud.com/angrysausage/toby-fox-undertale-6')
            printer(line)
            inreader(line)
        elif line.find('keeps me') > -1:
            printer(line)
            x = raw_input()
            while x != 'RED':
                printer('Nope, not quite. Remember how I showed you earler? Just type RED before pressing ENTER!')
                x = raw_input()
        else:
            printer(line)
            inreader(line)
        
def main():
    global driver
    driver = webdriver.Chrome() #capabilities = caps
    driver.get('https://www.google.com/')
    
    global game 
    game = open('even_secreter.txt').readlines()
    
    global save
    save = open('savestate.txt', 'r+')
    savestate = save.readlines()
    NEWGAME = int(savestate[0])
    LEVEL = int(savestate[1])
    POW = int(savestate[2])
    FRIENDS = int(savestate[3])
    REDCODE = savestate[4]
    
    initialize(game)
    if NEWGAME == 0:
        printer('It looks like you\'ve been here before, kid. Let\'s pick up right where we left off, shall we?')
        biggame(REDCODE, 'AENDING')
    else:
        intro(game, '001', 'ENDINTRO')
        biggame('ENDINTRO', 'AENDING')
    
    driver.quit()
	

if __name__ == "__main__":
    main()