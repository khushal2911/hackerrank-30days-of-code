# Enter your code here. Read input from STDIN. Print output to STDOUT
import os
import sys
import math

if __name__ == '__main__':
    n = int(input())
    phonebook = {}
    for i in range(n):
        line = input().rstrip().split()
        phonebook[line[0]] = int(line[1])
    while(True):
        try :
            search = input()
            if search in phonebook.keys():
                print('{}={}'.format(search,phonebook[search]))
            else:
                print("Not found")
        except:
            break
