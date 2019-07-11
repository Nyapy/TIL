from flask import Flask
import datetime
import random

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/ssafy')
def ssafy():
    return 'This is ssafy!'

@app.route('/dday')
def dday():
    today = datetime.datetime.now()
    endgame = datetime.datetime(2019,11,29)
    td = endgame - today
    return f'SSAFY 1학기 종료까지 {td.days} 일 남았습니다.'

@app.route('/html')
def html():
    return '<h1>이거는 HTML h1 태그다!</h1>'

@app.route('/html_line')
def html_line():
    return """
    <h1>여러줄로 작성해봤어!</h1>
    <ul>
        <li>1번</li>
        <li>2번</li>
    </ul>
    """

@app.route('/greeting/<string:name>')
def greeting(name):
    return f'방가방가! {name}씨!'

@app.route('/cube/<int:number>')
def mua(number):
    return f'{number}의 3제곱은 {number**3}입니당~ 헤헤'

#점심 메뉴 리스트(5개)에서 사람 수 만큼 뽑아 출력하기
# return str(order)
@app.route('/lunch/<int:person>')
def lunch(person):
    menu = ['쇠고기볶음','갈치카레구이','빨간우동','치킨', '떡만두국']
    recom =random.sample(menu,person)
    return str(recom)