from matplotlib import pyplot as plt
import numpy as np

def main():

    x = [(-1)**i for i in range(256)]
    f = open('256.txt','w')

    for i in x:
        f.write('%f\n' %i)

    f.close()

    x = [(-1)**i for i in range(512)]
    f = open('512.txt', 'w')

    for i in x:
        f.write('%f\n' % i)

    f.close()

    x = [(-1) ** i for i in range(1024)]
    f = open('1024.txt', 'w')

    for i in x:
        f.write('%f\n' % i)

    f.close()

    x = [(-1) ** i for i in range(2048)]
    f = open('2K.txt', 'w')

    for i in x:
        f.write('%f\n' % i)

    f.close()

    x = [(-1) ** i for i in range(4096)]
    f = open('4K.txt', 'w')

    for i in x:
        f.write('%f\n' % i)

    f.close()

    x = [(-1) ** i for i in range(8192)]
    f = open('8K.txt', 'w')

    for i in x:
        f.write('%f\n' % i)

    f.close()

    x = [(-1) ** i for i in range(16384)]
    f = open('16K.txt', 'w')

    for i in x:
        f.write('%f\n' % i)

    f.close()

    x = [(-1) ** i for i in range(32768)]
    f = open('32K.txt', 'w')

    for i in x:
        f.write('%f\n' % i)

    f.close()

    x = [(-1) ** i for i in range(64536)]
    f = open('64K.txt', 'w')

    for i in x:
        f.write('%f\n' % i)

    f.close()

main()
