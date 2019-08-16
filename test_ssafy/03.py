def summary(word):
    result = []
    tmp_list = []

    for char in word:
        if tmp_list and tmp_list[-1] != char:
            result.append(tmp_list[-1])
            result.append(f'{len(tmp_list)}')
            tmp_list.clear()
        tmp_list.append(char)

    result.append(tmp_list[-1])
    result.append(f'{len(tmp_list)}')
    
    return ''.join(result)




if __name__ == '__main__':
    print(summary('aabbaacc'))
    print(summary('ffgggeeeef'))
    print(summary('abcdefg'))