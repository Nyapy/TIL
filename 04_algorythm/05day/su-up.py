def my_strev(ary):
    str = list(ary)
    for i in range(len(str)//2):
        t = ary[i]
        str[i] = str[len(str)-1-i]
        str[len(ary) -1 - i] = t
    ary = "".join(str)
    return ary

ary = 'abcde'
ary = my_strev(ary)
print(ary)

s = 'Reverse this strings'
s = s[::-1]
print(s)