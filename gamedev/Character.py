'''
A class that stores all of the stats information about the player and controls lives.
It also swallows gum and takes names.

TO-DO: Implement PICKLEING for saving/loading game.
'''

import subprocess, multiprocessing, pickle
from Printer import Printer
from Playsound import Playsound

#'BRANDISH'

class Character(object):
    
    def __init__(self, LEV=1, POW=1, FRIENDS=4, LIFE=0, learnedmoves=[], RED='REVIEW', inventory=[]):
        self.LEV = LEV
        self.POW = POW
        self.FRIENDS = FRIENDS
        self.LIFE = LIFE
        self.RED = RED
        self.HP = 30
        self.inventory = inventory
        self.moveset = learnedmoves
        
    def lifechange(self, net):
        if net > 0 :
            self.LIFE += net
            Printer.out('You found ' + net + 'Revival-Enhanced Donuts. You can use them as extra LIFEs!')
        else:
            Printer.out('Uh-oh, looks like you lost a LIFE! Better eat a donut to make you feel better.\n')
            self.LIFE -= 1
            if self.LIFE < 0:
                self.gameover()
            else:
                Printer.out('You have eaten one Revival-Enhanced Donut, and are feeling refreshed!\n')
                Printer.out('You have ' + str(self.LIFE) + ' LIFEs left with your current donut stash.\n')
    
    def gameover(self):
        Printer.out('What\'s the matter?')
        raw_input()
        Printer.out('You ran out of LIFEs?')
        raw_input()
        Printer.out('You ran out of Revival-Enhanced Donuts, too?')
        raw_input()
        Printer.out('And you want to know why you\'re still alive??!')
        raw_input()
        Printer.out('Don\'t you know, kid?  LIFE is just a Little Indulgence For Eating donuts!!!')
        raw_input()
        Printer.out('After all- what\'s more memorable than eating a wonderful, sugary donut? You\'ll always remember those parts of your journey, won\'t you?')
        raw_input()
        Printer.out('Anyway, you\'re not going to die without any LIFEs. Sheesh, what do you take me for, a homicidal computer??')
        raw_input()
        Printer.out('Fine- if it makes you feel any better, here\'s three more donuts, which means three more LIFEs. So you\'re not dead, okay?')
        raw_input()
        Printer.out('. . .', 'DEAD')
        raw_input()
        Printer.out('Yet.')
        raw_input()
        self.LIFE = 3
        
    def displaySTATS(self):
        print ('\nHere are your current STATS:')
        print ('Your current LEV is %d.' % self.LEV)
        print ('Your POW is %d.' % self.POW)
        print ('You have %d FRIENDS.' % self.FRIENDS)
        print ('You have %d LIFEs remaining.' % self.LIFE)
        Printer.out('Now. . . where were we? Ah, yes.\n')
    
    def savegame(self, curline):
        music = Playsound('get')
        save = open('savefile.txt', 'r+')
        data = [self.LEV, self.POW, self.FRIENDS, self.LIFE, self.moveset, curline, self.inventory]
        #0=LEVEL, 1=POW, 2=FRIENDS, 3=LIFE, 4=LEARNEDMOVES, 5=RED(the savecode/line for dialogue), 6=inventory
        pickle.dump(data, save)
        Printer.out('You successfully used the move RED! The game is now saved.')
        Printer.out('Now. . . where were we? Ah, yes.\n')
        
    def changestats(self, questbuffs):
        for STAT in questbuffs:
            if STAT is 'LEV':
                self.LEV += questbuffs[STAT]
            elif STAT is 'POW':
                self.POW += questbuffs[STAT]
            elif STAT is 'FRIENDS':
                self.FRIENDS += questbuffs[STAT]
            elif STAT is 'LIFE':
                self.LIFE += questbuffs[STAT]
        
    def learnmove(self, move):
        if move not in moveset:
            moveset.append(move)
            s = Playsound('get')
            Printer.out('You learned the move ' + move + '!\n')
        else:
            Printer.out('You tried to learn the move ' + move + ', but you already knew it!\n')

    def getstats(self):
        statset = [self.LEV, self.POW, self.FRIENDS, self.LIFE]
        return statset
    
    def getmoves(self):
        return moveset
    
    def additem(self, item):
        self.inventory.append(item)