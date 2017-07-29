'''
This class is for an object that will translate lines of dialogue in the game, and also some Spanish.

Possibly needs to have a getnext method??
'''

game = open('even_secreter.txt').readlines()

class Reader(object):
        
    '''
    This method reads lines of script into an array, so that they may be printed one by one.
    The linekey is a unique keyword or number in the script that partitions different sections,
    e.g., the key '000' is the key that signals the very beginning of the game script.
    Lineend is another keyword (e.g., AENDING) that signlas the end of the section.
    
    Useful for breaking up the game into maneagable sections of story and quest which may behave
    slightly differently from each other.
    '''
    @staticmethod
    def read(linekey, lineend):
        section = []
        track = -1 #used to track the line number
        flag = -1  #gets saved as the current line number if key is found

        for line in game: #basic search to find the key (starting point for a section of dialogue)
            track += 1
            if line.find(linekey) > -1:
                flag = track
                break
        
        if flag >= 0: #i.e., key was found:
            flag += 1 #start fetching lines of dialogue starting with line directly after the key
            curline = game[flag] 
            while curline.find(lineend) == -1 :
                section.append(curline)
                flag += 1
                curline = game[flag]
            return section