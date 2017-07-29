'''
Sound handling for the game.
'''

import subprocess, multiprocessing
sounds = {'get': 'itemget.wav',
          'levelup': 'levelup.wav',
          'lifequest': 'questcomplete.wav',
          'text': 'textblip.mp3',
          'title': 'title.mp3',
          'observatory': 'observatory.mp3',
          'battle': 'battle.mp3',
          'battle2': 'battle2.mp3',
          'celeb': 'celeb.mp3',
          'boss': 'boss.mp3',
          'chase': 'chase.mp3',
          'ghost': 'ghost.mp3',
          'laugh': 'laugh.mp3',
          'learn': 'learn.mp3',
          'puzzle': 'puzzle.mp3',
          'sans': 'sans.mp3',
          'suspense': 'suspense.mp3'}

class Playsound(object):
    
    def __init__(self, situation):
        self.sound = sounds[situation]
        self.p = multiprocessing.Process(target=self.playsound)
        self.p.start()
        
    def playsound(self):
        return_code = subprocess.call(["afplay", self.sound])
        
    def endsound(self):
        return_code = subprocess.call("killall afplay", shell=True)
        self.p.terminate()