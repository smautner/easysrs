
import cards
import sys
import time
import curses
import os


#########
# card manager 
##########
deckpath = sys.argv[1]
reviewpath = sys.argv[2]
MANAGER = cards.cards(deckpath,reviewpath)


##############
#  main loop
###############

def main(win):
    win.nodelay(True)
    key=""
    STATE = "showQuestion"
    win.clear()                
    win.addstr(MANAGER.getq())

    while 1:          
        time.sleep(.1)
        try:                 
           key = win.getkey()         
           if str(key) =="q" or key==os.linesep:
                break
           

           if STATE == "showQuestion":
                win.clear()                
                STATE = "showAnswer"
                win.addstr(MANAGER.getaq())

           if STATE == "showAnswer":
               key2=str(key)
               MANAGER.answer(int(key2))
               STATE = "showQuestion"
               win.clear()                
               win.addstr(MANAGER.getq()) 

        except Exception as e:
           pass
           

curses.wrapper(main)
