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

#Calculate Kendall Tau Distance (N^2)
def slow(filea, fileb, output):
	
	lista = [] #1st list (ordered)
	listb = [] #2nd list (not ordered)
	
	readfile(lista, filea) #fill lists
	readfile(listb, fileb) #with data

	x = len(lista) #length of list (both lists same length)
	count = 0 #number of inversions found

	start = time.clock() #start time

	#iterate for every pair in lists, find inversions, increment counter
	for i in range (0, x):
		for j in range (i+1, x):
#			print(str(lista[i]) + ", " + str(lista[j]) + 
#					" and " + str(listb[i]) + ", " + str(listb[j]))
			if ((lista[i]-lista[j]) * (listb[i]-listb[j]) < 0):
				count +=1
#				print("Discord")
	
	end = time.clock() #end time
	result = end-start #completion time

	print("\nFor " + filea + " and " + fileb)
	print("Kendall Tau Distance: " + str(count))
	print("Normalized Distance: " + str(count/(x*(x-1)/2)))
	print("Execution Time: " + str(result) + " seconds")

	#Write execution time to external file
	output.write(str(result)+'\n')

#Find Kendall Tau Distance (N^2) using various test data
def runslow():

	file1a = "../data/data0.1024"
	file1b = "../data/data1.1024"
	file2a = "../data/data0.2048"
	file2b = "../data/data1.2048"
	file4a = "../data/data0.4096"
	file4b = "../data/data1.4096"
	file8a = "../data/data0.8192"
	file8b = "../data/data1.8192"
	file16a = "../data/data0.16384"
	file16b = "../data/data1.16384"
	file32a = "../data/data0.32768"
	file32b = "../data/data1.32768"

	output = "slow.txt"
	fileo = open(output, "w")

	slow(file1a, file1b, fileo)
	slow(file2a, file2b, fileo)
	slow(file4a, file4b, fileo)
	slow(file8a, file8b, fileo)
	slow(file16a, file16b, fileo)
	slow(file32a, file32b, fileo)

#Merge sort for counting inversions for Kendall Tau Distance
def merge(numList):

	#base case, sublist of 1 element
	if len(numList) == 1: return numList, 0

	else:
		#split list in half
		a = numList[:int(len(numList)/2)]
		b = numList[int(len(numList)/2):]

		a, counta = merge(a) #recursively find inversions
		b, countb = merge(b) #of each sublist
		c = []

		i = j = 0
		count = counta + countb

		#merge sublists back in order
		while i < len(a) and j < len(b):
			if a[i] < b[j]:
				c.append(a[i])
				i += 1
			else:
				c.append(b[j])
				j += 1
				count += (len(a)-i)

		c += a[i:]
		c += b[j:]

#	print("Inversions: " + str(count))

	return c, count

#Calculate Kendall Tau Distance (NlogN)
def fast(input, output):

	numList = [] #create list
	readfile(numList, input) #fill list with data
	x = len(numList) #length of list

	start = time.clock() #start time
	numList, count = merge(numList) #do work
	end = time.clock() #end time
	result = end-start #completion time

	print("\nFor " + input)
	print("Kendall Tau Distance: " + str(count))
	print("Normalized Distance: " + str(count/(x*(x-1)/2)))
	print("Execution Time: " + str(result) + " seconds")

	#Write execution time to external file
	output.write(str(result)+'\n')

#Find Kendall Tau Distance (NlogN) using various test data
def runfast():

	file1b = "../data/data1.1024"
	file2b = "../data/data1.2048"
	file4b = "../data/data1.4096"
	file8b = "../data/data1.8192"
	file16b = "../data/data1.16384"
	file32b = "../data/data1.32768"

	output = "fast.txt"
	fileo = open(output, "w")

	fast(file1b, fileo)
	fast(file2b, fileo)
	fast(file4b, fileo)
	fast(file8b, fileo)
	fast(file16b, fileo)
	fast(file32b, fileo)

#Plot execution time results into graph
def plotter():

	points1 = []
	points2 = []

	#Read from file, insert contents into list
	file = open('slow.txt', "r")
	line = file.readline()
	while line:
		points1.append(float(line.strip('\n')))
		line = file.readline()
	file.close()

	file = open('fast.txt', "r")
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
	plt.ylabel('Time (seconds)')
	plt.title('Kendall Tau Distance Calculation - Execution Time')
	plt.legend(['N^2', 'Nlog(N)'], loc='upper left')
	fig.savefig('graph.png')

def main():

#	runslow()
	runfast()
	plotter()

main()
