#  Web

최초의 웹

http://info.cern.ch/  

최초의 메시지: lo



## Web Service

![1564363969637](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1564363969637.png)

요청의 종류

1. 줘라(Get)

   주소창에 써넣는 거

2. 보내줘(Post)



#### 웹 서비스 개발

서버컴퓨터에서 요청과 응답을 처리할 프로그램을 개발



#### DNS (도네임 네이밍 서비스)

IP  = > 컴퓨터의 주소 == >172.217.27.78  (구글임)

도메인: 네트워크 상의 컴퓨터를 식별하는 호스트명==>  goolge.com 

URL: 도메인 + 경로, 실제로 해당 서버에 저장된 자료의 위치 ==> https://www.goolge.co.kr/search?q=구글





#### Static Web

단순한 서비스 

바닐라 크림 콜드브류 주세요 => 주문하신 아메리카노 나왔습니다.

정해진 것만 할 수 있음

학교 홈페이지, 댓글 기능이 없는 블로그

#### Dynamic Web

Web Application program (web APP)

접속해야할 때마다 변해야 할 필요가 있는 사이트



#### Web page

W3C - 웹 표준



###### HTML( Hyper Text Markup language) 

Hyper Text : 순서대로 글을 읽는 것이 아닌 링크를 타고 이동

Markup : 역할을 부여(하이라이팅 )

=> 웹페이지를 작성하기 위한 역할 표시 언어



HTTP(Hyper Text Transfer Protocol) 하이퍼 텍스트를 주고 받는 규약임



HTTP 문서 기본 구조

- DOCTYPE 선언
- html  요소
- head 요소
- body 요소



###### CSS(Cascading Style Sheet) 

예쁘게 꾸며줌.



###### JS(JavaScript)

활기를 넣어준다는데 뭐하는거람





### HTML 파일 만들어보기

```html
<!DOCTYPE html> #DOCTYPE 선언
<html lang="ko"> 
    <head># 헤드치고 탭누르면 알아서 꺽쇠 달아줌
        <meta charset= "UTF-8">
        <title>Hello World</title>
    </head>
    <body>
        <!--이것은 주석입니다. 화면에 나오지 않아요.-->
        <h1>Hi, There! Introduce Nyapy!</h1>
        <h2>My favorite food is pizza</h2>
    </head>
</html>
```

![1564370350984](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1564370350984.png)

```html
<!--이것은 주석입니다. 화면에 나오지 않아요.-->
```



#### 요소(Element)

```html
<h1>contents</h1>
```

여는태그 + 내용 + 닫는태그

```html
<img src="url"/>
```

얘는 닫는 태그가 없음. 지 혼자 닫음.



#### 속성(Attribute)

```html
<a href="google.com">
```

태그는 속성이 지정될 수 있다.

= 사이에 띄우면 안됨

id, class, style  태그는 모든 속성에 사용 가능하다.

id : 유일한 식별자(중복 지정 불가)

class : 스타일시트에 정의된 class를 요소에 지정(중복지정 가능)

style : 인라인 스타일 지정



#### DOM트리

![1564370754417](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1564370754417.png)

이런 구조

태그는 중첩되어 사용 가능하며, 이 때 위와 같은 관계를 갖는다.



#### 시멘틱태그

컨텐츠의 의미를 설명하는 태그,

html5에 새롭게 추가된 시맨틱 태그

```html
<div>이거슨 공간 </div>
```

하지만 공간 자체에 대한 어떤 의미도 없음.

그럼 왜 씀?

개발자가 의도한 요소의 의미가 명확히 보임. 코드의 가독성을 높이고 유지보수가 쉽다.

웹에 존재하는 수많은 웹페이지들에 메타데이터를 부여하여 기존 잡다한 데이터에 의미를  갖게 함.

 SEO(serch engine optimization): 웹 페이지 검색 엔진이 자료를 수집하고 순위를 매기는 방식에 맞게 웹페이지를 구성해 검색 결과의 상위에 노출될 수 있게 함.



```html
<!DOCTYPE html>
<head>
    <meta charset = "UTF-8">
    <title>Semantic Layout</title>
    <style type="text/css">
        * {
            font-family: 'Source Code Pro', sans-serif;
        }

        nav,
        header,
        section,
        article,
        aside,
        footer {
            margin: 16px;
            padding: 16px;
            border-radius: 4px;
            background-color: purple;
            text-align: center;
        }

        nav,
        header,
        footer {
            width: 400px;
        }

        header {
            margin-bottom: 0;
        }

        footer {
            margin-top: 0;
        }

        section {
            display: inline-block;
            width: 216px;
            height: 100px;
            margin-right: 8px;
        }

        aside {
            display: inline-block;
            width: 136px;
            height: 100px;
            margin-left: 0px;
            vertical-align: top;
        }

        article {
            background-color: grey;
        }
    </style>
</head>
<body>
    <header>
        &lt;heder&gt;
    </header>
    <nav>
        &lt;nav&gt;
    </nav>
    <section>
            &lt;section&gt;
    </section>
    <aside>
            &lt;aside&gt;
    </aside>
    <footer>
            &lt;footer&gt;
    </footer>
</body>
```





레이아웃 태그 - non-semantic 태그

링크태그 

```html
<a href ="google.com"/
```



미디어태그



