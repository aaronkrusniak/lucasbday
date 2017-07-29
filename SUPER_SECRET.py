# -*- coding: utf-8 -*-
'''
Don't look here.  You'll regret it later.
TO-DO:  Build library of quests and decide upon initial inventory
        Re-do the save system, yet again.
        Implement individual condition checking for each quest (it has to be done)
        Implement the battle system
        Write the rest of the quests
        Testing and bugfixes
'''

#import Python libraries:
import unittest, time, re, sys, pickle, os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from gamedev import *

caps = DesiredCapabilities.FIREFOX
caps["marionette"] = True
caps["binary"] = "/Applications/FirefoxDeveloperEdition.app/Contents/MacOS/firefox-bin"


#name, proctext, flavtext, goal, rewards, buffs
ZERO=Questline('DONUTS OF LIFE', 'Find some Revival-Enhanced Donuts!', 'Who knew donuts grew on trees?', 'CONFECTION', {'Revival-Enhanced Donut': 3}, {'LIFE': 3})
ONE = Questline('A DREADFUL HUNT', 'Look for Raggedy Evelyn, the Dreaded by the library!', 'Oh, THERE she is!', 'EVE', {}, {'FINDING ABILITY': 5})
TWO = Questline('RAGGEDY CHAT', 'Talk to Evelyn!', 'She\'s actually not as bad as she smells.', 'STINKY', {}, {'OUTGOINGNESS': 2, 'NASAL HEALTH': -4})
THREE = Questline('LET THERE BE LIGHT', 'Find the Flashlight you left in your room!', 'Now shine it on your face and say a ghost story!', 'BRIGHT', {'FLASHLIGHT':1}, {'FEAR OF DARK': -10})
FOUR = Questline('FRIGHTFUL FOOTBALL', 'Head toward the stadium.', 'If it\'s the HAPPYest game, why is this guy so sad?', 'HAILMARY', {}, {'GLUMNESS': 1})
FIVE = Questline('HAPPY HAPPY HAPPY', 'Order one HAPPY meal, with extra HAPPY!', 'Oh, HAPPY day! ...It smells nice, too.', 'DONALD', {}, {'HAPPYness': 4})
SIX = Questline('DESIGNER EMOJIS', 'Help design the world\'s next salsa girl or smiling poop!', 'My favorite is the jazz hands one.', 'SMILE', {}, {'CREATIVITY': 6})
SEVEN = Questline('THE STOIC SECRETARY', 'Find the Receptionist of Expressionless Disdain!', 'Wow, he\'s so... disdainful!', 'PAM', {}, {'FINDING ABILITY': 5})
EIGHT = Questline('PENULTIMATE PUZZLE', 'Get to ACAC and find the puzzle there!', 'Does it come with hints?', 'JIGSAW', {}, {})
NINE = Questline('FINAL PUZZLE', 'Solve the puzzle and use the completed image as the CODE.', 'I jigsee your jigsaw.', 'TREX', {}, {'PUZZLE-SOLVING ABILITY': 3, 'FOOLISHNESS?': 28})
TEN = Questline('SAVE GRACIE!', 'Run down there and stop RED from taking over her mind!', 'Pumpkins and penguins!', 'ERROR', {}, {})
#a list of all available quests in the game
questlog = [ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN] 
    
#LEGACY CODE FOR ORIGINAL "MONDAY TUTORIAL" RUN
'''
def intro(startkey, endkey):
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
            LEV = 2
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
            
            
'''

def initialize():

    section = Reader.read('000','001')
    for line in section:
        if section.index(line) == 0 or line.find('. . . . .') > -1:
            Printer.out(line,'DEFAULT',False)
        else:
            Printer.out(line, 'CRAZY', False)
            
    section = Reader.read('TITLE', 'ENDINTRO')
    titlemusic = Playsound('title')
    time.sleep(1)
    for line in section:
        print line
    print
    
    Printer.out('The game has been updated since you last played! Here are the patch notes:')
    section = Reader.read('PATCHNOTES', 'ENDPATCH')
    for line in section:
        print line
    print
    
    Printer.out('It looks like you\'ve been here before, kid. How about we continue from where you Recently Ended your Diversions?\n')
    Printer.out('<press ENTER to continue game>')
    raw_input()
    titlemusic.endsound()
    select = Playsound('levelup')
    os.system('clear')
    time.sleep(3)
    
