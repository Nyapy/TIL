# Vue Youtube project

```html
<template>
  <div>
    <input @input="Input" type="text">
    <a href="{{ data.aurl }}">GO!</a>
  </div>
</template>

<script>
export default {
  name : 'urlbox',
  data : {
    aurl : ''
  },
  methods: {
    Input(a) {
      this.data.aurl = a.target.value      
    }
  }

}
</script>

<style>

</style>
```