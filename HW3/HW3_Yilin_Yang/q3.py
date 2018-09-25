#Yilin Yang
#Data Structures & Algorithms HW3

import redblack as API
from random import shuffle
import math

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

        percent = tree.root.red/tree.root.redblack
##        print("Red Links: ", tree.root.red)
##        print("Total Links: ", tree.root.redblack)
##        print("% of Links that are Red: ", percent)
        tree.root.reset()

        return percent

file = "data.txt"
numList = [] #create list
readfile(numList, file) #fill list with data
x = len(numList) #length of list

N1 = 10000
N2 = 100000
N3 = 1000000

avg1 = avg2 = avg3 = 0
trials = 40

for i in range(0, trials): avg1 += test(N1, numList)
avg1 = avg1/trials
print("Red Link % for " + str(N1) + " keys: ", avg1)

for i in range(0, trials): avg2 += test(N2, numList)
avg2 = avg2/trials
print("Red Link % for " + str(N2) + " keys: ", avg2)

for i in range(0, trials): avg3 += test(N3, numList)
avg3 = avg3/trials
print("Red Link % for " + str(N3) + " keys: ", avg3)
