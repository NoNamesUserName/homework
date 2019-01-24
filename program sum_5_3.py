"""
Noah Rivera
Block 1
"""

"""
  program sum_5_3.py
     The point of this program is to add all natural
     numbers that are sum of all the
     multiples of three or five 
"""



"""
Variables
"""
tf=0
summ=0
x=0
"""
Variables
"""



"""
Math
"""
# if and else statemen makes it so you will not have to
# have multiples of one number
for tf in range(1000):
    if x %3 == 0:
        summ += tf
    elif x %5 == 0:
        summ += tf
"""
Math
"""


"""
Home Screen 
"""

print ("__________________________________________________")
print ("")
print ("The sum of all the multiples of three and five is")
print (summ)
print ("__________________________________________________")

"""
Home Screen 
"""



"""
Exit screen
"""
input("\n\nPress the enter key to exit.")
quit()
"""
Exit Screen
"""
