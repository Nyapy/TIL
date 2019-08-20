N = 100

for i in range(1,N+1):
    a = str(i)
    count = 0
    for j in a:
        if j == '3' or j =='6' or j =='9' :
            count += 1

    if count == 0:
        print(i, end = ' ')
    else :
        print('-'*count, end = ' ')