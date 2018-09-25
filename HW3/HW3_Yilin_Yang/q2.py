#Yilin Yang
#Data Structures & Algorithms HW3

import q1 as API
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
##		print ('\nPrinting 2-3 Tree...')
		self.root.count()

tree = Tree()

numList = list(range(128000))
N = int(input("Input Size of N: "))

if N > len(numList):
    print("Too big, resizing to ", len(numList))
    N = len(numList)

randomize = input("Randomize input? (y/n) ")
if randomize == "y":
    shuffle(numList)
    print("\n### RANDOM ###")

else: print("\n### SORTED ###")

print(str(N) + "-Insertions")
for i in range(0, N): tree.insert(numList[i])
tree.count()
