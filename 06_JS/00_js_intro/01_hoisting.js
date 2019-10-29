// Hoisting!
// 나중에 선언된 변수를 참조할 수 있음
// 함수 or statement 최상단으로 올려지는 것 (hosting)
//변수와 함수를 위한 메모리를 확보하는 과정

// console.log(a)
// var a = 10
// console.log(a)

// var 가 호이스트 되는 과정
// 1. 선언이 최상단으로 올라감
var a
// 2. 선언이 최상단으로 올라갔기 때문에 에러가 나지 않고 undefined가 출력
//(TMI) JS 에서는 var 변수를 선언할 때 값을 넣어주지 않으면 undeifned를 자동으로 넣어줌
console.log(a)

//3. 할당은 그 뒤에 이루어짐
a= 10
//4. 최종 출력
console.log(a)


//let
console.log(b)
let b = 10
console.log(b)

// let 가 호이스트 되는 과정
// 1. 선언이 최상단으로
let b
// 2. 근데 에러?
console.log(b)
// 3. 할당
b = 10
// 4. 출력
console.log(b)

// var 할당 과정
//1. 선언 - 초기화 (동시에 진행) --> 처음에는 값이 없기 때문에 JS가 undefined를 할당
//2. 값의 할당 진행


// let 할당 과정
//1. 선언 - > 초기화 x
//2. TDZ(Temporal Dead Zone) -> 임시적 사각지대
//3. 초기화 (초기에는 값이 없기 때문에 undefined 할당)
//4. 할당