<template>
    <header :class="{ 'blur-background': blur }">
        <div class="header">
            <!-- 左侧logo -->
            <div class="logo">
                <h2>科学创新协会</h2>
            </div>
            <!-- 主菜单 -->
            <div class="header-menu" :class="{ 'header-menu-change-search': isChangeSearch }">
                <router-link active-class="active" to="/home">首页</router-link>
                <router-link active-class="active" to="/about">关于我们</router-link>
                <router-link active-class="active" to="/activities">活动回顾</router-link>
                <router-link active-class="active" to="/achievements">成果展示</router-link>

                <el-dropdown class="header-menu-dropdown">

                    <span class="el-dropdown-link">
                        <router-link active-class="active" to="/home">
                            产品
                            <el-icon class="el-icon--right">
                                <arrow-down />
                            </el-icon>
                        </router-link>

                    </span>
                    <template #dropdown>
                        <el-dropdown-menu>
                            <el-dropdown-item>
                                <router-link class="link" to="/translate">中文翻译</router-link>
                            </el-dropdown-item>
                            <el-dropdown-item>
                                <router-link class="link" to="/rewrite">文风转换</router-link>
                            </el-dropdown-item>
                            <el-dropdown-item>
                                <router-link class="link" to="/code2txt">代码翻译</router-link>
                            </el-dropdown-item>
                            <el-dropdown-item>
                                <router-link class="link" to="/xiaohongshuGenerator">小红书生成器</router-link>
                            </el-dropdown-item>
                            <el-dropdown-item divided>翻译</el-dropdown-item>
                        </el-dropdown-menu>
                    </template>
                </el-dropdown>


            </div>
            <!-- 搜索框 -->
            <div class="search-bar" :class="{ 'search-bar-change-search': isChangeSearch }">
                <input type="text" @focusin="changeStyle" @focusout="changeStyle" placeholder="请输入关键字">

            </div>
            <!-- 头像区域 -->
            <div class="header-profile">
                <div class="notification">
                    <span class="notification-number">9</span>
                    <svg viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg" data-v-029747aa="">
                        <path fill="currentColor"
                            d="M384 960v-64h192.064v64H384zm448-544a350.656 350.656 0 0 1-128.32 271.424C665.344 719.04 640 763.776 640 813.504V832H320v-14.336c0-48-19.392-95.36-57.216-124.992a351.552 351.552 0 0 1-128.448-344.256c25.344-136.448 133.888-248.128 269.76-276.48A352.384 352.384 0 0 1 832 416zm-544 32c0-132.288 75.904-224 192-224v-64c-154.432 0-256 122.752-256 288h64z">
                        </path>
                    </svg>
                </div>
                <svg viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg" data-v-029747aa="">
                    <path fill="currentColor"
                        d="M764.416 254.72a351.68 351.68 0 0 1 86.336 149.184H960v192.064H850.752a351.68 351.68 0 0 1-86.336 149.312l54.72 94.72-166.272 96-54.592-94.72a352.64 352.64 0 0 1-172.48 0L371.136 936l-166.272-96 54.72-94.72a351.68 351.68 0 0 1-86.336-149.312H64v-192h109.248a351.68 351.68 0 0 1 86.336-149.312L204.8 160l166.208-96h.192l54.656 94.592a352.64 352.64 0 0 1 172.48 0L652.8 64h.128L819.2 160l-54.72 94.72zM704 499.968a192 192 0 1 0-384 0 192 192 0 0 0 384 0z">
                    </path>
                </svg>
                <img class="profile-img" src="../assets/profile.png" alt="">
            </div>
        </div>
    </header>
</template>



<script>
//引入icon
import { ArrowDown } from '@element-plus/icons-vue'
import { mapGetters } from 'vuex';
export default {
    name: 'ElementplusIcon',
    components: {
        ArrowDown
    },

    data() {
        return {
            isChangeSearch: false
        }
    },
    methods: {
        toggleBlur() {
            this.$store.commit('SET_BLUR', true);
        }
    },
    computed: {
    ...mapGetters(['blur'])
    }
}
</script>

<style lang="scss" scoped>

.header-menu-dropdown .el-dropdown-link {
    cursor: pointer;
    display: flex;
    align-items: center;
}

.el-icon--right {
    position: absolute;
}

.link {
    display: flex;
    align-items: center;
    white-space: nowrap;
    list-style: none;
    padding: 5px 16px;
    position: relative;
    padding: 5px 0;
    line-height: 20px;
    min-width: 10px;
    text-decoration: none;
    cursor: pointer;
    list-style: none;
    font-size: var(--el-font-size-base);
    color: var(--el-text-color-regular);
    --el-scrollbar-opacity: 0.3;
    --el-scrollbar-bg-color: var(--el-text-color-secondary);
    --el-scrollbar-hover-opacity: 0.5;
}

.el-dropdown-menu__item:hover .link {
    color: #409eff;
    /* 自定义的字体颜色 */
}

