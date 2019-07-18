# def is_palindrom(word):
#     if word == word[::-1]:
#         return True
#     else:
#         return False



# print(is_palindrom('level'))
# print(is_palindrom('가져가라 가져가'))

# def is_palindrom(word):
#     list_word = list(word)
#     for i in range(len(list_word) //2):
#         if list_word[i] != list_word[-i-1]:
#             return False
#     return True

# print(is_palindrom('가자미'))

# print(dir(__builtins__))

def ssafy(name, location = '서울') :
    print(f'{name}의 지역은 {location}입니다')

ssafy('허준' )
