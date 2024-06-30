import os
import mytime
import json

import re

'''
IDEA IS THIS:
    like cards, but we just want to review contents of one of my obsidian notes
'''

def markdown_to_cards(path):

    text= open(path,'r').read()
    pattern = r"##(.*)([^#]*)"
    matches = re.finditer(pattern, text)

    q_a = []
    for match in matches:
        # Print the content of the first two groups
        if match.groups():
            q_a.append({'q': match.group(1), 'a':match.group(2)}

    return q_a



class cards:
    #############
    # init
    ###############
    def __init__(self, markdownpath):

        self.cards = markdown_to_cards(markdownpath)



    #############
    # daily biz
    ################

    def getq(self):
        if self.q:
            card = self.cards[0]
            return card['q']+"\n\n"
        else:
            return "no questions left"

    def getaq(self):
        card = self.cards[0]
        return card['q']+'\n\n'+card['a']+"\n\n 1-SoonAgain, 2-mvToEnd, 3-rm\n"


    def answer(self, a):
        # -> False, interval dec, interval inc

        if a == 1:  # we didnt know the answer
            self.cards[6:6] = [self.cards[0]]
            del self.cards[0]

        elif a == 2:  # we got it barely right  -> push to the end
            self.cards.append(self.cards[0])
            del self.cards[0]

        elif a == 3:  # correct
            del self.cards[0]
        else:
            print ('eeeeh')

