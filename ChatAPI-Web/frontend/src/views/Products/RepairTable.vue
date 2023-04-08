<template>
  <el-table :data="tableData" style="width: 100%" class="table-with-fixed-height" @row-click="handleRowClick">
    <el-table-column fixed prop="Num" label="报修编号" />
    <el-table-column prop="Date" label="报修时间" />
    <el-table-column prop="Location" label="报修地点" />
    <el-table-column prop="Description" label="问题描述" />
    <el-table-column prop="Reporter" label="报修人员" />
    <el-table-column prop="Phonenum" label="联系方式" />
    <el-table-column prop="Solution" label="处理方法" />
    <el-table-column prop="Stuff" label="出勤人员" />
    <el-table-column prop="Consumables" label="维修耗材" />

    <el-table-column fixed="right" prop="State" label="流程状态">
      <template #default="{ row }">
        <span class="state-span" v-if="row.State === '审批中'">
          <svg viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="16" height="16">
            <path d="M512 896a320 320 0 1 0 0-640 320 320 0 0 0 0 640zm0 64a384 384 0 1 1 0-768 384 384 0 0 1 0 768z">
            </path>
            <path d="M512 320a32 32 0 0 1 32 32l-.512 224a32 32 0 1 1-64 0L480 352a32 32 0 0 1 32-32z"></path>
            <path
              d="M448 576a64 64 0 1 0 128 0 64 64 0 1 0-128 0zm96-448v128h-64V128h-96a32 32 0 0 1 0-64h256a32 32 0 1 1 0 64h-96z">
            </path>
          </svg>审批中
        </span>
        <span class="state-span" v-if="row.State === '未通过'">
          <svg viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="16" height="16">
            <path
              d="M764.288 214.592 512 466.88 259.712 214.592a31.936 31.936 0 0 0-45.12 45.12L466.752 512 214.528 764.224a31.936 31.936 0 1 0 45.12 45.184L512 557.184l252.288 252.288a31.936 31.936 0 0 0 45.12-45.12L557.12 512.064l252.288-252.352a31.936 31.936 0 1 0-45.12-45.184z">
            </path>
          </svg>未通过
        </span>
        <span class="state-span" v-if="row.State === '进行中'">
          <svg viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="16" height="16">
            <path
              d="M512 64a32 32 0 0 1 32 32v192a32 32 0 0 1-64 0V96a32 32 0 0 1 32-32zm0 640a32 32 0 0 1 32 32v192a32 32 0 1 1-64 0V736a32 32 0 0 1 32-32zm448-192a32 32 0 0 1-32 32H736a32 32 0 1 1 0-64h192a32 32 0 0 1 32 32zm-640 0a32 32 0 0 1-32 32H96a32 32 0 0 1 0-64h192a32 32 0 0 1 32 32zM195.2 195.2a32 32 0 0 1 45.248 0L376.32 331.008a32 32 0 0 1-45.248 45.248L195.2 240.448a32 32 0 0 1 0-45.248zm452.544 452.544a32 32 0 0 1 45.248 0L828.8 783.552a32 32 0 0 1-45.248 45.248L647.744 692.992a32 32 0 0 1 0-45.248zM828.8 195.264a32 32 0 0 1 0 45.184L692.992 376.32a32 32 0 0 1-45.248-45.248l135.808-135.808a32 32 0 0 1 45.248 0zm-452.544 452.48a32 32 0 0 1 0 45.248L240.448 828.8a32 32 0 0 1-45.248-45.248l135.808-135.808a32 32 0 0 1 45.248 0z">
            </path>
          </svg>进行中
        </span>
        <span class="state-span" v-if="row.State === '已完成'">
          <svg viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="16" height="16">
            <path
              d="M280.768 753.728 691.456 167.04a32 32 0 1 1 52.416 36.672L314.24 817.472a32 32 0 0 1-45.44 7.296l-230.4-172.8a32 32 0 0 1 38.4-51.2l203.968 152.96zM736 448a32 32 0 1 1 0-64h192a32 32 0 1 1 0 64H736zM608 640a32 32 0 0 1 0-64h319.936a32 32 0 1 1 0 64H608zM480 832a32 32 0 1 1 0-64h447.936a32 32 0 1 1 0 64H480z">
            </path>
          </svg>已完成
        </span>
      </template>
    </el-table-column>

  </el-table>
</template>
  
<script lang="ts">
import { ref, onMounted } from 'vue';
import apiClient from "../apiClient";
import { ElIcon } from 'element-plus';
import { ElMessageBox } from "element-plus";
import { useRouter } from "vue-router";
import { useStore } from 'vuex';

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
  State?: string;
}

export default {
  name: 'RepairTable',
  setup() {
    const router = useRouter();

    const handleClick = () => {
      console.log('click');
    };
    const store = useStore();

    const handleRowClick = async (row: Repair) => {
      try {
        const res = await ElMessageBox.confirm(
          "确定要查看此工作流吗？",
          "查看工作流",
          {
            confirmButtonText: "确定",
            cancelButtonText: "取消",
            type: "warning",
          }
        );
        if (res === 'confirm') {
          // 将工作流的唯一标识符存储到 Vuex 中
          store.commit('workflow/setWorkflowNum', row.Num);
        }

      } catch (error) {
        // 用户点击了取消按钮，不做任何操作
      }
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
      handleRowClick,
    };
  },
};
</script>

<style scoped>
.state-span {
  display: flex;
  align-items: center;
}

.state-span svg {
  margin-right: 3px;
}
</style>

  