def questcode(character):
    Printer.out('You have a quest code?  Huh.  Let\'s hear it:\n')
    x = raw_input()
    didcomplete = False
    for quest in questlog:
        if quest.checkgoal(x):
            Printer.out('Oh, I guess you got it.\n')
            quest.reward()
            character.changestats(quest.getbuffs())
            for reward in quest.getrewards():
                if reward != 'Revival-Enhanced Donut':
                    character.additem(reward)
                else:
                    character.LIFE += 3
            didcomplete = True
            break
    if not didcomplete:
        Printer.out('That code doesn\'t seem to work here. What\'s taking you so long?\n')
            
            
def inreader(x, curline, character):
    if x == 'STATS':
        character.displaySTATS()
    elif x == 'RED':
        character.savegame(curline)
    elif x == 'CODE':
        questcode(character)
    elif x == 'INVENTORY':
        print 'Here\'s what\'s in your inventory right now:'
        print character.inventory
        Printer.out('Now. . . where were we? Ah, yes.\n')
    elif x == 'EAT':
        Printer.out('What\'s that?  You want to eat one of your Revival-Enhanced Donuts?\n')
        Printer.out('Well, that means you\'ll have one less LIFE. You sure you want to go through with it?  Type YES or NO, then hit ENTER to decide.')
        x = raw_input()
        if x == 'YES':
            character.LIFE -= 1
            Printer.out('Alright, you ate one Revival-Enhanced Donut! You don\'t feel as hungry- but you lost an extra LIFE.')
            Printer.out('Now. . . where were we? Ah, yes.\n')
            if character.LIFE is 0:
                character.gameover()
        elif x == 'NO':
            Printer.out('I\'m glad you\'re playing it safe. With your level of incompetency, you\'re bound to need that extra LIFE sometime sooner or later.')
            Printer.out('Now. . . where were we? Ah, yes.\n')
        else:
            Printer.out('I would appreciate it if you refrained from using your regular barbarian vernacular in the future, thank you. But I\'ll take it that you don\'t want a donut, for now.')
            Printer.out('Now. . . where were we? Ah, yes.\n')
    elif x != '':
        Printer.out('Did you hear something? . . .Must\'ve just been the wind. Huh.\n')
        