.header {
    // background-color: skyblue;
    background: -webkit-linear-gradient(left, rgb(145, 217, 246) 0%, #db6ff3 100%);
    display: flex;
    align-items: center;
    flex-shrink: 0;
    height: 58px;
    width: 100%;
    border-bottom: 1px solid RGBA(113 119 144 / 25%);
    padding: 0 30px;
    white-space: nowrap;

    @media screen and (max-width: 480px) {
        padding: 0 16px;
    }

    .logo {
        width: 96px;
        height: 30px;
        margin-right: 110px;
        flex-shrink: 0;
        display: flex;
        flex-direction: row;
        align-items: center;

        @media screen and (max-width: 945px) {
            display: none;
        }

        h2 {
            background-image: linear-gradient(#dc81f1, #db6ff3);
            background-clip: text;
            -webkit-background-clip: text;
            color: transparent;
        }

        svg {
            //fill:currentColor;
            fill: #db6ff3;
        }

    }

    /* .head-menu */
    &-menu,
    .header-menu-dropdown,
    .dropdown-item {
        display: flex;
        align-items: center;

        a {
            padding: 20px 30px;
            text-decoration: none;
            color: rgb(60, 62, 70);
            border-bottom: 2px solid transparent;
            transition: 0.3s;

            @media screen and (max-width: 610px) {
                &:not(.main-header-link) {
                    display: none;
                }
            }

        }

        a:hover,
        a.active {
            color: #ffffff;
            border-bottom: 2px solid #ffffff;
        }

    }

    .notify {
        position: relative;

        &:before {
            content: "";
            position: absolute;
            background-color: #3a6df0;
            width: 6px;
            height: 6px;
            border-radius: 50%;
            right: 20px;
            top: 16px;
        }

        @media screen and (max-width: 1055px) {
            display: none;
        }
    }

    .search-bar {
        height: 40px;
        display: flex;
        width: 100%;
        max-width: 400px;
        padding-left: 16px;
        border-radius: 4px;
        border: none;

        input {
            width: 100%;
            height: 100%;
            border: none;
            outline: none;
            background-color: #b7bbea;
            background-color: white;
            border-radius: 4px;
            font-family: "Poppins", sans-serif;
            font-size: 15px;
            font-weight: 500;
            padding: 0 20px 0 40px;
            //box-shadow: 0 0 0 2px rgb(134 140 160 / 0%);
            background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 56.966 56.966' fill='%23717790c7'%3e%3cpath d='M55.146 51.887L41.588 37.786A22.926 22.926 0 0046.984 23c0-12.682-10.318-23-23-23s-23 10.318-23 23 10.318 23 23 23c4.761 0 9.298-1.436 13.177-4.162l13.661 14.208c.571.593 1.339.92 2.162.92.779 0 1.518-.297 2.079-.837a3.004 3.004 0 00.083-4.242zM23.984 6c9.374 0 17 7.626 17 17s-7.626 17-17 17-17-7.626-17-17 7.626-17 17-17z'/%3e%3c/svg%3e");
            background-size: 14px;
            background-repeat: no-repeat;
            background-position: 16px 48%;

            //color: #212324;
            &::placeholder {
                font-family: "Poppins", sans-serif;
                color: rgb(131, 131, 237);
                font-size: 15px;
                font-weight: 500;
            }
        }

        input:focus {
            border: 2px solid rgb(192, 134, 192);
        }

    }

    .header-profile {
        display: flex;
        align-items: center;
        //text-align: center;
        padding: 0 16px 0 40px;
        margin-left: auto;
        flex-shrink: 0;

        svg {
            width: 22px;
            color: #f9fafb;
            flex-shrink: 0;
        }

        .notification {
            position: relative;
            top: 2px;

            &-number {
                position: absolute;
                background-color: #3a6df0;
                width: 16px;
                height: 16px;
                border-radius: 50%;
                font-size: 10px;
                display: flex;
                align-items: center;
                justify-content: center;
                color: #fff;
                right: -6px;
                top: -6px;
            }

            &+svg {
                margin-left: 22px;

                @media screen and (max-width: 945px) {
                    display: none;
                }
            }
        }

        .profile-img {
            width: 32px;
            height: 32px;
            border-radius: 50%;
            object-fit: cover;
            border: 2px solid #f9fafb;
            margin-left: 22px;
        }
    }

    /*输入框聚焦后，样式改变 */

    .header-menu-change-search {
        display: none;
    }

    .search-bar-change-search {
        max-width: 600px;
        margin: auto;
        transition: 0.4s;
        box-shadow: 0 0 0 1px RGBA(113 119 144 / 25%);
        padding-left: 0;
    }


    .change-search {

        .header-menu,
        .header-profile {
            display: none;
        }

        .search-bar {
            max-width: 600px;
            margin: auto;
            transition: 0.4s;
            box-shadow: 0 0 0 1px RGBA(113 119 144 / 25%);
            padding-left: 0;
        }

        .logo {
            margin-right: 0;
        }
    }
}
.blur-background {
  filter: blur(4px);
}
</style>