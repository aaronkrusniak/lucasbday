'''
An object class for enemies.
'''

from Printer import Printer
import random

evelynreact = {'INSULT': 'Evelyn seems to be taken aback by your stinging wit and loses a little HP!',
                'KNIFE': 'You wave your Reliable Enemy Decapitator in the air and Evelyn looks mildly afraid!'}
evelyndamage = {'INSULT': 0, 
                'KNIFE': -4}
evelynimprov = {'You do an Irish jig to distract Evelyn! She joins in on the fun and seems emboldened!': 4,
                'You let out a mighty roar! Evelyn cowers in fear!': -7,
                'You threaten to report Evelyn to the proper authorities! Evelyn laughs, but begins to look fidgety!': -5}
evelynattack = {'Evelyn uses the move STINKY and disgusts you with her noxious smell!': -3,
                'Evelyn uses the move ROT-PUT and throws a rotting rag at you!': -5,
                'Evelyn uses the move RAGGED BREATH. She takes a deep, calming breath and regains some HP!': 1}


pamreact = {'INSULT': 'The Receptionist gives no reaction to your stinging words!',
            'KNIFE': 'You wave your Reliable Enemy Decapitator in the air but the Receptionist is totally unphased!',
            'HAPPY': 'You betray emotion! The Receptionist gains HP in stoic anger!',
            'FLASHLIGHT': 'You use your flashlight as a strobe while you dance! It\'s somewhat effective!'}
pamdamage = {'INSULT': 0, 
             'KNIFE': 0,
             'FLASHLIGHT': 0,
             'HAPPY' : 10}
pamimprov = {'You do an Irish jig for the Receptionist! He seems to be slightly intimidated!': -3,
             'You do the funky chicken! The Recpetionist seems to be mildly bewildered!!': -4,
             'You do some freestyle dancing! The Receptionist is quite scared of your dancing prowess!': -8,
             'You use your jazz hands on the Receptionist! He is somewhat afraid of them!': -6,
             'You twirl like a ballerina! It almost seems like the Receptionist is emboldened by your ridiculousness!': 2}
pamattack = {'The Receptionist uses the move SPRINKLER and showers you with his mad skillz!': -2,
             'The Receptionist uses the move KICKLINE and lifts his legs to incredible heights!': -4,
             'The Receptionist uses the move FREESTYLE. You are awed by his outrageous grooving abilities!' : -6,
             'The Receptionist uses the move RELAXING TWIRL. He spins around and regains some HP!': 2}

class Enemy(object):
    
    def __init__(self, kind):
        self.kind = kind
        if kind == 'Evelyn':
            self.name = 'Raggedy Evelyn the Dreaded'
            self.HP = 30
        elif kind == 'Pam':
            self.name = 'the Receptionist of Expressionless Disdain'
            self.HP = 30
        
    def react(self, attack):
        critchance = random.randint(0,12)
        if critchance == 10:
            crit = True
        else:
            crit = False
            
        if self.kind == 'Evelyn':
            if attack != 'IMPROV':
                for reaction in evelynreact:
                    if attack == reaction:
                        Printer.out(evelynreact[reaction])
                        raw_input()
                        if attack == 'INSULT':
                            damage = random.randint(-6,-2)
                        else:
                            damage = evelyndamage[reaction]
                        if crit:
                            Printer.out('It\'s a critical hit!!')
                            damage = damage * 2
                        Printer.out('Your attack caused Evelyn to lose ' + str(damage) + ' HP!')
                        self.HP += damage
                        break
            else:
                move = random.choice(evelynimprov.keys())
                Printer.out(move)
                raw_input()
                if move.find('jig') > -1:
                    Printer.out('Your attack caused Evelyn to gain ' + str(evelynimprov[move]) + ' HP!')
                    self.HP += evelynimprov[move]
                else:
                    damage = evelynimprov[move]
                    if crit:
                        Printer.out('It\'s a critical hit!!')
                        damage = damage * 2
                    Printer.out('Your attack caused Evelyn to lose ' + str(damage) + ' HP!')
                    self.HP += damage
        elif self.kind == 'Pam':
            if attack != 'IMPROV' and attack != 'HAPPY':
                for reaction in pamreact:
                    if attack == reaction:
                        Printer.out(pamreact[reaction])
                        raw_input()
                        if attack == 'FLASHLIGHT':
                            damage = random.randint(-6,-2)
                        else:
                            damage = 0
                        if crit and damage != 0:
                            Printer.out('It\'s a critical hit!!')
                            damage = damage * 2
                        Printer.out('Your attack caused the Receptionist to lose ' + str(damage) + ' HP!')
                        self.HP += damage
                        break
            elif attack == 'IMPROV':
                move = random.choice(pamimprov.keys())
                Printer.out(move)
                raw_input()
                if move.find('ballerina') > -1:
                    Printer.out('Your attack caused the Receptionist to gain ' + str(pamimprov[move]) + ' HP!')
                    self.HP += pamimprov[move]
                else:
                    damage = pamimprov[move]
                    if crit:
                        Printer.out('It\'s a critical hit!!')
                        damage = damage * 2
                    Printer.out('Your attack caused the Receptionist to lose ' + str(damage) + ' HP!')
                    self.HP += damage
            else:
                Printer.out(pamreact['HAPPY'])
                raw_input()
                Printer.out('Your attack caused the Receptionist to gain 1 HP!')
                self.HP += 1
                    
    def attack(self):
        critchance = random.randint(0,17)
        if critchance == 10:
            crit = True
        else:
            crit = False
        if self.kind == 'Evelyn':
            move = random.choice(evelynattack.keys())
            damage = evelynattack[move]
        elif self.kind == 'Pam':
            move = random.choice(pamattack.keys())
            damage = pamattack[move]
        Printer.out(move)
        if crit:
            damage = damage * 2
            Printer.out('It\'s a critical hit!!')
        if move.find('RAGGED BREATH') > -1 or move.find('RELAXING TWIRL') >-1:
            Printer.out(self.name + ' recovered ' + str(damage) + ' HP!')
            self.HP += damage
            damage = 0
        return damage
        
        
                    
        
    