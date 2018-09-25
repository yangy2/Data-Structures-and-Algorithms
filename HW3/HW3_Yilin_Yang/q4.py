#Yilin Yang
#Data Structures & Algorithms HW3

import redblack as API
from random import shuffle
import numpy

class Tree:
	def __init__(self):
		self.root = None
		
	def insert(self, item):
##		print("Inserting: " + str(item))
		if self.root is None:
			self.root = API.Node(item)
		else:
			self.root.insert(API.Node(item))
			while self.root.parent:
				self.root = self.root.parent
		return True
		
	def count(self):
##		print ('\nPrinting Red Black Tree...')
		self.root.count(0)

def readfile(numList, filepath):
        with open(filepath) as f:
                line = f.readline()
                while line:
                        numList.append(int(line.strip('\n')))
                        line = f.readline()

def test(N, numList):
        shuffle(numList)
        
        tree = Tree()
##        print(str(N) + "-Insertions")
        for i in range(0, N): tree.insert(numList[i])
        tree.count()

        average = tree.root.path/tree.root.leaves

        return average

file = "data.txt"
numList = [] #create list
readfile(numList, file) #fill list with data
x = len(numList) #length of list

N1 = 1024
N2 = 2048
N3 = 4096
N4 = 8192
N5 = 10000

avg1 = avg2 = avg3 = avg4 = avg5 = []
trials = 1000

##print("Average: ", test(N1, numList))
##print("Average: ", test(N2, numList))
##print("Average: ", test(N3, numList))
##print("Average: ", test(N4, numList))
##print("Average: ", test(N5, numList))

for i in range(0, trials):
    avg1.append(test(N1, numList))
##    print(i)
print("Average Path Length for " + str(N1) + " keys: ", numpy.mean(avg1))
print("Standard Deviation for " + str(N1) + " keys: ", numpy.std(avg1))

print()

for i in range(0, trials):
    avg2.append(test(N2, numList))
##    print(i)
print("Average Path Length for " + str(N2) + " keys: ", numpy.mean(avg2))
print("Standard Deviation for " + str(N2) + " keys: ", numpy.std(avg2))

print()

for i in range(0, trials):
    avg3.append(test(N3, numList))
##    print(i)
print("Average Path Length for " + str(N3) + " keys: ", numpy.mean(avg3))
print("Standard Deviation for " + str(N3) + " keys: ", numpy.std(avg3))

print()

for i in range(0, trials):
    avg4.append(test(N4, numList))
##    print(i)
print("Average Path Length for " + str(N4) + " keys: ", numpy.mean(avg4))
print("Standard Deviation for " + str(N4) + " keys: ", numpy.std(avg4))

print()

for i in range(0, trials):
    avg5.append(test(N5, numList))
##    print(i)
print("Average Path Length for " + str(N5) + " keys: ", numpy.mean(avg5))
print("Standard Deviation for " + str(N5) + " keys: ", numpy.std(avg5))
