# Web2

## 스타일 바꾸기

```html
<li style="list-style: upper-alpha">int</li>
<li style="list-style: lower-greek">float</li>
<li style="list-style: upper-latin">complex</li>
<li><del>complex</del> </li>

<ul>
    <li style="list-style: square">HTML</li>
    <li style="list-style: square">CSS</li>
</ul>
```

![1564445557160](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1564445557160.png)

바뀐걸 확인 가능하다.



## 링크

a tab하면 태그 완성

```html
<a href="https://docs.python.org/3/" target="_blank"> <h2>파이썬</h2></a>        
```

뒤에 taget="_blank" 는 새탭에서 열리게 하는 기능



#### 같은 폴더내 html 파일로 링크 걸기

```html
<a href="index.html">[참고 사이트]</a>
```

주소부분에 #을 넣으면 아무것도 안일어나게 할 수 있음



## 미디어 띄우기

```html
<img src="" alt=""> </a>
```

img치고 tab 누르면 태그 완성해줌



```html
<a href="https://docs.python.org/3/" target="_blank"> <img src="images/python.jpg" alt="Python logo" width="50px" height= "50px"> </a>
```

width="50px" height= "50px" 를 뒤에 붙이면 크기 조절이 됨.



src에 있는 이미지를 불러올 수 없을 경우 alt에 있는 글을 대신 나타냄



#### 동영상 

```html
<iframe width="1252" height="704" src="https://www.youtube.com/embed/cJB6iYckbSQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

소스코드를 복사해서 붙여넣기 하면 알아서 iframe 태그를 완성해줌





#### 표만들기

```html
<table  border = "1px solid black">
    <tr>
        <th></th> 
        <th>월</th>
        <th>화</th>
        <th>수</th>
        </th>
    </tr>

    <tr>
        <td> A 코스</td>
        <td rowspan="2">짬뽕</td>
        <td colspan="2">초밥</td>
    </tr>

    <tr>
        <td> B 코스</td>
        <td> 김치찌개</td>
        <td> 삼계탕</td>
    </tr>
</table>
```

tr: 테이블 로우 : 표의 행

th: 테이블 헤드 : 테이블의 제목 진하게 표시됨

td : 테이블 데이터

rowspan : 행을 2줄로 늘림

colspan : 열을 2줄 사용



![1564447774177](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1564447774177.png)

```html
<style>
        td{
            border : 1px solid darkgray
        }
</style>
```

헤드에서 스타일 설정할 때 위랑 같이 해두면 테이블데이터에만 됨



```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Music TimeTable</title>
    <style>
        td{
            border : 1px solid darkgray
        }
    </style>
</head>
<body>
    <h1>2019년 타임테이블</h1>
    <table>
        <tr>
            <th>TIME</th>
            <th>INDOOR</th>
            <th colspan="2">OUTDOOR</th>
        </tr>

        <tr>
            <td></td>
            <td>소극장</td>
            <td>잔디마당</td>
            <td>대공연장</td>
        </tr>

        <tr>
            <td>10:00</td>
            <td rowspan="2">안녕하신가영</td>
            <td></td>
            <td>10CM</td>
        </tr>

        <tr>
            <td>13:00</td>
            <td rowspan="2">선우정아</td>
            <td rowspan="2">참깨와 솜사탕</td>
        </tr>

        <tr>
            <td>15:00</td>
            <td></td>
        </tr>
        
        <tr>
            <td>17:00</td>
            <td>크러쉬</td>
            <td></td>
            <td>폴킴</td>
        </tr>
    </table>
    
</body>
</html>
```







## 폼 만들기

```html
<form action=""></form>
```

폼탭

```html
<form action="">
        TEXT: <input type="text" placeholder="내용을 입력해주세요"> <br>
        NUMBER: <input type="number"><br>
        PASSWORD: <input type="password"><br>
        EMAIL: <input type="email"><br>
        DATE: <input type="date"><br>

        <input type="radio" name = "language">HTML<br>
        <input type="radio" name = "language">CSS<br>
        <input type="radio" name = "language">JS<br>

        <select name="contry" id="">
            <option value="한국" selected>한국</option>
            <option value="중국">중국</option>
            <option value="일본" disabled>일본</option>
        </select><br>

        한국: <input type="checkbox">
        일본: <input type="checkbox"><br>
        <input type="submit" value = "제출하세요.">
    </form>  
```

![1564451312514](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1564451312514.png)



#### 입력칸 만들기

```html
<input type="text">
```

placeholder = "" 를 붙이면 입력하기 전에 "" 안의 내용이 보임

Type을 입력하는 타입에 맞춰 지정해주면 입력칸이 알아서 잘 바꿔줌



#### 라디오박스 만들기

```html
<input type="radio" name = "a" value="1">
```

인풋 태그에서 type을 radio로 바꾸면 나옴, value를 입력하면 전송했을때 그 값이 넘어감

뒤에 disabled 붙이면 선택 불가능하게 됨



#### 셀렉트칸 만들기

```php+HTML
<select name="" id="">
    <option value="한국" selected>한국</option>
</select>
```



#### 체크박스

````html
<input type="checkbox">
````

#### 제출버튼

```html
<input type="submit" value = "제출하세요.">
```









## CSS



기본사용

```css
h1{color: bluse; font_size: 15px}
```

h1 : 셀렉터  { 기본 선언: 선언}

활용하는 방법 3가지



CSS 활용하기

 1. Inline(인라인)

HTML 요소의 style에 CSS 넣기

별로 안좋은 방식임.



2. Embedding(내부참조)

HTML 내부에 삽입



3. Link(외부참조)

외부의 CSS파일을 로드하기





### 폰트





### 위치 (position)



1. static(기본위치)



2. relative(상대위치)

복잡함. 공간은 차지하고 위치만 이동

3. absolute(절대위치)

   참조할 부모가 없으면 Body 에 붙는다.



4. fixed(고정위치)

화면 기준, 스크롤 땡겨도 거기 있음





#### 선택

element:nth-child(n)

자식태그들 중 n번째 요소를 찾아  n번째 요소가 element 인 경우 변환



element:nth-of-type(n)

자식 중에 n반째 element를 찾아 변환