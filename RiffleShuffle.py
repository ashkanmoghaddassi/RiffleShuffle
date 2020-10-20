#Ashkan Moghadddassi
#Riffle Shuffle Simulation

import random
import numpy as np
from scipy.special import comb


def top_to_random(l):
    copylist = l.copy()
    card = copylist[0]
    copylist.remove(copylist[0])
    new_loc = random.randint(0,len(copylist))
    copylist.insert(new_loc,card)
    return copylist

def gsr(l):
    def choose_card(left, right):
        """Returns 0 if drawing from the left deck, 1 if right."""
        l_prob = len(left) / (len(left) + len(right))
        return np.random.choice([0,1], p=[l_prob, 1-l_prob])

    # choose how many will be in left and right
    n = len(l)
    probs = [comb(n, k) for k in range(n + 1)]
    probs = 1 / 2 ** n * np.array(probs)
    k = np.random.choice(range(n + 1), p = probs)
    # split the deck into left and right
    left = l[:k]
    right = l[k:]
    # create the new deck adding 1 card at a time
    res = []
    while left or right:
        # choose a side of the deck to draw from
        side = choose_card(left, right)
        if side == 0:
            # draw from left side
            res.append(left[len(left) - 1])
            left = left[:len(left) - 1] # remove top card
        else:
            res.append(right[len(right) - 1])
            right = right[:len(right) - 1]
    return res


def gsr_old(l):
    tosses = 0
    copylist = l.copy()
    new_l=[]
    RS=[]
    LS=[]
    flips=[]
    while tosses<len(copylist):
        #get list of heads and tails
        coin = random.randint(0,1)
        flips.append(coin)
        ''' if coin==1:
            RS.append(copylist[tosses])
        elif coin==0:
            LS.append(copylist[tosses])'''
        tosses+=1
    
    for i in range(len(flips)):
    #add into RS if 1 and LS if 0
        if flips[i] == 1:
            RS.append(copylist[tosses])
            #new_l.append(RS.pop(random.randint(0,len(RS)-1)))
        elif flips[i] == 0:
            LS.append(copylist[tosses])
            #new_l.append(LS.pop(random.randint(0,len(LS)-1)))
    return new_l

def test_order(i,j,l):
    if l.index(i) < l.index(j):
        return 1
    else:
        return 0
def MonteCarlogsr(l,i,j,k,lim = 20000):

    trials = 0
    total = 0

    while trials < lim:
        copylist = l.copy()
        for n in range(k):
            copylist = gsr(copylist)
        result = test_order(i,j,copylist)
        total += result
        trials += 1
    return total/trials

def MonteCarlottr(l,i,j,k,lim = 500000):
    trials = 0
    total = 0
    while trials < lim:
        copy = l.copy()
        for n in range(k):
            copy = top_to_random(copy)
        result = test_order(i,j,copy)
        total += result
        trials += 1
    return total/trials
    

def main():
    l = []
    create_deck = int(input('How many cards in the deck? '))
    for i in range(create_deck):
        l.append(i)
    k = int(input('How many shuffles: '))
    i = int(input('first card: '))
    j = int(input('second card: '))
    style = input('How would you like to shuffle?: ')

    if style == 'ttr':
        probability = MonteCarlottr(l,i,j,k)
    elif style == 'gsr':
        probability = MonteCarlogsr(l,i,j,k)
    else:
        print('invalid argument')
    
    
    

    print('The probability is: ',probability)
    

while(True):
    main()



    
        
        
    

    

    
    
    

    
            
        
    
    
        
        
        





    


