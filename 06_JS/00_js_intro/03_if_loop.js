// IF문
//swich
/*
const fruit = "Papayas"

switch(fruit) {
  case 'Oranges': {
    console.log('Oranges are 40000 won.')
    break
  }
  case 'Mangoes':{
    console.log('Mangoes are 40000 won.')
    break
  }
  case 'Papayas':{
    console.log('Papayas are 40000 won.')
    break
  }
  default:{
    console.log("Hi")
  }
}


let i = 0

while( i < 6){
  console.log(i)
  i++
}

//for loop
//for 문 내에서 사용하는 변수 j가 false가 되면 반복 중지

for (let j = 0; j < 6; j++){
  console.log(j)
}

*/

//for of

const numbers = [0, 1, 2, 3, 4, 5]

// let 재할당 잇음
for (let number of numbers) {
  console.log(number)
}
for (let number of [0, 1, 2, 3, 4, 5]) {
  console.log(number)
}

//재할당 없음
for (const number of [0, 1, 2, 3, 4, 5]){
  console.log(number)
}