#Fill list with contents of external file
def readfile(numList, filepath):

	with open(filepath) as f:
		line = f.readline()
		while line:
			numList.append(float(line.strip('\n')))
			line = f.readline()

	return numList

def main():
        
        file = "./Dataset/(-1,1)/"
        file0 = file + "512.txt"

        numList = []

        readfile(numList, file)

        for i in range(len(numList)): print(str(numList[i]))

main()
