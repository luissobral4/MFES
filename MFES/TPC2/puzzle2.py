import re
import numpy as np

def printTabuleiro(tabuleiro,sinaisL,size):
 l = 0
 while l < size:
  c = 0
  while c < size:
    print(tabuleiro[l][c],end = "")
    if c != 4 and sinaisL[l][c] != 0:
     if(sinaisL[l][c] == 1):
      print('>',end = "")
     else:
      print('<',end = "")
    else:
     print(' ',end = "")
    c += 1

  print('')
  l+=1
 return
 

sinaisL = dict()
sinaisC = dict() 
size = 0

tabRE = re.compile(r'P(\d+) (\d+) (\d+)')
sinaisRE = re.compile(r'S(-?\d+) (\d+) (\d+)')

with open("P1.txt") as f:
 file = f.read()
 s = re.search(r'Size (\d+)',file)
 size = int(s.group(1))

 sz = (size,size)
 tab = np.zeros(sz, dtype=int)
 sinaisL = np.zeros((size,size - 1), dtype=int)
     
 tabContent = re.findall(tabRE, file)
 sinaisContent = re.findall(sinaisRE, file)

 for line in tabContent:
  tab[int(line[0])][int(line[1])] = int(line[2])

 for line in sinaisContent:
  sinaisL[int(line[1])][int(line[2])] = int(line[0])

printTabuleiro(tab,sinaisL,size)


from z3 import *

# 9x9 matrix of integer variables
X = [ [ Int("x_%s_%s" % (i+1, j+1)) for j in range(size) ] 
      for i in range(size) ]

# each cell contains a value in {1, ..., size}
cells_c  = [ And(1 <= X[i][j], X[i][j] <= size) 
             for i in range(size) for j in range(size) ]

# each row contains a digit at most once
rows_c   = [ Distinct(X[i]) for i in range(size) ]

# each column contains a digit at most once
cols_c   = [ Distinct([ X[i][j] for i in range(size) ]) 
             for j in range(size) ]

futoshiki = cells_c + rows_c + cols_c

tab_c = [ If(tab[i][j] == 0, 
            True, 
            X[i][j] == tab[i][j])
          for i in range(size) for j in range(size) ]


s = Solver()

s.add(futoshiki + tab_c)
for l in range(size):
    for c in range(size - 1):
        if(sinaisL[l][c] == 1):
            s.add(X[l][c] > X[l][c + 1])
        elif (sinaisL[l][c] == -1):
            s.add(X[l][c] < X[l][c + 1])

if s.check() == sat:
    m = s.model()
    print(m)
else:
    print( "failed to solve")
                  

