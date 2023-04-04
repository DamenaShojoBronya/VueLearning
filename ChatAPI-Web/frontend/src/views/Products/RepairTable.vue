<template>
  <el-table :data="tableData" style="width: 100%" class="table-with-fixed-height">
    <el-table-column fixed prop="Num" label="报修编号" />
    <el-table-column prop="Date" label="报修时间" />
    <el-table-column prop="Location" label="报修地点" />
    <el-table-column prop="Description" label="问题描述" />
    <el-table-column prop="Reporter" label="报修人员" />
    <el-table-column prop="Phonenum" label="联系方式" />
    <el-table-column prop="Solution" label="处理方法" />
    <el-table-column prop="Stuff" label="出勤人员" />
    <el-table-column prop="Consumables" label="维修耗材" />
    <el-table-column fixed="right" label="Operations">
      <template #default>
        <el-button link type="primary" size="small" @click="handleClick">Detail</el-button>
        <el-button link type="primary" size="small">Edit</el-button>
      </template>
    </el-table-column>
  </el-table>
</template>
  
<script lang="ts">
import { ref, onMounted } from 'vue';
import apiClient from "../apiClient";

interface Repair {
  Num?: string;
  Date?: string;
  Location: string;
  Description: string;
  Reporter: string;
  Phonenum: string;
  Solution?: string;
  Stuff?: string;
  Consumables?: string;
}

export default {
  name: 'RepairTable',
  setup() {
    const handleClick = () => {
      console.log('click');
    };

    const tableData = ref<Repair[]>([]);

    const fetchRepairs = async () => {
      try {
        const response = await apiClient.get('/api/repairs');
        tableData.value = response.data;
      } catch (error) {
        console.error('Failed to fetch repairs:', error);
      }
    };

    onMounted(fetchRepairs);

    return {
      handleClick,
      tableData,
    };
  },
};
</script>

  