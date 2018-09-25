#Yilin Yang
#Data Structures & Algorithms HW2

import random
import time
import matplotlib.pyplot as plt
import tkinter

N = 7 #Insertion Sort Cut-Off
#Comment out the randomization in runquicksort
#for consistentcy when testing different N values

#Fill list with contents of external file
def readfile(numList, filepath):

	with open(filepath) as f:
		line = f.readline()
		while line:
			numList.append(int(line.strip('\n')))
			line = f.readline()

	return numList

#Switch two elements in a list
def swap(numList, i, j):
    numList[i], numList[j] = numList[j], numList[i]

#Shell Sort Algorithm - Insertion sort when provided increment 1					   
def shellsort(numList, increment, swaps):

    for i in range (increment, len(numList)):
        temp = numList[i]

        j = i
        while j>= increment and numList[j-increment] > temp:
            numList[j] = numList[j-increment]
            j -= increment
            swaps += 1
		
        numList[j] = temp
    return swaps

#Find median of 3 elements for partitioning
def median(numList, left, right):

    #Given leftmost and rightmost element
    #Find the central element
    center = (left + right)//2

    #Find the pivot value out of the 3 values
    median = [numList[left], numList[center], numList[right]]
    median.sort()
    pivot = median[len(median)//2]

    #Find index of pivot value
    if(pivot == numList[left]): index = left
    elif(pivot == numList[right]): index = right
    else: index = center

##    print("Leftmost index (" + str(left) + ") = " + str(numList[left]))
##    print("Rightmost index (" + str(right) + ") = " + str(numList[right]))
##    print("Central index (" + str(center) + ") = " + str(numList[center]))
##    print("Pivot will be " + str(pivot))

    return index #the index of the pivot in the list

def quicksort(numList, left, right):

    #Quicksort the list if there's more than N elements
    if(right-left > N):

        #Find pivot value using median-of-3
        pivotdex = median(numList, left, right)
        pivot = numList[pivotdex]

        #Variables to iterate through list
        i = left
        j = right
        count = 0 #number of swaps made
        
        #Begin quicksorting
##        print("Begin " + str(numList[left:right+1]))
        while(1):
            while(numList[i] < pivot): i+=1
##            print(str(numList[i]) + " >= " + str(pivot))
            while(numList[j] > pivot): j-=1
##            print(str(numList[j]) + " <= " + str(pivot))
            if(i<j):
                swap(numList, i, j)
                count += 2
##                print(numList[left:right+1])
            else:
##                print("Don't swap")
                break
##        print("End " + str(numList[left:right+1]))

        #Quicksort sublists recursively
        a = quicksort(numList, left, i-1)
        b = quicksort(numList, i+1, right)
        count = count + a + b

        return count
    
    else:
        count = 0
        temp = numList[left:right+1]
        count = shellsort(temp, 1, count)
        numList[left:right+1] = temp
        return count

def runquicksort(input, output):

    numList = []
    numList = readfile(numList, input) #read input file
#    numList = random.sample(numList, len(numList)) #shuffle contents

    start = time.clock()
    count = quicksort(numList, 0, len(numList)-1) #do quicksort
    end = time.clock()
    result = end-start #get time

    #Write sorted data to external file
    sortedlist = input[8:] + "_Quicksorted.txt"
    sort = open(sortedlist, "w")
    for i in range (0, len(numList)):
        sort.write(str(numList[i])+'\n')

    #Report
    print("Contents of " + input[8:] + " Quicksorted")
    print("Comparisons Made: " + str(count))
    print("Execution Time: " + str(result) + " seconds\n")

    #Write number of comparisons made
    output.write(str(count)+'\n')

##    print(numList)

#Plot results into graph
def plotter():

	points1 = []
	points2 = []
	points3 = []

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

	file = open('compares.txt', "r")
	line = file.readline()
	while line:
		points3.append(float(line.strip('\n')))
		line = file.readline()
	file.close()
	
        #Plot results
	x = [1024, 2048, 4096, 8192, 16384, 32768]
	fig = plt.figure()
	plt.plot(x, points1)
	plt.plot(x, points2)
	plt.plot(x, points3)
	plt.xlabel('Problem Size')
	plt.ylabel('Comparisons')
	plt.title('Merge Sort vs Quick Sort')
	plt.legend(['Merge - Bottom Up', 'Merge - Top Down', 'Quick - N=7'], loc='upper left')
	fig.savefig('graph.png')
	
def main():

    file1 = "../data/data1.1024"
    file2 = "../data/data1.2048"
    file4 = "../data/data1.4096"
    file8 = "../data/data1.8192"
    file16 = "../data/data1.16384"
    file32 = "../data/data1.32768"

    output = open("compares.txt", "w")
    
    runquicksort(file1, output)
    runquicksort(file2, output)
    runquicksort(file4, output)
    runquicksort(file8, output)
    runquicksort(file16, output)
    runquicksort(file32, output)

    output.close()
    plotter()
    
main()
