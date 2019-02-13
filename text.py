"""
Noah
Rivera
Block1
"""

"""
file_stats.py

A program to determine the following statistics about the file:
The number of lines in the file
The number of words in the file
The number of 4 letter words in the file
The number of each of the vowels in the file
The longest word in the file
"""

"""
open/close.txt
"""
def opent():
    return open ("programs3.txt","r")
def close():
    txtf.close()
"""
open/close.txt/split
"""

"""
length
of lines
"""
txtf=opent()
lines = txtf.readlines()
numol = len(lines)
close()
print (numol)
"""
length
of lines
"""
"""
num of words
"""
def numw():
    
    txtf=opent()
    txt = txtf.read().split()
    return (len(txt))


close()


"""
num of words
"""

"""
number of each vowel
"""
countA=0
countE=0
countI=0
countO=0
countU=0
countALL=0

aA="a"
eE="e"
iI="i"
oO="o"
uU="u"

txtf=opent()
x=0 
ntxt=len(txtf.read())
close()

txtf=opent()
while x <= ntxt:
    x+=1
    newtx=txtf.read(1).lower()
      
    if aA == newtx:
        countA+=1
    elif eE in newtx:
        countE+=1
    elif iI in newtx:
        countI+=1
    elif oO in newtx:
        countO+=1
    elif uU in newtx:
        countU+=1
countALL=countA+countE+countI+countO+countU
    
close()
print (countA)
print (countE)
print (countI)
print (countO)
print (countU)
print (countALL)
"""
number of each vowel
"""

"""
num of 4 letter words
"""
def fl():
    txtf=opent()
    txt = txtf.read().split()
    return (nfl)
    close()
"""
num of 4 letter words
"""

"""
longest word
"""

"""
longest word
"""
