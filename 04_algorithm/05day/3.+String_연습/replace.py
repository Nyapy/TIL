str1 = "abc 1, 2 ABC"
print(str1)
str1 =str1.replace("1, 2", "one, two")
print(str1)

find = str1.find("one")
print(find)

rst = str1.split(" ")
print(rst)

str = " ".join(rst)
print(str)

print(str1.isalpha())