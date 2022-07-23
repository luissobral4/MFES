import re

def printTabuleiro(tabuleiro,sinaisL,size):
 l = 0
 while l < size:
  c = 0
  while c < size:
   pos = l * size + c
   if pos in tabuleiro and tabuleiro[pos] != -1:
    print(tabuleiro[pos],end = "")
   else:
    print(' ',end = "")

   pos = l * (size - 1) + c
   if pos in sinaisL and c != 4:
    print(sinaisL[pos],end = "")
   else:
    print(' ',end = "")
   c += 1

  print('')
  l+=1
 return
 

tabuleiro = dict()
sinaisL = dict()
sinaisC = dict() 
size = 0

tabRE = re.compile(r'P(\d+) (\d+)')
sinaisRE = re.compile(r'([<>]) (\d+)')

with open("P1.txt") as f:
 file = f.read()
 s = re.search(r'Size (\d+)',file)
 size = int(s.group(1))
 tabContent = re.findall(tabRE, file)
 sinaisContent = re.findall(sinaisRE, file)

for line in tabContent:
 tabuleiro[int(line[0])] = int(line[1])

for line in sinaisContent:
 sinaisL[int(line[1])] = line[0]


l = 0
while l < size:
 c = 0
 while c < size:
  pos = l * size + c
  if pos not in tabuleiro:
   tabuleiro[pos] = -1
  c += 1
 l += 1

printTabuleiro(tabuleiro,sinaisL,size)


from z3 import *

s = Solver()

l = 0
while l < size:
    pos = l * size
    tabuleiro[pos] = Int('tabuleiro[pos]')
    tabuleiro[pos+1] = Int('tabuleiro[pos+1]')
    tabuleiro[pos+2] = Int('tabuleiro[pos+2]')
    tabuleiro[pos+3] = Int('tabuleiro[pos+3]')
    tabuleiro[pos+4] = Int('tabuleiro[pos+4]')

    s.add(Distint
