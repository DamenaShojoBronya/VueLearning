<template>
    <el-scrollbar height="430px">
        <div>
            <div v-for="(item, index) in tableData" :key="index">
                <el-card>
                    <el-button @click="approve(item)">批准</el-button>
                    <el-button @click="reject(item)">拒绝</el-button>
                    <el-button @click="toggleDetail(index)">详情</el-button>

                    <el-steps :active="activeStep" finish-status="success">
                        <el-step title="提交"></el-step>
                        <el-step title="审批中"></el-step>
                        <el-step title="已审批"></el-step>
                    </el-steps>
                </el-card>

                <el-descriptions v-if="detailsVisible[index]" title="设备报修详情" direction="horizontal" :column="1" :size="size"
                    border>
                    <el-descriptions-item label="报修编号">{{ item.Num }}</el-descriptions-item>
                    <el-descriptions-item label="报修时间">{{ item.Date }}</el-descriptions-item>
                    <el-descriptions-item label="报修地点">{{ item.Location }}</el-descriptions-item>
                    <el-descriptions-item label="问题描述">{{ item.Description }}</el-descriptions-item>
                    <el-descriptions-item label="报修人员">{{ item.Reporter }}</el-descriptions-item>
                    <el-descriptions-item label="联系方式">{{ item.Phonenum }}</el-descriptions-item>
                    <el-descriptions-item label="处理方法">{{ item.Solution }}</el-descriptions-item>
                    <el-descriptions-item label="出勤人员">{{ item.Stuff }}</el-descriptions-item>
                    <el-descriptions-item label="维修耗材">{{ item.Consumables }}</el-descriptions-item>
                </el-descriptions>
            </div>
        </div>
    </el-scrollbar>
</template>
  
<script lang="ts">
import { ref, onMounted, reactive } from "vue";
import apiClient from "../apiClient";
import {
    Document,
    Menu as IconMenu,
    Location,
    Setting,
} from '@element-plus/icons-vue'

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
    name: "ProcessApproval",
    components: {},
    setup() {
        const detailsVisible = reactive<Record<number, boolean>>({});

        const handleClick = () => {
            console.log("click");
        };

        const toggleDetail = (index: number) => {
            detailsVisible[index] = false;
        };

        const tableData = ref<Repair[]>([]);

        const fetchRepairs = async () => {
            try {
                const response = await apiClient.get("/api/repairs");
                tableData.value = response.data;
                tableData.value.forEach((_, index) => {
                    detailsVisible[index] = false;
                });
            } catch (error) {
                console.error("Failed to fetch repairs:", error);
            }
        };

        onMounted(fetchRepairs);

        // ...

        const approve = async (item: Repair) => {
            try {
                // API call to approve the repair
                await apiClient.put(`/api/repairs/${item.Num}/approve`);
                // Update the state of the repair
                item.State = "已审批";
            } catch (error) {
                console.error("Failed to approve repair:", error);
            }
        };

        const reject = async (item: Repair) => {
            try {
                // API call to reject the repair
                await apiClient.put(`/api/repairs/${item.Num}/reject`);
                // Update the state of the repair
                item.State = "已拒绝";
            } catch (error) {
                console.error("Failed to reject repair:", error);
            }
        };

        const detail = (item: Repair) => {
            console.log("Repair details:", item);
        };

        // ...
        return {
            handleClick,
            tableData,
            toggleDetail,
            detailsVisible,
            approve,
            reject,
            detail,
        };
    },
    
};

</script>
  
<style scoped>
.icon-state {
    margin-right: 4px;
}
</style>
  