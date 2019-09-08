# Poker hands
# Problem 54
# In the card game poker, a hand consists of five cards and are ranked, 
# from lowest to highest, in the following way:

# High Card: Highest value card.
# One Pair: Two cards of the same value.
# Two Pairs: Two different pairs.
# Three of a Kind: Three cards of the same value.
# Straight: All cards are consecutive values.
# Flush: All cards of the same suit.
# Full House: Three of a kind and a pair.
# Four of a Kind: Four cards of the same value.
# Straight Flush: All cards are consecutive values of same suit.
# Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
# The cards are valued in the order:
# 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

# If two players have the same ranked hands then the rank made up of the highest value wins;
 # for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, 
 # for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); 
 # if the highest cards tie then the next highest cards are compared, and so on.

# Consider the following five hands dealt to two players:

# Hand        Player 1        Player 2        Winner
# 1       5H 5C 6S 7S KD
# Pair of Fives
#     2C 3S 8S 8D TD
# Pair of Eights
#     Player 2
# 2       5D 8C 9S JS AC
# Highest card Ace
#     2C 5C 7D 8S QH
# Highest card Queen
#     Player 1
# 3       2D 9C AS AH AC
# Three Aces
#     3D 6D 7D TD QD
# Flush with Diamonds
#     Player 2
# 4       4D 6S 9H QH QC
# Pair of Queens
# Highest card Nine
#     3D 6D 7H QD QS
# Pair of Queens
# Highest card Seven
#     Player 1
# 5       2H 2D 4C 4D 4S
# Full House
# With Three Fours
#     3C 3D 3S 9S 9D
# Full House
# with Three Threes
#     Player 1
# The file, poker.txt, contains one-thousand random hands dealt to two players. 
# Each line of the file contains ten cards (separated by a single space): 
# the first five are Player 1's cards and the last five are Player 2's cards. 
# You can assume that all hands are valid (no invalid characters or repeated cards), 
# each player's hand is in no specific order, and in each hand there is a clear winner.

# How many hands does Player 1 win?



import time
from termcolor import colored

# problem 54

f = open("i54_poker.txt")

nDict = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}

def checkFlush(hand):
    firstCardSuit = hand[0][1]
    for a in range(1,5):
        if hand[a][1] != firstCardSuit:
            return False
    return True

def sortedHand(hand):
    temp = []
    for a in hand:
        temp.append(nDict[a[0]])
    temp.sort()
    temp.reverse()
    return temp

def checkStraight(sortedHand):
    if sortedHand == [14, 5, 4, 3, 2]:
        return True
    for i in range(1,5):
        if sortedHand[i] != sortedHand[i-1]-1:
            return False
    return True

def checkPairs(sortedHand):
    pairs = []
    for i in sortedHand:
        if sortedHand.count(i) == 2:
            if not i in pairs:
                pairs.append(i)
    return pairs

def checkTrips(sortedHand):
    trips = []
    for i in sortedHand:
        if sortedHand.count(i) == 3:
            if not i in trips:
                trips.append(i)
    return trips

def checkQuads(sortedHand):
    quads = []
    for i in sortedHand:
        if sortedHand.count(i) == 4:
            if not i in quads:
                quads.append(i)
    return quads



def checkRank(hand):
    hSorted = sortedHand(hand)
    isFlush = checkFlush(hand)
    isStraight = checkStraight(hSorted)
    trips = checkTrips(hSorted)
    pairs = checkPairs(hSorted)
    if hSorted == [14, 13, 12, 11, 10] and isFlush:
        return ['Royal Flush', None]
    elif isStraight and isFlush:
        return ['Straight Flush', hSorted[0]]  #wheel straight???
    elif len(checkQuads(hSorted)) == 1:
        return 'Four of a Kind'
    elif len(trips) == 1 and len(pairs) == 1:
        return ['Full House', [trips[0],pairs[0]]]
    elif isFlush:
        return ['Flush', hSorted]
    elif isStraight:
        return ['Straight', hSorted]
    elif len(trips) == 1:
        return ['Three of a Kind', [trips, hSorted]]
    elif len(pairs) == 2:
        return ['Two Pairs', [pairs, hSorted]]
    elif len(pairs) == 1:
        kickers = hSorted[:]
        kickers.remove(pairs[0])
        kickers.remove(pairs[0])
        return ['One Pair', [pairs, kickers]]
    else:
        return ['High Card', hSorted]
    
        
# looks like the only ties are high card and one pair

handValue = {'Royal Flush': 10,
             'Straight Flush': 9,
             'Four of a Kind': 8,
             'Full House': 7,
             'Flush': 6,
             'Straight': 5,
             'Three of a Kind': 4,
             'Two Pairs': 3,
             'One Pair': 2,
             'High Card': 1}





def main_process():
    p1 = 0
    p2 = 0
    ties = 0
    
    for line in f:
        temp = line.replace('\n', '')
        temp2 = temp.split(' ')
        hand1 = temp2[0:5]
        hand2 = temp2[5:]
        h1Rank = checkRank(hand1)[0]
        h2Rank = checkRank(hand2)[0]
        h1Val = handValue[h1Rank]
        h2Val = handValue[h2Rank]
        if h1Val > h2Val:
            p1 += 1
        elif h1Val < h2Val:
            p2 +=1
        elif h1Val == h2Val:
            if checkRank(hand1)[1] > checkRank(hand2)[1]:
                p1 += 1
            elif checkRank(hand1)[1] < checkRank(hand2)[1]:
                p2 += 1
            else:
                ties += 1

    print(p1, p2, ties)
    print("The answer is ", p1)

    # print(colored('mycount=', 'red'), 'results')

if __name__ == "__main__":
    tic = time.clock()
    
    main_process()

    toc = time.clock()
    print("time=",toc - tic)