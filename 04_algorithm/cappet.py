brown = 24
yellow = 24

def cappet():
    de = (4+brown)**2-(4*2)*(2*yellow+2*brown)
    a = de**(0.5)/4
    aa = (4+brown)/4
    garo = a+aa
    sero = aa-a
    answer = [garo,sero]
    return list(map(int, answer))


def cappet2():
    cap = brown + yellow
    for i in range(3,cap//3+1):
        for j in range(i, cap//i+1):
            if i*j == cap:
                if (i-2)*(j-2)==yellow:
                    answer = [j,i]
                    return answer

print(cappet(),cappet2())
