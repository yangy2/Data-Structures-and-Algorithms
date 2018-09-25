from matplotlib import pyplot as plt
import numpy as np

def main():

    x = [(0) for i in range(256)]
    f = open('./Zeros/256.txt','w')

    for i in x:
        f.write('%f\n' %i)

    f.close()

    x = [(0) for i in range(512)]
    f = open('./Zeros/512.txt', 'w')

    for i in x:
        f.write('%f\n' % i)

    f.close()

    x = [(0) for i in range(1024)]
    f = open('./Zeros/1024.txt', 'w')

    for i in x:
        f.write('%f\n' % i)

    f.close()

    x = [(0) for i in range(2048)]
    f = open('./Zeros/2K.txt', 'w')

    for i in x:
        f.write('%f\n' % i)

    f.close()

    x = [(0) for i in range(4096)]
    f = open('./Zeros/4K.txt', 'w')

    for i in x:
        f.write('%f\n' % i)

    f.close()

    x = [(0) for i in range(8192)]
    f = open('./Zeros/8K.txt', 'w')

    for i in x:
        f.write('%f\n' % i)

    f.close()

    x = [(0) for i in range(16384)]
    f = open('./Zeros/16K.txt', 'w')

    for i in x:
        f.write('%f\n' % i)

    f.close()

    x = [(0) for i in range(32768)]
    f = open('./Zeros/32K.txt', 'w')

    for i in x:
        f.write('%f\n' % i)

    f.close()

    x = [(0) for i in range(64536)]
    f = open('./Zeros/64K.txt', 'w')

    for i in x:
        f.write('%f\n' % i)

    f.close()

main()
