'''
An class to define the procedures, goals, and rewards of each quest.

TO-DO: Implement Quest & reward sounds!
'''
from gamedev import Playsound, Printer


class Questline(object):
    
    def __init__(self, name, proctext, flavtext, goal='goal', rewards={}, buffs={}):
        self.name = name            #Name of quest
        self.proctext = proctext    #Begin text
        self.flavtext = flavtext    #Win text
        self.goal = goal            #Win condition
        self.rewards = rewards      #Item rewards (a dictionary of form reward: amount)
        self.buffs = buffs          #STATS increases (a dictionary of form STAT: amount)
        self.complete = False
        self.on = False
        
    def beginquest(self):
        p = Playsound('lifequest')
        print '****************************************\nNEW QUEST: ' + self.name + '\n' + self.proctext + '\n****************************************\n'
        self.on = True
        
    def checkon(self):
        return self.on
        
    def checkcomplete(self):
        return self.complete
    
    def printbuffs(self):
        p = Playsound('levelup')
        for buff in self.buffs:
            if self.buffs[buff] > 0:
                direction = 'up'
            else:
                direction = 'down'
            Printer.out('Your ' + buff + ' has gone ' + direction + ' by %d!' % self.buffs[buff])
            
    def printrewards(self):
        p = Playsound('get')
        for reward in self.rewards:
            amount = str(self.rewards[reward])
            Printer.out('You received ' + amount + ' ' + reward + ' to boot!')
        
    def checkgoal(self, attempt):
        if attempt == self.goal:
            self.complete = True
            return True
        else:
            return False
    
    def reward(self):
        p = Playsound('lifequest')
        print('****************************************\nQUEST COMPLETE: ' + self.name + '\n' + self.flavtext + '\n')
        if self.buffs != {}:
            self.printbuffs()
        if self.rewards != []:
            self.printrewards()
        print('****************************************\n')
        on = False
    
    def getrewards(self):
        return self.rewards
    
    def getbuffs(self):
        return self.buffs
    