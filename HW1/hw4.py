#Yilin Yang
#Data Structures & Algorithms HW1
import time

filepath = 'hw1-1.data/8int.txt'
numList = []

#Read from file, insert contents into list
with open(filepath) as fp:
    line = fp.readline()
    while line:
        numList.append(float(line.strip('\n'))) #ignore delimiter
        line = fp.readline()

#Number of elements in list
x = len(numList)

min = numList[0]
mindex = 0
max = numList[0]
maxdex = 0

for i in range(0, x):
    if numList[i] > max:
        max = numList[i]
        maxdex = i
    if numList[i] < min:
        min = numList[i]
        mindex = i

print('Min is ' + str(min) + ' at index ' + str(mindex))
print('Max is ' + str(max) + ' at index ' + str(maxdex))
print('Smallest difference between two values is ' + str(max-min))

