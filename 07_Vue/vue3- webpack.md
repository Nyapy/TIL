# vue3- webpack

webpack.config.js 설정

src 폴더 만든뒤 안에 main.js 파일 만듬

src에 최상위 컴포넌트 App.vue를 만듬

vue 파일 만들면 template, script, style 태그 3개 항상 만들고 시작 ㄱ

로더랑 컴파일러 설치 ㄱ

```bash
npm install vue-loader vue-template-compiler -D
```

cofing.js 상단에 불러와줘야함

```js
const VueLoaderPlugin = require('vue-loader/lib/plugin')
```

config.js 안에 module이랑 plugins 안에 설정 ㄱ

package.json에 scripts안에 build 설정 ㄱㄱ

bash에서 

```bash
npm run build
```

public 폴더 만든뒤에

index.html 만들기 ㄱ

인덱스 내용 작성하고 고라이브 ㄱ

config에서 mode 작성하고 다시 빌드(npm) ㄱ

src에 components 폴더 생성 ㄱ, 거기에 TodoList.vue 생성 ㄱ



임포트해서 등록한다, 불러온다, 돔에 등록한다.

TodoList.vue 다 만들었으면 최상단 app.vue 가서 위 과정 ㄱ

다시 npm run build로 빌드 ㄱ

그러면 바로 에러남 

```
npm install vue-style-loader css-loader -D
```

이거 해줘야함

그리고 config 가서 다시 등록해야함

rules에 등록 ㄱ

다시 빌드 ㄱㄱㄱㄱㄱㄱㄱㄱㄱㄱㄱㄱㄱ

끝