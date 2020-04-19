import sys

sys.stdin = open("5337.txt")

T = int(input())

for tc in range(1,T+1):
    n = int(input())
    a = list(map(list,input().split()))

    cube = []
    for i in range(6):
        tem = [[i for _ in range(3)] for _ in range(3)]
        cube.append(tem)


    print(a)
    print(cube)