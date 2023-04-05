<template>
    <el-scrollbar height="480px">

        <div v-for="(item, index) in tableData" :key="index">
            <div class="progress-card">
                <div class="card-top">
                    <span>
                        <div class="img"></div>
                        <p>设备报修工作流</p>
                    </span>
                    <!-- #409eff -->
                    <span>
                        <el-button color="#337ecc" @click="approve(item)">
                            <p style="color:white">批准</p>
                        </el-button>
                        <el-button @click="reject(item)">
                            <p style="color:#337ecc">拒绝</p>
                        </el-button>
                        <div text class="edit-button" @click="toggleDetail(index)">...</div>
                    </span>
                </div>

                <!-- <el-steps :active="activeStep" :space="200" simple finish-status="success"> -->
                <el-steps :active="1" finish-status="success" simple>
                    <el-step title="提交"></el-step>
                    <el-step title="审批中"></el-step>
                    <el-step title="已审批"></el-step>
                </el-steps>
            </div>
            
                <el-descriptions v-if="detailsVisible[index]" title="设备报修详情" direction="horizontal" :column="1" :size="size"
                    >
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

    </el-scrollbar>
</template>
  
<script lang="ts">
import { ref, onMounted, reactive } from "vue";
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
            detailsVisible[index] = !detailsVisible[index];
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


        // ...
        return {
            handleClick,
            tableData,
            toggleDetail,
            detailsVisible,
            approve,
            reject,
        };
    },

};

</script>
  
<style scoped>
.icon-state {
    margin-right: 4px;
}

.progress-card {
    margin-bottom: 20px;
    margin-left: 20px;
    border-radius: 10px;
    width: 1150px;
    border: solid 1px #e7e5e5;
    box-shadow: 0px 6px 22px 0px rgba(0, 0, 0, 0.10);
    background-color: rgb(246, 246, 246);
}

.progress-card .el-steps {
    border-radius: 0px 0px 10px 10px;
    background-image: linear-gradient(to right, #dbe2e8, #f5e3cc);
}

.el-card__body {
    padding: 0;
}

.card-top {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-right: 20px;
    height: 48px;
    background-color: rgb(246, 246, 246);
}

.edit-button {
    margin-top: -5px;
    margin-left: 15px;
    cursor: pointer;
}

.card-top span {
    display: flex;
    align-items: center;
    margin-left: 15px;
}

.card-top span p {
    font-weight: bold;
    margin-left: 5px;
}

.card-top .img {
    display: inline-block;
    width: 30px;
    height: 30px;
    background-image: url("../../assets/man.png");
    background-blend-mode: lighten;
    background-size: cover;
    filter: invert(45%) sepia(10%) saturate(5000%) hue-rotate(176deg) brightness(94%) contrast(82%);
}

.progress-card:hover {
    box-shadow: 0 6px 22px 0 rgba(0, 0, 0, 0.3);
    border: 1px white;
}

.el-descriptions{
    margin-left: 20px;
    margin-bottom: 40px;
    /* border-radius: 10px; */
    width: 1150px;
    /* border: solid 1px #e7e5e5; */
    box-shadow: 0px 6px 22px 0px rgba(0, 0, 0, 0.10);
    padding:10px 40px 40px 40px;
    /* background-color: rgb(246, 246, 246); */
}
</style>
  