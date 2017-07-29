import pygame, time
from pygame.locals import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((0,0), pygame.RESIZABLE, 0)
    pygame.display.flip()
    pygame.display.set_caption("RED Origins - Lucas Reborn")
    clock = pygame.time.Clock()
    # raise the USEREVENT every 1000ms
    pygame.time.set_timer(pygame.USEREVENT, 80)
    
    myfont = pygame.font.Font("assets/Cutive_Mono/CutiveMono-Regular.ttf", 35) #
    # render text
    label = myfont.render("Some text!", 1, (255,255,255))
    screen.blit(label, (2, 2)) 
    
    text = 'Here is my message: RED Alert'
    message = DynamicText(myfont, text, 20, 500, autoreset=False)
    while message.done == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: break
            if event.type == pygame.USEREVENT: 
                print pygame.event.event_name
                message.update()
        else:
            print "I'm taking it THERE"
            screen.fill(pygame.color.Color('black'))
            message.draw(screen)
            pygame.display.flip()
            clock.tick(60)
            continue
        break
    
                 
def text_generator(text):
    tmp = ''
    for letter in text:
        tmp += letter
        # don't pause for spaces
        if letter != ' ':
            yield tmp

# a simple class that uses the generator
# and can tell if it is done
class DynamicText(object):
    def __init__(self, font, text, xpos, ypos, autoreset=False):
        self.done = False
        self.font = font
        self.text = text
        self._gen = text_generator(self.text)
        self.xpos = xpos
        self.ypos = ypos
        self.autoreset = autoreset
        self.update()

    def reset(self):
        self._gen = text_generator(self.text)
        self.done = False
        self.update()

    def update(self):
        if not self.done:
            try: self.rendered = self.font.render(next(self._gen), True, (255, 255, 255))
            except StopIteration: 
                self.done = True
                if self.autoreset: self.reset()

    def draw(self, screen):
        screen.blit(self.rendered, (self.xpos, self.ypos))

            

    
    
if __name__ == "__main__":
    main()