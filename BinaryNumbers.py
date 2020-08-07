#!/bin/python3

import math
import os
import random
import re
import sys

def dectobin(n):
    binary = ''
    while(n>=1):
        if n==1:
            binary = ''.join([binary,str(n)])
            return binary
        else:
            r = n%2
            binary = ''.join([binary,str(r)])
            n = n//2
    return binary


if __name__ == '__main__':
    n = int(input())
    binary = dectobin(n)
    result = binary.split('0')
    print(max([len(x) for x in result]))
