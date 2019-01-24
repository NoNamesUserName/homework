
lists = []
for x in range(4):
    c = int(input("? "))
    if x % 2 != 0:
        c += 1
    lists.append(c)
    
        
print(lists)

lists.sort()
x = "HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain."

print(x[lists[0]:lists[1]], x[lists[2]:lists[3]])
print (sqrt [144])
