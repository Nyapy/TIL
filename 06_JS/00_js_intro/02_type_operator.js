// primitive(원시)타입
/*
const a = 13
const b = -5
const c = 3.15
const d = 2.998e8 //10^8
const e = Infinity
const f = -Infinity
const g = NaN //Not a number

console.log(a, b, c, d, e, f, g)


//string
const sentence1 = 'Ask and go to the blue' //single
const sentence2 = "Ask and go to the blue" //double
const sentence3 = `Ask and go to the blue` //backtick
console.log(sentence1)
console.log(sentence2)
console.log(sentence3)


//따옴표를 사용하면 줊바꿈 불가 -> 빽틱 이용
const word = "안녕
하세요"
console.log(word)

const word = "안녕\n하세요"


const word1 = `안녕
하세요`
console.log(word1)


//백틱 사용 - > 줄바꿈 + 문자열 사이에 변수도 넣을 수 있다.(python의 f`string) 단, 이스케이프 문자열은 사용 불가

const word2 = `안녕
하세요`
console.log(word2)

const age = 10
const message = `홍길동은 ${age}
세 입니다`
console.log(message)


const happy = "will you join us?"
const hacking = 'Happy'+ "Hacking" + '!'
console.log(happy, hacking)


const truthy = true
const falsy = false
console.log(truthy, falsy)
console.log(typeof truthy)
console.log(typeof falsy)


// Empty value
// JS -> null, undefined

let first_name
console.log(first_name) //JS에서 넣어줌

let last_name = null
console.log(last_name) //의도적으로 값이 없음을 명시


console.log(typeof null) //object
console.log(typeof undefined) //undefined

console.log(null == undefined) //동등 비교 연산자 (true)
console.log(null === undefined) // 일치 연산자 (false)

console.log(!null) //true
console.log(!undefined) //true




//할당 연산자
let c = 0

c += 10
console.log(c)

c -= 3
console.log(c)

c += 10
console.log(c)

c++
console.log(c)

c--
console.log(c)



//비교 연산자
console.log(3 > 2)
console.log( 4 <= 2)

console.log('A' < 'Z')

console.log('Z' < 'a')

console.log('가' < '나')


//동등비교 연산자(==) -> 느슨한 평가, 사용을 지양하자
const a = 1
const b = "1"

console.log(a == b)
console.log(a != b)
console.log(a == Number(b))

//자동 형변환 예시
console.log(8*null) //0
console.log("5" -1) // 4(number)
console.log("5" +1) // 51 (string)
console.log('five'*2) //NaN



//일치 연산자 (===) - > 엄격한 평가
const a = 1
const b = "1"
console.log(a ===b) //false
console.log(a === Number(b)) //true



// 논리 연산자
// and
console.log(true && false) //false
console.log(true && true) // true

console.log(1 && 0) //0
console.log( 0 && 1) // 0
console.log( 4 && 7) // 7

//or
console.log(false || ture) //true
console.log(false || false) //false

console.log(1 || 0) //1
console.log(0 || 1) //1
console.log(4 || 7) //4

//not
console.log(!true) //false
console.log(!false) //true

*/

//삼항 연산자
// 가장 앞의 불리언 값이 참이면 :앞의 값이 반환되고 반대일 경우에는 : 뒤의 값이 반환
console.log(true ? 1:2)
console.log(false ? 1:2)
console.log('nyapy' ? 'nice' : 'awesome') //nice

//삼항의 결과를 변수에 할당할 수 있다.
const result = Math.PI > 4 ? "Yep":"Nope"
console.log(result)