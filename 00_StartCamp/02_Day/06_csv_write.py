lunch  = {
    '양자강' : '02-557-4211',
    '김밥카페': '02-553-3181',
    '순남시레기': '02-508-0887'
}

#1. 방법 1
#tuple() 튜플 형태로 나옴 ('양자강, 02어쩌구')
with open('lunch.csv', 'w' , encoding = 'utf-8') as f:
     #한글 깨짐을 막기 위해 인코딩 인자를 넣어줌
    for item in lunch.items():
        f.write(f'{item[0]}, {item[1]}\n')