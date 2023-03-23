<template>
  <footer>
    <p>© 2023 科学创新协会. 版权所有。</p>
    <p>联系我们：contact@sciinnov.org</p>
  </footer>
</template>

<script>
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'PageFooter'
});
</script>

<style>
footer {
  margin-top: 50px;
  padding: 20px;
  background-color: #f2f2f2;
  font-size: 14px;
  text-align: center;
}

footer p {
  margin: 5px;
}
</style>
