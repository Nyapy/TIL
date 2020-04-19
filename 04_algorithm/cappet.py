brown = 10
red = 2

de = (4+brown)**2-(4*2)*(2*red+2*brown)

a = de**(0.5)/4

aa = (4+brown)/4

garo = a+aa
sero = aa-a
ans = [garo,sero]

print(list(map(int, ans)))
