import sys
sys.stdin = open("(5185)이진수_input.txt", "r")
asc = [[0, 0, 0, 0],  #0
       [0, 0, 0, 1],  #1
       [0, 0, 1, 0],  #2
       [0, 0, 1, 1],  #3
       [0, 1, 0, 0],  #4
       [0, 1, 0, 1],  #5
       [0, 1, 1, 0],  #6
       [0, 1, 1, 1],  #7
       [1, 0, 0, 0],  #8
       [1, 0, 0, 1],  #9
       [1, 0, 1, 0],  #A
       [1, 0, 1, 1],  #B
       [1, 1, 0, 0],  #C
       [1, 1, 0, 1],  #D
       [1, 1, 1, 0],  #E
       [1, 1, 1, 1]]  #F

def aToh(c):
    if c <= '9' : return ord(c) - ord('0')
    else : return ord(c) - ord('A') + 10

def makeT(x):
    for i in range(4):
        bin.append(asc[x][i])

T = int(input())
for tc in range(T):
    bin = []
    n, arr = input().split()

    for i in range(len(arr)):
           makeT(aToh(arr[i]))

    print("#{}".format(tc+1), end=" ")
    for i in range(len(bin)):
        print(bin[i], end="")
    print()