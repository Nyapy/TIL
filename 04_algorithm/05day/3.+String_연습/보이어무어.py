def preprocess(P, M, PI):
    for i in range(M-1):
        PI[ord(P[i])] = i + 1

def BoyerMooreHorspool(T, N, P, M, PI):
    i, j, k, l = 0, 0, 0, 0
    pos = -1
    while i <= N-M:
        j = M -1
        k = i + M - 1
        while j >= 0 and P[j] == T[k]:
            j -= 1
            k -= 1
        if j == -1:
            pos = i
            break
        i = i + (M -PI[ord(T[i + M -1])])

    return pos

T = "abcdabcdabcdabcef"
P = "abcdabcef"
ASCII = 128
PI = [0] * (ASCII+1)

N = len(T)
M = len(P)
preprocess(P, M, PI)
pos = BoyerMooreHorspool(T, N, P, M, PI)
print(pos)