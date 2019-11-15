import sys
sys.stdin = open('표준입출력.txt')

T = int(input())

N, M = map(int, input().split())

arr = [list(map(int, input())) for _ in range(5)]

print(arr)