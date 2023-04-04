<template>
    <el-table :data="tableData" style="width: 100%" class="table-with-fixed-height">
      <el-table-column fixed prop="Num" label="报修编号" width="120" />
      <el-table-column prop="Date" label="报修时间" width="120" />
      <el-table-column prop="Location" label="报修地点" width="100" />
      <el-table-column prop="Bug" label="问题描述" width="120" />
      <el-table-column prop="Contact" label="报修人员" width="100" />
      <el-table-column prop="Phonenum" label="联系方式" width="120" />
      <el-table-column prop="Solution" label="处理方法" width="120" />
      <el-table-column prop="Stuff" label="出勤人员" width="120" />
      <el-table-column prop="Consumables" label="维修耗材" width="120" />
      <el-table-column fixed="right" label="Operations" width="120">
        <template #default>
          <el-button link type="primary" size="small" @click="handleClick">Detail</el-button>
          <el-button link type="primary" size="small">Edit</el-button>
        </template>
      </el-table-column>
    </el-table>
  </template>
  
  <script lang="ts">
  export default {
    name: 'DeviceRepairListTable',
    setup() {
      const handleClick = () => {
        console.log('click')
      }
  
      const tableData = Array.from({ length: 7 }, () => ({
        Num: 'SBBX-asgdas78faif',
        Date: '2023-2-19',
        Location: '综合楼300',
        Bug: '办公室需要布网，电脑需要重装系统',
        Contact: '刘老师',
        Phonenum: '18823123125',
        Solution: '更换网线、系统重装',
        Stuff: '大黄，张sir',
        Consumables: '一箱网线',
      }))
  
      return {
        handleClick,
        tableData,
      }
    },
  }
  </script>
  