def itoa(x):
    itoa_li = []
    while x%10 > 0 :
        val = x % 10
        itoa_li += '{}'.format(val)
        x = x//10

    itoa_li = itoa_li[::-1]
    return ''.join(itoa_li)

x = 123
print(x, type(x))
str1 = itoa(x)
print(str1, type(str1))