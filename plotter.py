#-------------------------------#
#Joel Aoto                      #
#-------------------------------#

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from string import ascii_lowercase

#Functions
def word_count(file_path):
    aCount = dict()
    alphCount = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
                 'q','r','s','t','u','v','w','x','y','z'] 
    for x in alphCount:
        aCount[x] = 0
            
    for c in aCount:
        aCount[c] = looper(c)

    return aCount   

def looper(c):
    value = 0
    with open(file_path,'r') as df:
        for line in df:
            for y in line:
                if c == y:
                    value += 1
    return value

#Main
file_path = './words.txt'
hist = word_count(file_path)

x = hist.keys()
y = np.array(hist.values())

plt.bar(x,hist.values())
plt.plot(x, hist.values(), color='red', marker='o', linestyle='solid',
         linewidth=1, markersize=4)
plt.xlabel('Character')
plt.ylabel('Frequency')
plt.grid(True)
plt.savefig('result.png')
plt.show()

