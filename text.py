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
open/close.txt
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


"""
num of words
"""
txtf=opent()
txt = txtf.read().split()

close()
"""
number of each vowel
"""

aA=set("a A")
eE=("e","E")
iI=("i","I")
oO=("o","O")
uU=("u","U")

txtf=opent()
txt = txtf.read().split()

countA=0

for at in txt:
    if at in txt:
        countA+=1
        print(countA)
close()
