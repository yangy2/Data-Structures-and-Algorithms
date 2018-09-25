from matplotlib import pyplot as plt
import numpy as np

def main():

    x = [(1) for i in range(256)]
    f = open('./Ones/256.txt','w')

    for i in x:
        f.write('%f\n' %i)

    f.close()

    x = [(1) for i in range(512)]
    f = open('./Ones/512.txt', 'w')

    for i in x:
        f.write('%f\n' % i)

    f.close()

    x = [(1) for i in range(1024)]
    f = open('./Ones/1024.txt', 'w')

    for i in x:
        f.write('%f\n' % i)

    f.close()

    x = [(1) for i in range(2048)]
    f = open('./Ones/2K.txt', 'w')

    for i in x:
        f.write('%f\n' % i)

    f.close()

    x = [(1) for i in range(4096)]
    f = open('./Ones/4K.txt', 'w')

    for i in x:
        f.write('%f\n' % i)

    f.close()

    x = [(1) for i in range(8192)]
    f = open('./Ones/8K.txt', 'w')

    for i in x:
        f.write('%f\n' % i)

    f.close()

    x = [(1) for i in range(16384)]
    f = open('./Ones/16K.txt', 'w')

    for i in x:
        f.write('%f\n' % i)

    f.close()

    x = [(1) for i in range(32768)]
    f = open('./Ones/32K.txt', 'w')

    for i in x:
        f.write('%f\n' % i)

    f.close()

    x = [(1) for i in range(64536)]
    f = open('./Ones/64K.txt', 'w')

    for i in x:
        f.write('%f\n' % i)

    f.close()

main()
