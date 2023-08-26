#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    arr.sort()
    minmax=[None]*int(len(arr)-3)
    for i in range(0,len(arr)-3):
        temp=0
        for j in range(i,i+4):
            temp=temp+arr[j]
        minmax[i]=temp
    print(minmax[0],minmax[-1])

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
