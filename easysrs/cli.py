
import sys
deckpath = sys.argv[1]
reviewpath = sys.argv[2]

import cards
MANAGER = cards.cards(deckpath,reviewpath)
import time


import curses
import os
def main(win):
    win.nodelay(True)
    key=""

    STATE = "Q"
    win.clear()                
    win.addstr(MANAGER.getq())

    while 1:          
        time.sleep(.1)
        try:                 
           key = win.getkey()         
           if str(key) =="q" or key==os.linesep:
                break

           if STATE == "Q":
                win.clear()                
                STATE = "A"
                win.addstr(MANAGER.getaq())
                
           if STATE == "A":
               key2=str(key)
               MANAGER.answer(int(key2))
               STATE = "Q"
               win.clear()                
               win.addstr(MANAGER.getq()) 

        except Exception as e:
           # No input   
           #win.addstr("ERRER")
           pass
           

curses.wrapper(main)
