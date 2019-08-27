import sys

sys.stdin = open('Shuffle-O-Matic.txt')


T = int(input())

for tc in range(T):
    N = int(input())
    x = range(N)
    card = list(map(int, input().split()))
    print(card)

    deck1 = card[:N//2]
    deck2 = card[N//2:]

    print(deck1)
    print(deck2)