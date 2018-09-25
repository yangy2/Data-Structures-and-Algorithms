#Yilin Yang
#Data Structures & Algorithms HW2

import time
import matplotlib.pyplot as plt
import tkinter

#Fill list with contents of external file
def readfile(numList, filepath):

	with open(filepath) as f:
		line = f.readline()
		while line:
			numList.append(int(line.strip('\n')))
			line = f.readline()

	return numList

#Merge Sort - Top Down 
def merge(numList):

	#counter for comparison is incremented
	#whenever list is split in half
	#and when merging elements 

	#base case, sublist of 1 element
	#returns list and number 1 to add to counter
	if len(numList) == 1: return numList, 1

	else:
		#split list in half
		a = numList[:int(len(numList)/2)]
		b = numList[int(len(numList)/2):]

		a, counta = merge(a) #recursively mergesort
		b, countb = merge(b) #sublists
		c = []

		i = j = 0
		count = counta + countb #add counters from sublists

		#merge sublists back in order
		while i < len(a) and j < len(b):
			if a[i] < b[j]:
				c.append(a[i])
				i += 1
				count += 1
			else:
				c.append(b[j])
				j += 1
				count += 1
				
		c += a[i:]
		c += b[j:]

	return c, count

#Merge Sort - Bottom Up
def mergeBU(numList):

	length = len(numList)
	
	power = 2 #initial size of sublists
	count = 0 #number of comparisons made

	while(power <= length):

#		print("Power: " + str(power))

		for i in range(0, length): 
			if(i % power == power-1): #For sublist size of 2, 4, 8...
				temp = numList[i-(power-1):i+1] #Create the sublist
				temp.sort() #And sort it
				count += len(temp)-1
				numList[i-(power-1):i+1] = temp #Put back sorted sublist

		power *= 2 #increase size of sublists for next iteration

#		for i in range(0, length): print(numList[i])

	return numList, count

#Run specific merge algorithm given inputs, write results
def runmerge(input, output, x):

	numList = []
	readfile(numList, input)

	start = time.clock()

	#check if using top down/bottom up
	if(x == 1): numList, count = merge(numList)
	else: numList, count = mergeBU(numList)

	end = time.clock()
	result = end-start

	if(x == 1): sortedlist = input[8:] + "_Top_Down.txt"
	else: sortedlist = input[8:] + "_Bottom_Up.txt"
	print(sortedlist)

	#Write sorted data to external file
	sort = open(sortedlist, "w")
	for i in range (0, len(numList)):
		sort.write(str(numList[i])+'\n')

	#Report
	if(x == 1): print("Contents of " + input[8:] + " Sorted Top Down")
	else: print("Contents of " + input[8:] + " Sorted Bottom Up")
	print("Comparisons Made: " + str(count))
	print("Execution Time: " + str(result) + " seconds\n")

	#Write number of comparisons made
	output.write(str(count)+'\n')

def experiment(x):

	file1 = "../data/data1.1024"
	file2 = "../data/data1.2048"
	file4 = "../data/data1.4096"
	file8 = "../data/data1.8192"
	file16 = "../data/data1.16384"
	file32 = "../data/data1.32768"

	if (x == 1):
		output = "topdown.txt"
		fileo = open(output, "w")

		runmerge(file1, fileo, x)
		runmerge(file2, fileo, x)
		runmerge(file4, fileo, x)
		runmerge(file8, fileo, x)
		runmerge(file16, fileo, x)
		runmerge(file32, fileo, x)

	else:
		output = "bottomup.txt"
		fileo = open(output, "w")

		runmerge(file1, fileo, x)
		runmerge(file2, fileo, x)
		runmerge(file4, fileo, x)
		runmerge(file8, fileo, x)
		runmerge(file16, fileo, x)
		runmerge(file32, fileo, x)

#Plot results into graph
def plotter():

	points1 = []
	points2 = []

	#Read from file, insert contents into list
	file = open('bottomup.txt', "r")
	line = file.readline()
	while line:
		points1.append(float(line.strip('\n')))
		line = file.readline()
	file.close()

	file = open('topdown.txt', "r")
	line = file.readline()
	while line:
		points2.append(float(line.strip('\n')))
		line = file.readline()
	file.close()

#	j = len(points)
#	for i in range (0, j): print(points[i])

	#Plot results
	x = [1024, 2048, 4096, 8192, 16384, 32768]
	fig = plt.figure()
	plt.plot(x, points1)
	plt.plot(x, points2)
	plt.xlabel('Problem Size')
	plt.ylabel('Comparisons')
	plt.title('Merge Sort - Implementation Analysis')
	plt.legend(['Bottom Up', 'Top Down'], loc='upper left')
	fig.savefig('graph.png')

def main():

	experiment(1)
	experiment(2)
	plotter()

main()
