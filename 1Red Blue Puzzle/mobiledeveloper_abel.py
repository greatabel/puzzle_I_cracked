"""
created by Abel , tested at Python 2.7.5 ,2013-11-06


step1 -> mark the titles with ids:
0  1  2  3
4  5  6  7
8  9  10 11
12 13 14 15


step2 -> define the matrix by red titles 's status set of start and end:

start set is : 1 4 5 8 9 12 13
end set is   : 2 5 7 8 10 13 15
We can consider the status of the matrix as a 16bit binary string: 
at beginning ,according to red's start set , the binary string is:  0011001100110010, 
the value of the bytes is sum([ power(2,x) for x in start set ])
at the end ,we want the matrix's status to be present as: 1010010110100101,
the value of the bytes is sum([ power(2,x ) for x in end set ])


step3 -> define the all the possible move of the white tilte according to 
         its location and puzzle boundary
3.1 when white is not at first row , it can move up.
3.2 when white is not at the rightmost column, it can move to right.
3.3 when white is not at bottom row, it can move down.
3.4 when white is not at first column ,it can move left.

We only care the white's interaction with red, so  when white is 
not coming from red status set poistion move to red set ,we should add the value to
currentValue change, oppositely we remove the change value.
step4 -> define the trversal policy

We choose BFS ,as our aim is to more less time not memory.
we start to move white from start status, after every move ,we ciculate the bytes's value
when bytes's value = end's status value and white move back to 0 position ,we stop, 
otherwise we store the current value and current
already moved path and bytes's value to a multidimensional array.

 #answer is -> RRDLLURRRDLLURDDLDRURDLULLDRUULU
"""
import time;
#import pdb
#from PdbSublimeTextSupport import preloop, precmd
#pdb.Pdb.preloop = preloop
#pdb.Pdb.precmd = precmd

 



def move((whiteBeforeThisMove,currentValue)):
  next_possible_move = []
  now_white_possible_positions=[]

  if whiteBeforeThisMove > 3    : now_white_possible_positions.append(('U',whiteBeforeThisMove - 4))
  if whiteBeforeThisMove % 4!=3 : now_white_possible_positions.append(('R',whiteBeforeThisMove + 1))
  if whiteBeforeThisMove < 12   : now_white_possible_positions.append(('D',whiteBeforeThisMove + 4))
  if whiteBeforeThisMove % 4!=0 : now_white_possible_positions.append(('L',whiteBeforeThisMove - 1))

  def circulate_currentValue(posssible_positions):

      def inredset(position):
        #print 'currentValue=',currentValue,'position=',position
        redflag = ((currentValue & (2**position))>0)
        return redflag
       
      for direction,whiteAfterThisMove in posssible_positions:
        
        
        if inredset(whiteAfterThisMove) and not inredset(whiteBeforeThisMove):
          nextValue = currentValue + (2**whiteBeforeThisMove )
        elif not inredset(whiteAfterThisMove) and inredset(whiteBeforeThisMove):
          #pdb.set_trace()
          nextValue = currentValue - (2**whiteBeforeThisMove )
        else:
          nextValue = currentValue
        next_possible_move.append((direction,(whiteAfterThisMove,nextValue)))
      return next_possible_move

  thisStep=circulate_currentValue(now_white_possible_positions)
  #pdb.set_trace()
  return thisStep




def main():

  start = (0, sum(2**x for x in [1,4,5,8,9,12,13]))
  end = (0, sum(2**x for x in [2,5,7,8,10,13,15])) 
  nextpossibleSet = set([start])    
  current = {start: set([""])} 
  #print 'current=',current
  while end not in current:
    tmp = {}
    to_add = set()
    for currentWhite, path in current.iteritems():
      for direction, next in move(currentWhite):
        if not next in nextpossibleSet:
          to_add.add(next)
          if not next in tmp: tmp[next] = set()
          for movepath in path:
            tmp[next].add(movepath+direction)
    

    nextpossibleSet = nextpossibleSet.union( to_add ) 
    #print 'nextpossibleSet=',nextpossibleSet
    current = tmp

  print ''.join(current[end])
  

if __name__ == "__main__":
  start_time = time.time()
  main()
  print time.time() - start_time, "seconds"



