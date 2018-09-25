#Yilin Yang
#Data Structures & Algorithms HW1
import time

filepath = 'hw1-1.data/4096int.txt'
numList = []

#Read from file, insert contents into list
with open(filepath) as fp:
    line = fp.readline()
    while line:
        numList.append(int(line.strip('\n'))) #ignore delimiter
        line = fp.readline()

#Number of elements in list
x = len(numList)

#Print all elements in list
##for i in range(0, x): print(numList[i])

#Three Sum Algorithm (Brute Force)
start = time.clock()
count = 0
for i in range(0, x):
    for j in range(i+1, x):
        for k in range(j+1, x):
            if numList[i] + numList[j] + numList[k] == 0: count += 1
end = time.clock()

print('Given ' + str(x) + ' integers in ' + filepath + ':')
print('Triples that sum to zero found = ' + str(count))
print('Execution time = ' + str(end-start))

