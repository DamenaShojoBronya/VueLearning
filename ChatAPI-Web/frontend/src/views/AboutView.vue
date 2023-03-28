<template>
ee
</template>

<style scoped>
a {
    text-decoration: none;
    color: #444;
    -webkit-transition: .3s;
    -moz-transition: .3s;
    -ms-transition: .3s;
    -o-transition: .3s;
    transition: .3s;
}
.header {
    position: fixed;
    left: 0;
    top: 5px;
    z-index: 50;
    width: 100%;
    padding: 0 40px;
}
.header:before {
    content: '';
    position: absolute;
    top: -5px;
    left: 0;
    right: 0;
    height: 138px;
    background: url(../assets/bgq1.png) repeat-x;
    -webkit-background-size: auto 100%;
    -moz-background-size: auto 100%;
    -ms-background-size: auto 100%;
    -o-background-size: auto 100%;
    background-size: auto 100%;
}
.header .so {
    float: right;
    width: 251px;
    height: 39px;
    background: url(../assets/new_search.png) no-repeat center center;
    border-radius: 20px;
    padding-right: 70px;
    margin-right: 141px;
    margin-top: 22px;
    position: relative;
    z-index: 2;
    overflow: hidden;
}
.header .navA {
    position: absolute;
    left: auto;
    right: 0;
    top: 0;
    bottom: auto;
    z-index: 2;
    background: url(../assets/iconq1.png) center no-repeat;
    -webkit-background-size: cover;
    -moz-background-size: cover;
    -ms-background-size: cover;
    -o-background-size: cover;
    background-size: cover;
    width: 100px;
    height: 80px;
}
</style>