def maingame(character):
    
    if character.RED != "REVIEW":
        print character.RED
    
    section = Reader.read(character.RED, 'ZENDING')
    for line in section:
        if line.find('. . .**') > -1:
            Printer.out('. . .', 'DEAD')
            x = raw_input()
            inreader(x, line, character)
        elif line.find('MUSIC_OBSERVATORY') > -1:
            music = Playsound('observatory')
        elif line.find('ITEMGET_KNIFE') > -1:
            p = Playsound('get')
            character.additem('KNIFE')
        elif line.find('You put it in your') > -1:
            print line
            x = raw_input()
            inreader(x, line, character)
        elif line.find('END_OBSERVATORY') > -1:
            music.endsound() 
        elif line.find('QUEST0') > -1:
            ZERO.beginquest()
        elif line.find('QUEST1') > -1:
            ONE.beginquest()
        elif line.find('QUEST_COND0') > -1:
            while not ZERO.checkcomplete():
                Printer.out('What\'s up? Found a quest code?')
                x = raw_input()
                inreader(x, line, character)
        elif line.find('QUEST_COND1') > -1:
            while not ONE.checkcomplete():
                Printer.out('What\'s up? Found a quest code?')
                x = raw_input()
                inreader(x, line, character)
        elif line.find('. . .**') > -1:
            Printer.out('. . .', 'DEAD')
            x = raw_input()
            inreader(x, line, character)
        elif line.find('MUSIC_BATTLE') > -1:
            music = Playsound('battle')
        elif line.find('BATTLE1') > -1:
            #character, enemy, buffs={}, loot={}, theme='battle'
            Eve = Enemy('Evelyn')
            evebattle = Battle(character, Eve, {'LEV':1, 'POW':1, 'FRIENDS':1}, {}, 'battle')
        elif line.find('MUSIC_LEARN') >-1:
            music = Playsound('learn')
        elif line.find('ENDLEARN') >-1:
            music.endsound()
        elif line.find('QUEST+COND2') >-1:
            evebattle.celebmusic.endsound()
            TWO.beginquest()
            while not TWO.checkcomplete():
                Printer.out('What\'s up? Found a quest code?')
                x = raw_input()
                inreader(x, line, character)
        elif line.find('QUEST+COND3') >-1:
            THREE.beginquest()
            while not THREE.checkcomplete():
                Printer.out('What\'s up? Found a quest code?')
                x = raw_input()
                inreader(x, line, character)
        elif line.find('QUEST+COND5') >-1:
            FIVE.beginquest()
            while not FIVE.checkcomplete():
                Printer.out('What\'s up? Found a quest code?')
                x = raw_input()
                inreader(x, line, character)
            music.endsound()
        elif line.find('QUEST+COND6') >-1:
            SIX.beginquest()
            while not SIX.checkcomplete():
                Printer.out('What\'s up? Found a quest code?')
                x = raw_input()
                inreader(x, line, character)
            character.moveset.append('HAPPY')
        elif line.find('QUEST+COND8') >-1:
            EIGHT.beginquest()
            while not EIGHT.checkcomplete():
                Printer.out('What\'s up? Found a quest code?')
                x = raw_input()
                inreader(x, line, character)
        elif line.find('QUEST+COND9') >-1:
            NINE.beginquest()
            time.sleep(2)
            music = Playsound('puzzle')
            while not NINE.checkcomplete():
                Printer.out('What\'s up? Found a quest code?')
                x = raw_input()
                inreader(x, line, character)
        elif line.find('QUEST4') > -1:
            FOUR.beginquest()
        elif line.find('QUEST_COND4') > -1:
            while not FOUR.checkcomplete():
                Printer.out('What\'s up? Found a quest code?')
                x = raw_input()
                inreader(x, line, character)
            music = Playsound('sans')
        elif line.find('QUEST7') > -1:
            SEVEN.beginquest()
        elif line.find('QUEST_COND7') >-1:
            while not SEVEN.checkcomplete():
                Printer.out('What\'s up? Found a quest code?')
                x = raw_input()
                inreader(x, line, character)
        elif line.find('QUESTX') > -1:
            TEN.beginquest()
        elif line.find('BATTLE2') > -1:
            Pam = Enemy('Pam')
            pambattle = Battle(character, Pam, {'LEV':1, 'POW':1, 'FRIENDS':1}, {}, 'battle2')
        elif line.find('ENDBATTLEMUSIC') > -1:
            pambattle.celebmusic.endsound()
        elif line.find('MUSIC_LAUGHTER') >-1:
            music = Playsound('laugh')
            time.sleep(2)
        elif line.find('MUSIC_SUSPENSE') >-1:
            music = Playsound('suspense')
        elif line.find('MISSINGPERSON') >-1:
            music.endsound()
        elif line.find('MUSIC_CHASE') >-1:
            music = Playsound('chase')
        elif line.find('SILENCE') >-1:
            music.endsound()
        elif line.find('NOTHING!') >-1:
            music.endsound()
            print '\033[91m'
            Printer.out(line)
        elif line.find('TO BE CONTINUED') >-1:
            print '\033[0m'
            Printer.out(line)
            x = raw_input()
            inreader(x, line, character)
        else:
            Printer.out(line)
            x = raw_input()
            inreader(x, line, character)
    
    character.savegame('TO BE CONTINUED')
       
    
def loadgame(save):
    savedata = pickle.load(save)
    #INIT: Lucas = Character(1, 1, 3, 0, ['INSULT', 'IMPROV'], 'REVIEW', [])
    Lucas = Character(savedata[0], savedata[1], savedata[2], savedata[3], savedata[4], savedata[5], [])
                            #0=LEVEL, 1=POW, 2=FRIENDS, 3=LIFE, 4=LEARNEDMOVES, 5=RED(the savecode/line for dialogue), 6=inventory
    return Lucas

def main():
    #global driver
    #driver = webdriver.Chrome() #capabilities = caps
    #driver.get('https://www.google.com/')
    
    save = open('savefile copy init.txt', 'r+')
    Lucas = loadgame(save) #Savesystem should allow for minimal patching between Friday & Saturday, and beyond...
    initialize()
    maingame(Lucas)
    
    
    '''
    if Lucas.RED is not '000':
        maingame(Lucas.RED, 'ZENDING')
    else: #Assumed to be false as of 2/21/17 (Lucas started playing the game), but left for posterity:
        intro('001', 'ENDINTRO')
        biggame('ENDINTRO', 'AENDING')
        maingame('ABEGINNING', 'ZENDING')
    '''
    
    save.close()
    #driver.quit()
	

if __name__ == "__main__":
    main()