"""
Noah Rivera
Block 1
"""

"""
slicer.py.
    The program is to Print out a slice of the string from integer 1
    to integer 2 (inclusive of 2), and another slice from integer 3
    to integer 4 (inclusive of 4), with a space between each slice.
"""


"""
Variables
"""
# Users 1st Input 
inp=[]
# Users 2nd input
nums=1
#no.1
no=1
#no.2
nt=2
#no.3
nth=3
#no.4
nf=4
#used for knowing what num is entered
x=0
#Used to find the length of the string
y=""
z=0
"""
Variables
"""

"""
Input/Math
"""
# allows the program to check if the string is 200 words long
while z==0:
    inp=input("Enter a string:")
    y=len (inp)
    if y<=200:
        z+=1
    else:
        print("__________________________________________________")
        print("String needs to less than or equal to 200 words long")
        print("")
        print("__________________________________________________")

#just there to look nice
print("__________________________________________________")
print("")
for loop in range(4):
    
    nums=int(input("Enter four integers:"))
    x+=1
    if x==1:
        no=int(nums)
    elif x==2:
        nt=int(nums)
    elif x==3:
        nth=int(nums)
    else:
        nf=int(nums)
             
        
"""
Input/Math
"""


"""
Output
"""
print ("__________________________________________________")
print ("")
print (inp[no:nt+1])

print (inp[nth:nf+1])

print ("__________________________________________________")

"""
Output
"""






         
