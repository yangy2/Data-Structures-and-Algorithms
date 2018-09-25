# Read from external file and put into list
def readfile(numList, filepath):
    with open(filepath) as f:
        line = f.readline()
        while line:
            numList.append(int(line.strip('\n')))
            line = f.readline()
            
file = "data.txt"
numList = [] #create list
readfile(numList, file) #fill list with data
x = len(numList) #length of list

numList2 = []

for i in range(0,x):
    if numList[i] not in numList2:
        numList2.append(numList[i])

for i in range(0, len(numList2)): print(numList2[i])

##numList.sort()
##check = 0
##for i in range(0,x):
##    if numList[i] != check:
##        print(numList[i])
##        check = numList[i]
##z = 7
### fill BST
##for i in range(1, x):
##    if numList[i] == z:
##        print("Found", z, "at line", i)
##        break
##print("Done")
