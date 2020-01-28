import sys

sys.stdin = open("16235.txt")

N,M,K = map(int, input().split())

ground = [list(map(int, input().split())) for _ in range(N)]