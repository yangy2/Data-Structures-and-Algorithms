#Yilin Yang
#Data Structures & Algorithms HW2

import csv

#Fill list with contents of external file
def readfile(numList, filepath):

	with open(filepath) as f:
		line = f.readline()
		while line:
			numList.append(int(line.strip('\n')))
			line = f.readline()

	return numList

#Print contents of list (debugging purposes)	
def printlist(numList, x):
	
	for i in range (0, x): print(numList[i])

#Shell Sort Algorithm						   
def shellsort(numList, increment, swaps):

	for i in range (increment, len(numList)):
#		printlist(numList, len(numList))
		temp = numList[i]

		j = i
		while j>= increment and numList[j-increment] > temp:
			numList[j] = numList[j-increment]
			j -= increment
			swaps += 1
		
#		print("Switching " + str(temp) + " and " + str(numList[j]))
		numList[j] = temp

	return swaps

#Run shell sort using specific increments (7, 3, 1)
#Also runs insertion sort for comparison
def runshellsort(filepath):

	numList = []
	readfile(numList, filepath)

	swaps = 0
	swaps2 = 0

	print("\n *** " + filepath + " *** ")

	print("Shell Sort - Increment of 7")
	i7 = shellsort(numList, 7, swaps)
	swaps = swaps + i7
	print("Swaps made: " + str(i7) + ", Total: " + str(swaps) + "\n")
	
	print("Shell Sort - Increment of 3")
	i3 = shellsort(numList, 3, swaps)
	swaps = swaps + i3
	print("Swaps made: " + str(i3) + ", Total: " + str(swaps) + "\n")

	print("Shell Sort - Increment of 1")
	i1 = shellsort(numList, 1, swaps)
	swaps = swaps + i1
	print("Swaps made: " + str(i1) + ", Total: " + str(swaps) + "\n")

	swaps2 = runinsertsort(filepath)

	result  = [i7, i3, i1, swaps, swaps2]

#	printlist(numList, len(numList))

	return result

#Insertion Sort Algorithm (shell sort with increment 1)
def runinsertsort(filepath):
	
	numList = []
	readfile(numList, filepath)

	swaps = 0

#	print("\n *** " + filepath + " *** ")
	print("Insertion Sort")
	swaps = shellsort(numList, 1, swaps)
	print("Swaps made: " + str(swaps) + "\n")

#	printlist(numList, len(numList))

	return swaps

def main():
	
	file1 = "../data/data1.1024"
	file2 = "../data/data1.2048"
	file4 = "../data/data1.4096"
	file8 = "../data/data1.8192"
	file16 = "../data/data1.16384"
	file32 = "../data/data1.32768"

	result1 = runshellsort(file1)
	result1.insert(0, file1)

	result2 = runshellsort(file2)
	result2.insert(0, file2)

	result4 = runshellsort(file4)
	result4.insert(0, file4)

	result8 = runshellsort(file8)
	result8.insert(0, file8)

	result16 = runshellsort(file16)
	result16.insert(0, file16)

	result32 = runshellsort(file32)
	result32.insert(0, file32)

	#Write results to external csv file
	with open('comparisons.csv', 'w') as csvfile:
		writer = csv.writer(csvfile, delimiter=' ')
		writer.writerow(["File Directory Name", "Shell7", 
				"Shell3", "Shell1", "Shell+", "Insertion"])
		writer.writerow(result1)
		writer.writerow(result2)
		writer.writerow(result4)
		writer.writerow(result8)
		writer.writerow(result16)
		writer.writerow(result32)

main()
