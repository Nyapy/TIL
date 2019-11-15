def binarySearch2(a, low, high, key):
    if low > high : #검색실패
        return  False
    else:
        middle = (low + high) // 2
        if key == a[middle]: #검색성공
            return True
        elif key < a[middle]:
            return binarySearch2(a, low, middle-1, key)
        else:
            return binarySearch2(a, middle+1, high, key)


key = 7
#key = 22
data = [2,4,7,9,11,19,23]
print(binarySearch2(data,0, len(data)-1, key))