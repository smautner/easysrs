
import cards
import sys
import time
from getch import getch, pause
import os


#########
# card manager 
##########
deckpath = sys.argv[1]
reviewpath = sys.argv[2]
MANAGER = cards.cards(deckpath,reviewpath)


# manager hjas getaq answer(int) and getq()

##############
# MAINLOOP
#############


stop=False
while not stop: 
    print(MANAGER.getq())
    pause()
    print(MANAGER.getaq())
    ch = getch()
    if ch == 'q':
        break
    MANAGER.answer(int(ch))



