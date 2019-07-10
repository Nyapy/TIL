'''
문제1.문자열을 입력받아 문자열의 첫 글자와 마지막 글자를 출력하는 프로그램을 만드세요
'''

# str = input('문자를 입력하세요: ')

# print(f'첫글자는 {str[0]}')
# print(f'마지막 글자는 {str[-1]}')

'''
문제2. 자연수 n이 주어질 때, 1부터 n까지 한 줄에 하나씩 출력하는 프로그램을 만드세요.
# '''
# a = int(input('숫자를 입력하세요: '))

# for i in range(1,a+1):
#     print(f'{i}')

'''
문제3. 숫자를 입력 받아 짝수/홀수를 구분하는 코드를 작성하세요.
'''

# number = int(input('숫자를 입력하세요 :'))

# if number %2 == 1 :
#     print('홀수입니다.')
    
# else :
#     print('짝수입니다.')

'''
문제 4. 표준 입력으로 국어, 영어, 수학, 과학 점수가 입력됩니다.
국어는 90점 이상,
영어는 80점 초과,
수학은 85점 초과,
과학은 80점 이상일 때 합격이라고 정했습니다.
(한 과목이라도 조건에 만족하지 않으면 불합격)
다음 코드를 완성하여 합격이면 True, 불합격이면 False가 출력되도록 작성하세요
'''
# a = int(input('국어:'))
# b = int(input('영어:'))
# c = int(input('수학:'))
# d = int(input('과학:'))
# if a>=90 and b>80 and c>85 and d>=80:
#     print('합격',end='')
# else:
#     print('불합격')

'''
문제5. 표준 입력으로 물품 가격 여러 개가 문자열 한 줄로 입력되고, 각 가격은 ;으로 구분되어 있습니다. 입력된 가격을 높은 가격순으로 한줄에 하나씩 출력하는 프로그램을 만드세요
입력예시: 30000;2000;40000
출력예시
40000
30000
2000
'''



prices = input('물품 가격을 입력하세요:')

makes = prices.split(';')
boxs = []
#print(makes)

for make in makes:
    boxs.append(int(make))

boxs.sort(reverse=True)

for box in boxs:
    print(box)