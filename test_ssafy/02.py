def alphabet_count(word):
    # result = {}

    # for char in word:
    #     if result.get(char): #if char in result
    #         result[char] += 1
    #     else:
    #         result[char] = 1

    # return result


    return {char: word.count(char) for char in word}



if __name__ == '__main__':
    print(alphabet_count('hello'))
    print(alphabet_count('internationalization'))
    print(alphabet_count('haha'))
