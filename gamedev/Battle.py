'''
A class to handle the battle system.
'''

from gamedev import*

class Battle(object):
    
    def __init__(self, character, enemy, buffs={}, loot={}, theme='battle'):
        self.character = character
        self.character.LIFE = 0
        self.enemy = enemy
        self.buffs = buffs
        self.loot = loot
        self.theme = theme
        self.celebmusic = self.battledriver()
        
    def battledriver(self):
        battlemusic = Playsound(self.theme)
        print '****************************************'
        Printer.out('A wild ' + self.enemy.name + ' has appeared! You enter into battle!\n')
        while self.enemy.HP > 0:
            while self.character.HP > 0 and self.enemy.HP > 0:
                print 'You (' + str(self.character.HP) + 'HP) versus ' + self.enemy.name + ' (' + str(self.enemy.HP) + 'HP)' 
                valmove = False
                while not valmove:
                    print 'What will you do?'
                    print 'Use ' + str(self.character.moveset) + ' or ITEM'
                    x = raw_input()
                    if x == 'STATS' or x == 'RED' or x == 'CODE' or x == 'INVENTORY':
                        print 'You can\'t use that command while in BATTLE!\n'
                    else:
                        for move in self.character.moveset:
                            if x == move:
                                self.usemoveitem('character', move)
                                valmove = True
                                break
                        if not valmove:
                            if x == 'ITEM':
                                print 'What item do you wish to use? Type BACK to go back to your moves.'
                                print self.character.inventory
                                x = raw_input()
                                for item in self.character.inventory:
                                    if x == item:
                                        self.usemoveitem('character', item)
                                        valmove = True
                                        break
                                if not valmove:
                                    if x == 'Revival-Enhanced Donut':
                                        print 'You can\'t use that item in battle!'
                                    elif x != 'BACK':
                                        print 'Looks like you\'re fresh out of ' + x + '.\n'
                            else:
                                print 'I\'m not sure that ' + str(x) + ' is a good idea in this situation.\n'
                valmove = False
                if self.enemy.HP > 0:
                    self.usemoveitem() #by default, selects a random enemy move
            
            #ASSUMPTION: either player or enemy health is below 0.
            if self.character.HP <= 0: #Player died, use an extra life and restart while loop.
                self.character.lifechange(-1)
                self.character.HP = 30
        #Enemy died, break out of the while.
        
        battlemusic.endsound()
        celebmusic = Playsound('celeb')
        Printer.out('You have bested ' + self.enemy.name + '!\n')
        self.character.HP = 30
        if self.buffs != {}:
            self.character.changestats(self.buffs)
            p = Playsound('levelup')
            for buff in self.buffs:
                if self.buffs[buff] > 0:
                    direction = 'up'
                else:
                    direction = 'down'
                Printer.out('Your ' + buff + ' has gone ' + direction + ' by %d!' % self.buffs[buff])
        if self.loot != {}:
            p = Playsound('get')
            for reward in self.loot:
                #self.character.inventory[reward] = self.loot[reward] TAKE CARE OF THIS AFTER BATTLE!
                #amount = str(self.rewards[reward])
                Printer.out('You received ' + str(self.loot[reward]) + ' ' + reward + ' to boot!')
        print '****************************************'
        raw_input()
        return celebmusic
    
    def usemoveitem(self, side='enemy', attack='ERROR'):
        if side == 'character':
            Printer.out('You used your ' + attack + ' against ' + self.enemy.name + '!')
            raw_input()
            self.enemy.react(attack)
            raw_input()
        else:
            damage = self.enemy.attack()
            self.character.HP += damage
            raw_input()
            Printer.out('You lost ' + str(damage * -1) + ' HP from the attack!')
            raw_input()
                        