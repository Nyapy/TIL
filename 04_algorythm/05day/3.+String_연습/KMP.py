def preprocess(P, M, PI):
    i, j = 0, -1
    PI[0] = -1
    while i < M:
        while j > -1 and P[i] != P[j]:
            j = PI[j]
        i += 1
        j += 1
        PI[i] = j

def KMP(T, N, P, M, PI):
    i, j = 0, 0
    pos = -1
    while i < N:
        while j >= 0 and T[i] != P[j]:
            j = PI[j]
        i += 1
        j += 1
        if j == M :
            pos = i - j
            break
    return pos

T = "abcdabcdabcdabcef"
P = "abcdabcef"
PI = [0] * (len(P) + 1)

N = len(T)
M = len(P)
preprocess(P, M, PI)
pos = KMP(T, N, P, M, PI)
print(pos)