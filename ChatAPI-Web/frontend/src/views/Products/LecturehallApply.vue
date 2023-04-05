<template>
  <div>
    <el-steps :active="activeStep" finish-status="success">
      <el-step title="提交"></el-step>
      <el-step title="审批中"></el-step>
      <el-step title="已审批"></el-step>
    </el-steps>
    <el-table :data="tableData" style="width: 100%">
      <el-table-column
        prop="Location"
        label="报修地点"
        width="180">
      </el-table-column>
      <el-table-column
        prop="Description"
        label="问题描述"
        width="180">
      </el-table-column>
      <el-table-column
        prop="Reporter"
        label="报修人员"
        width="180">
      </el-table-column>
      <el-table-column
        prop="Phonenum"
        label="联系方式"
        width="180">
      </el-table-column>
      <el-table-column
        label="操作"
        width="120">
        <template #default="{ row }">
          <el-button type="text" @click="approve(row)">批准</el-button>
          <el-button type="text" @click="reject(row)">拒绝</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script lang="ts" setup>
import { defineProps, defineEmits } from 'vue';
import { ref } from 'vue';
// 步骤条
const activeStep = ref(1);

const props = defineProps({
  tableData: Array,
});

const emit = defineEmits<{
  approve: (row: Record<string, any>) => void;
  reject: (row: Record<string, any>) => void;
}>();

const approve = (row: Record<string, any>) => {
  console.log("Approved:", row);
  emit.approve(row);
  // 在这里处理批准操作
};

const reject = (row: Record<string, any>) => {
  console.log("Rejected:", row);
  emit.reject(row);
  // 在这里处理拒绝操作
};
</script>
