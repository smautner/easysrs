
import os
import mytime
import json
jdumpfile = lambda thing, filename:  open(filename,'w').write(json.dumps(thing))
jloadfile = lambda filename:  json.loads(open(filename,'r').read())

'''
IDEA IS THIS:
    cards:    hash:{q,a,sort}
    reviews:  hash:{duedate, ease} 
    queue: [hash] # list of hashes of cards to review today ordered by sort field of the cards
   
   
    getq()   # return card.q for the card on top of the queue
    getaq()  # returns card.q and card.a
    answer() # answers the top hash
'''


class cards:
    #############
    # init 
    ###############
    def __init__(self, deckpath, reviewpath):
        self.cards = jloadfile(deckpath)
        self.store = reviewpath

        if os.path.exists(reviewpath):
            self.reviews  = jloadfile(reviewpath)
        else:
            self.reviews={}
        self.buildqueue()



    def queuetoday(self, h): 
        if h not in self.reviews: 
            self.reviews[h] = {"duedate":"0","ease":0}
            return True
        else:
            return self.reviews[h]['duedate'] < mytime.now()

    def buildqueue(self): 
        self.q = [ k for k in self.cards.keys() if self.queuetoday(k) ]
        self.q.sort(key= lambda x: self.cards[x]['sort'],reverse = True)


    #############
    # daily biz
    ################
    def save(self):
        jdumpfile(self.reviews,self.store)

    def reshedule(self,card):
            ease  =  self.reviews[card]['ease']
            self.reviews[card]['duedate'] = mytime.indays(ease_to_interval(ease))


    def getq(self):
        if self.q:
            card = self.cards[self.q[-1]]
            return card['q']
        else:
            return "no questions left"

    def getaq(self):
        card = self.cards[self.q[-1]]
        return card['q']+'\n\n'+card['a']+"\n\n 1-noknow, 2-wonky, 3-success"


    def answer(self, a):
        # -> False, interval dec, interval inc

        h = self.q[-1] # hash of current card

        if a == 1:  # we didnt know the answer
            self.q.insert(0, self.q.pop()) 
            self.reviews[h]['ease'] = 0
            
        elif a == 2:  # we got it barely right
            self.q.pop() # remove from queue today
            # change ease  and dueday 
            if self.reviews[h]['ease'] > 1:
                self.reviews[h]['ease'] -=1
            self.reshedule(h)

        elif a == 3:  # great success
            self.q.pop() # remove from queue today
            # change ease  and dueday 
            self.reviews[h]['ease']+=1
            self.reshedule(h)
        else:
            print ('eeeeh')
        self.save()
            




# ease tetermines the interbal length:
def ease_to_interval(ease): 
    if ease == 0: 
        return 1 
    if ease == 1: 
        return 1
    if ease == 2:
        return 3
    if ease == 2:
        return 7
    return ease_to_interval(ease-1)+ease_to_interval(ease-2)

