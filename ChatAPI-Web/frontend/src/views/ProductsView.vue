<template>
    <view-box>

        <div class="common-layout">
            <el-container>

                <el-aside width="200px">
                    <el-radio-group v-model="isCollapse" style="margin-bottom: 20px">
                        <el-radio-button :label="false">expand</el-radio-button>
                        <el-radio-button :label="true">collapse</el-radio-button>
                    </el-radio-group>
                    <el-menu default-active="1" class="el-menu-vertical-demo" :collapse="isCollapse" @open="handleOpen"
                        @close="handleClose" @select="handleSelect">
                        <!-- 首页 -->
                        <el-menu-item index="1">
                            <el-icon>
                                <Location />
                            </el-icon>
                            <template #title>首页</template>
                        </el-menu-item>
                        <!-- 设备报修 -->
                        <el-menu-item index="2">
                            <el-icon><Icon-menu /></el-icon>
                            <template #title>设备报修</template>
                        </el-menu-item>
                        <!-- 维修指派 -->
                        <el-menu-item index="3">
                            <el-icon>
                                <Document />
                            </el-icon>
                            <template #title>维修指派</template>
                        </el-menu-item>
                        <!-- 报告厅申请 -->
                        <el-menu-item index="4">
                            <el-icon>
                                <Setting />
                            </el-icon>
                            <template #title>报告厅申请</template>
                        </el-menu-item>
                    </el-menu>
                </el-aside>

                <el-main>
                    <!-- 首页内容 -->
                    <el-card class="box-card" v-if="activeIndex === '1'">
                        <template #header>
                            <div class="card-header">
                                <span>Card name</span>
                            </div>
                        </template>

                        <el-table :data="tableData" style="width: 100%" max-height="450">
                            <el-table-column fixed prop="报修编号" label="Num" width="100" />
                            <el-table-column prop="报修时间" label="Date" width="120" />
                            <el-table-column prop="报修地点" label="Address" width="120" />
                            <el-table-column prop="问题描述" label="Bug" width="120" />
                            <el-table-column prop="报修人员" label="contac" width="120" />
                            <el-table-column prop="联系方式" label="Phonenum" width="120" />
                            <el-table-column prop="处理方法" label="Approach" width="120" />
                            <el-table-column prop="出勤人员" label="stuff" width="120" />
                            <el-table-column prop="维修耗材" label="Consumables" width="120" />
                            <el-table-column fixed="right" label="Operations" width="120">
                                <template #default>
                                    <el-button link type="primary" size="small" @click="handleClick">Detail</el-button>
                                    <el-button link type="primary" size="small">Edit</el-button>
                                </template>
                            </el-table-column>
                        </el-table>

                    </el-card>
                    <el-card class="box-card" v-if="activeIndex === '2'">
                        <!-- 设备报修内容 -->
                    </el-card>

                    <el-card class="box-card" v-if="activeIndex === '3'">
                        <!-- 维修指派内容 -->
                    </el-card>

                    <el-card class="box-card" v-if="activeIndex === '4'">
                        <!-- 报告厅申请内容 -->
                    </el-card>
                </el-main>

            </el-container>
        </div>

    </view-box>
</template>

<style scoped>
aside.el-aside {
    background: aliceblue;
}

view-box {
    margin: 0 auto;
    width: 100%;
    height: auto;
    margin-top: 150px;
    display: flex;
    justify-content: space-around
}

.card-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.el-menu-vertical-demo:not(.el-menu--collapse) {
    width: 200px;
    min-height: 400px;
}
</style>

<script lang="ts" setup>
import { ref } from 'vue'
import {
    Document,
    Menu as IconMenu,
    Location,
    Setting,
} from '@element-plus/icons-vue'
// elementplus组件
const isCollapse = ref(true)
const handleOpen = (key: string, keyPath: string[]) => {
    console.log(key, keyPath)
}
const handleClose = (key: string, keyPath: string[]) => {
    console.log(key, keyPath)
}
const handleClick = () => {
    console.log('click')
}

const tableData = [
    {
        报修编号: 'SBBX-asgdas78faif',
        报修时间: '2023-2-19',
        报修地点: '综合楼300',
        问题描述: '办公室需要布网，电脑需要重装系统',
        报修人员: '刘老师',
        联系方式: '18123123125',
        处理方法: '更换网线、系统重装',
        出勤人员: '大黄，张sir',
        维修耗材: '一箱网线',
    },
    {
        报修编号: 'SBBX-asgdas78faif',
        报修时间: '2023-2-19',
        报修地点: '综合楼300',
        问题描述: '办公室需要布网，电脑需要重装系统',
        报修人员: '刘老师',
        联系方式: '18123123125',
        处理方法: '更换网线、系统重装',
        出勤人员: '大黄，张sir',
        维修耗材: '一箱网线',
    },
    {
        报修编号: 'SBBX-asgdas78faif',
        报修时间: '2023-2-19',
        报修地点: '综合楼300',
        问题描述: '办公室需要布网，电脑需要重装系统',
        报修人员: '刘老师',
        联系方式: '18123123125',
        处理方法: '更换网线、系统重装',
        出勤人员: '大黄，张sir',
        维修耗材: '一箱网线',
    },
    {
        报修编号: 'SBBX-asgdas78faif',
        报修时间: '2023-2-19',
        报修地点: '综合楼300',
        问题描述: '办公室需要布网，电脑需要重装系统',
        报修人员: '刘老师',
        联系方式: '18123123125',
        处理方法: '更换网线、系统重装',
        出勤人员: '大黄，张sir',
        维修耗材: '一箱网线',
    },
]
const activeIndex = ref('1') // 添加 activeIndex 变量，默认设置为 '1'
const handleSelect = (index: string) => {  // 添加 handleSelect 方法
    activeIndex.value = index
}
</script>

<script lang="ts">
export default {
    name: 'DeviceAndAttendance',
    data() {
        return {
        };
    },
    methods: {

    },
};
</script>
