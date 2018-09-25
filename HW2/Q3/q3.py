#Yilin Yang
#Data Structures & Algorithms HW2

#Write a txt file with contents to sort
def write():

	output = "data.txt"
	file = open(output, "w")

	for i in range (0, 1024): file.write("1\n")
	for i in range (0, 2048): file.write("11\n")
	for i in range (0, 4096): file.write("111\n")
	for i in range (0, 1024): file.write("1111\n")

#Fill list with contents of external file
def readfile(numList, filepath):

	with open(filepath) as f:
		line = f.readline()
		while line:
			numList.append(int(line.strip('\n')))
			line = f.readline()

	return numList

#Bucket Sort Algorithm
def bucket(numList):
	
	count = [0]*len(numList)

	for i in range (0, len(numList)):
		count[numList[i]] += 1

	for i in range (0, len(count)):
		if(count[i] !=  0):
			print(str(i) + " x " + str(count[i]))


def main():

	numList = []
	numList = readfile(numList, "data.txt")
	bucket(numList)

main()
