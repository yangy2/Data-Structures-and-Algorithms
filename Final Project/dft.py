# Discrete Fourier Transform (DFT)
# FB - 20141227

import random
import math
import cmath
import time

pi2 = cmath.pi * 2.0

#Fill list with contents of external file
def readfile(numList, filepath):
    with open(filepath) as f:
        line = f.readline()
        while line:
            numList.append(float(line.strip('\n')))
            line = f.readline()
            
    return numList

def pickdata():

    filepath = "./Dataset/"

    print("Data Set")
    print("0. Zeros")
    print("1. Ones")
    print("2. -1 to 1")

    var = int(input("Enter a Number: "))

    if   var == 1: filepath += "Ones/"
    elif var == 2: filepath += "(-1,1)/"
    else: filepath += "Zeros/"

    print("Data Size")
    print("256. 256")
    print("512. 512")
    print("1. 1k")
    print("2. 2k")
    print("4. 4k")
    print("8. 8k")
    print("16. 16k")
    print("32. 32k")
    print("64. 64k")

    var = int(input("Enter a Number: "))

    if   var == 1: filepath += "1024.txt"
    elif var == 2: filepath += "2K.txt"
    elif var == 4: filepath += "4K.txt"
    elif var == 8: filepath += "8K.txt"
    elif var == 16: filepath += "16K.txt"
    elif var == 32: filepath += "32K.txt"
    elif var == 64: filepath += "64K.txt"
    elif var == 512: filepath += "512.txt"
    else: filepath += "256.txt"

    print(filepath)
    print()
    
    return filepath

def DFT(fnList):
    ops = 0
    N = len(fnList)
    FmList = []
    for m in range(N):
        Fm = 0.0
        for n in range(N):
            Fm += fnList[n] * cmath.exp(- 1j * pi2 * m * n / N)
            ops += 1
        FmList.append(Fm / N)
    return FmList, ops
        
def InverseDFT(FmList):
    N = len(FmList)
    fnList = []
    for n in range(N):
        fn = 0.0
        for m in range(N):
            fn += FmList[m] * cmath.exp(1j * pi2 * m * n / N)
        fnList.append(fn)
    return fnList

def testinput():
    # TEST
    print ("Input Sine Wave Signal:")
    N = 360 # degrees (Number of samples)
    a = float(random.randint(1, 100))
    f = float(random.randint(1, 100))
    p = float(random.randint(0, 360))
    print ("frequency = " + str(f))
    print ("amplitude = " + str(a))
    print ("phase ang = " + str(p))
    print ()

    fnList = []

    for n in range(N):
        t = float(n) / N * pi2
        fn = a * math.sin(f * t + p / 360 * pi2)
        fnList.append(fn)

    return fnList

def main():
    fnList = []

    filepath = pickdata()
    
    readfile(fnList, filepath)

##    print(str(FnList))
    
    print ("DFT Calculation Results:")
    start = time.time()
    FmList, ops = DFT(fnList)
    end = time.time()
    

##    print(str(FmList))
    
    threshold = 0.001
    for (i, Fm) in enumerate(FmList):
        if abs(Fm) > threshold:
            print ("frequency = " + str(i))
            print ("amplitude = " + str(abs(Fm) * 2.0))
            p = int(((cmath.phase(Fm) + pi2 + pi2 / 4.0) % pi2) / pi2 * 360 + 0.5)
            print ("phase ang = " + str(p) + "\n")

    print("Execution Time: " + str(end-start) + " seconds")
    print("Total Operations: " + str(ops))
    
    #Recreate input signal from DFT results and compare to input signal
##    fnList2 = InverseDFT(FmList)
##    for n in range(len(fnList)):
##        print (fnList[n], fnList2[n].real)

if __name__ == "__main__":
    main()
