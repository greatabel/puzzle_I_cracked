'''
A player starts on the GO square and adds the scores on two 6-sided dice to determine 
the number of squares they advance in a clockwise direction. Without any further rules 
we would expect to visit each square with equal probability: 2.5%. However, landing on 
G2J (Go To Jail), CC (community chest), and CH (chance) changes this distribution.

In addition to G2J, and one card from each of CC and CH, that orders the player to go 
directly to jail, if a player rolls three consecutive doubles, they do not advance the
 result of their 3rd roll. Instead they proceed directly to jail.

At the beginning of the game, the CC and CH cards are shuffled. When a player lands on
 CC or CH they take a card from the top of the respective pile and, after following 
 the instructions, it is returned to the bottom of the pile. There are sixteen cards 
 in each pile, but for the purpose of this problem we are only concerned with cards 
 that order a movement; any instruction not concerned with movement will be ignored 
 and the player will remain on the CC/CH square.

Community Chest (2/16 cards):
Advance to GO
Go to JAIL
Chance (10/16 cards):
Advance to GO
Go to JAIL
Go to C1
Go to E3
Go to H2
Go to R1
Go to next R (railway company)
Go to next R
Go to next U (utility company)
Go back 3 squares.
The heart of this problem concerns the likelihood of visiting a particular square. 
That is, the probability of finishing at that square after a roll. For this reason 
it should be clear that, with the exception of G2J for which the probability of finishing 
on it is zero, the CH squares will have the lowest probabilities, as 5/8 request a movement 
to another square, and it is the final square that the player finishes at on each roll that 
we are interested in. We shall make no distinction between "Just Visiting" and being sent to JAIL,
 and we shall also ignore the rule about requiring a double to "get out of jail", assuming 
 that they pay to get out on their next turn.

By starting at GO and numbering the squares sequentially from 00 to 39 
we can concatenate these two-digit numbers to produce strings that correspond with sets of squares.

Statistically it can be shown that the three most popular squares, in order, are JAIL (6.24%) = Square 10,
 E3 (3.18%) = Square 24, and GO (3.09%) = Square 00. So these three most popular squares can be listed with
  the six-digit modal string: 102400.

If, instead of using two 6-sided dice, two 4-sided dice are used, find the six-digit modal string.
'''

import time
from termcolor import colored

import random

random.seed(0)

########


squares = [
  "GO",  "A1", "CC1",  "A2",  "T1",  "R1",  "B1", "CH1",  "B2",  "B3",
"JAIL",  "C1",  "U1",  "C2",  "C3",  "R2",  "D1", "CC2",  "D2",  "D3",
  "FP",  "E1", "CH2",  "E2",  "E3",  "R3",  "F1",  "F2",  "U2",  "F3",
 "G2J",  "G1",  "G2", "CC3",  "G3",  "R4", "CH3",  "H1",  "T2",  "H2"
]


NUM_SQUARES = len(squares)
NUM_DIE_SIDES = 4
DEBUG = False


########


def die():
  return random.randrange(1, NUM_DIE_SIDES + 1)

def dice():
  return die(), die()


########


def s_to_i(square):
  return squares.index(square)

def i_to_s(i):
  return squares[i]


########

def ident(current_square):
  return current_square

def nextR(current_square):
  i = s_to_i(current_square)
  while squares[i][0] != "R":
    i = (i + 1) % NUM_SQUARES
  return i_to_s(i)

def nextU(current_square):
  i = s_to_i(current_square)
  while squares[i][0] != "U":
    i = (i + 1) % NUM_SQUARES
  return i_to_s(i)

def back3(current_square):
  i = s_to_i(current_square)
  # Python actually has sensible sign semantics for modulus,
  # but enough languages have made the wrong choice, so I'm always paranoid.
  return i_to_s((i + NUM_SQUARES - 3) % NUM_SQUARES)

CC_cards = [
  ident, ident, ident, ident,
  ident, ident, ident, ident,
  ident, ident, ident, ident,
  ident, ident,
  "GO",
  "JAIL"
]

CH_cards = [
  ident, ident, ident, ident,
  ident, ident,
  "GO",
  "JAIL",
  "C1",
  "E3",
  "H2",
  "R1",
  nextR,
  nextR,
  nextU,
  back3
]

########


def simulation(num_games, num_turns, turns_to_burn):

  frequencies = {}
  for square in squares:
    frequencies[square] = 0

  for sim in range(num_games):

    current_square = "GO"

    # Copying lists: it's so obvious!
    decks = {
     "CC": list(CC_cards),
     "CH": list(CH_cards)
    }

    # Let's shuffle! In place? Why not‽ We have no other choice!
    random.shuffle(decks["CC"])
    random.shuffle(decks["CH"])

    for turn in range(num_turns + turns_to_burn):
      if DEBUG: print("[Sim %d][Turn %d] Currently on: %s (Square %d)" % (sim, turn, current_square, s_to_i(current_square)))

      continueRolling = True
      numDoubles = 0
      while continueRolling:

        if (turn >= turns_to_burn):
          frequencies[current_square] += 1

        d1, d2 = dice()
        continueRolling = (d1 == d2)

        if DEBUG: print("[Sim %d][Turn %d] Rolled [%d, %d] => %d (Doubles? %r)" % (sim, turn, d1, d2, d1+d2, continueRolling))

        if (continueRolling):
          numDoubles += 1
          if (numDoubles == 3):
            if DEBUG: print("[Sim %d][Turn %d] Rolled three doubles. Going to JAIL." % (sim, turn))
            current_square = "JAIL"
            continue

        i = squares.index(current_square)
        i = (i + d1 + d2) % NUM_SQUARES
        current_square = i_to_s(i)

        CC_or_CH = current_square[:2]

        if current_square == "G2J":
          current_square = "JAIL"
          # In real Monopoly, the turn ends.
          # The problem description is not clear about this. :-/
          continue
        elif CC_or_CH in ["CC", "CH"]:

          card = decks[CC_or_CH][0]
          decks[CC_or_CH] = decks[CC_or_CH][1:] + [card]

          if isinstance(card, str):
            current_square = card
          elif callable(card): # Only one obvious way to do everything, duh: http://bugs.python.org/issue10518
            current_square = card(current_square)
          else:
            assert False # Trust no one.

          # HEY, PROBLEM STATEMENT. GET YOUR ACT TOGETHER.
          if current_square == "JAIL":
            continue

  return frequencies


frequencies = simulation(num_games=1, num_turns=100000, turns_to_burn=100)
sorted_frequencies = sorted(frequencies, key=frequencies.get)

if DEBUG: print(sorted(frequencies.items(), key=lambda x:x[1]))

result = ""
# Convert to a list because APPARENTLY PYTHON CAN'T SLICE THE FRONT OF A GENERATOR WITHOUT IMPORTING ITERTOOLS.
for square in list(reversed(sorted_frequencies))[:3]:
  result += "%02d" % s_to_i(square)
# https://github.com/lgarron/project-euler/blob/master/84.py
# I do not want to solve this problem
print(result)




