<template>
    <el-scrollbar class="scrollbar" height="480px" width="1400px">

        <div v-for="(item, index) in tableData" :key="index">
            <div class="progress-card">
                <div class="card-top">
                    <span>
                        <div class="img"></div>
                        <p>设备报修工作流</p>
                    </span>
                    <!-- #409eff -->
                    <span>
                        <el-button-group>
                            <el-button color="#337ecc" @click="approve(item)">
                                <p style="color:white">批准</p>
                            </el-button>
                            <el-button @click="reject(item)">
                                <p style="color:#337ecc">拒绝</p>
                            </el-button>
                        </el-button-group>

                        <!-- <div text class="edit-button" @click="toggleDetail(index)">...</div> -->

                        <span @click="toggleDetail(index)">
                            <svg viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg" class="edit-button">
                                <path fill="currentColor"
                                    d="M176 416a112 112 0 1 1 0 224 112 112 0 0 1 0-224zm336 0a112 112 0 1 1 0 224 112 112 0 0 1 0-224zm336 0a112 112 0 1 1 0 224 112 112 0 0 1 0-224z">
                                </path>
                            </svg>
                        </span>

                        <span @click="hideItem(index)">
                            <svg viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg" class="delete-icon">
                                <path fill="currentColor"
                                    d="M195.2 195.2a64 64 0 0 1 90.496 0L512 421.504 738.304 195.2a64 64 0 0 1 90.496 90.496L602.496 512 828.8 738.304a64 64 0 0 1-90.496 90.496L512 602.496 285.696 828.8a64 64 0 0 1-90.496-90.496L421.504 512 195.2 285.696a64 64 0 0 1 0-90.496z">
                                </path>
                            </svg>
                        </span>
                        <!-- <el-button type="success" :icon="Check" circle @click="hideItem(index)"></el-button> -->
                    </span>
                </div>

                <!-- <el-steps :active="activeStep" :space="200" simple finish-status="success"> -->
                <el-steps :active="getCurrentStep(item.State)" finish-status="finish" simple>
                    <el-step :title="item.State === '未通过' ? '未通过' : '审批中'"
                        :status="item.State === '未通过' ? 'error' : (item.State === '审批中' ? 'process' : (getCurrentStep(item.State) > 1 ? 'success' : 'wait'))"></el-step>
                    <el-step title="进行中"
                        :status="item.State === '未通过' ? 'wait' : (item.State === '进行中' ? 'process' : (getCurrentStep(item.State) > 2 ? 'success' : 'wait'))"></el-step>
                    <el-step title="已完成" :status="item.State === '已完成' ? 'success' : 'wait'"></el-step>
                </el-steps>


            </div>

            <el-descriptions v-if="detailsVisible[index]" title="设备报修详情" direction="horizontal" :column="2">
                <el-descriptions-item label="报修编号">{{ item.Num }}</el-descriptions-item>
                <el-descriptions-item label="报修时间">{{ item.Date }}</el-descriptions-item>
                <el-descriptions-item label="报修地点">{{ item.Location }}</el-descriptions-item>
                <el-descriptions-item label="问题描述">{{ item.Description }}</el-descriptions-item>
                <el-descriptions-item label="报修人员">{{ item.Reporter }}</el-descriptions-item>
                <el-descriptions-item label="联系方式">{{ item.Phonenum }}</el-descriptions-item>
                <el-descriptions-item label="处理方法">
                    <span @click="() => editItem(item, 'Solution', '处理方法')">{{ item.Solution }}</span>
                </el-descriptions-item>
                <el-descriptions-item label="出勤人员">
                    <span @click="() => editItem(item, 'Stuff', '出勤人员')">{{ item.Stuff }}</span>
                </el-descriptions-item>
                <el-descriptions-item label="维修耗材">
                    <span @click="() => editItem(item, 'Consumables', '维修耗材')">{{ item.Consumables }}</span>
                </el-descriptions-item>
            </el-descriptions>


        </div>

    </el-scrollbar>
</template>
  
<script lang="ts">
import { ref, computed, watch, onMounted, reactive } from "vue";
import apiClient from "../apiClient";
import { ElMessage, ElMessageBox } from 'element-plus';
import { Delete, Edit, Search, Share, Upload } from '@element-plus/icons-vue'
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
    name: "ProcessApproval",
    components: {},

    setup() {
        const getCurrentStep = (state: string): number => {
            switch (state) {
                case '审批中':
                    return 1;
                case '进行中':
                    return 2;
                case '未通过':
                    return 3; // 你可以选择一个不同的步骤数来表示拒绝状态
                case '已完成':
                    return 4; // 你可以选择一个不同的步骤数来表示拒绝状态
                default:
                    return 0;
            }
        };
        const store = useStore();

        const workflowNum = ref(""); // 初始化一个 ref 用于存储工作流编号
        const workflowVisible = computed(() => workflowNum.value === store.state.workflow.workflowNum); // 计算属性，用于判断工作流是否可见

        watch(() => store.state.workflow.workflowNum, (newValue) => {
            workflowNum.value = newValue;
        });

        const hideItem = (index: number) => {
            ElMessageBox.confirm(
                '关闭工作流？',
                'Warning',
                {
                    confirmButtonText: 'OK',
                    cancelButtonText: 'Cancel',
                    type: 'warning',
                }
            )
                .then(() => {
                    tableData.value.splice(index, 1);
                    ElMessage({
                        type: 'success',
                        message: 'Delete completed',
                    })
                })
                .catch(() => {
                    ElMessage({
                        type: 'info',
                        message: 'Delete canceled',
                    })
                })
            // tableData.value.splice(index, 1);
        };


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
                console.log("Approving repair:", item.Num);
                // API call to approve the repair
                await apiClient.put(`/api/repairs/${item.Num}/approve`, { state: "进行中" });
                // Update the state of the repair
                item.State = "进行中";
                for (let i = 0; i < tableData.value.length; i++) {
                    if (tableData.value[i].Num === item.Num) {
                        tableData.value[i].State = "进行中";
                        break;
                    }
                }
                console.log("Repair approved:", item.Num);
            } catch (error) {
                console.error("Failed to approve repair:", error);
            }
        };


        const reject = async (item: Repair) => {
            try {
                console.log("Approving repair:", item.Num);
                // API call to approve the repair
                await apiClient.put(`/api/repairs/${item.Num}/reject`, { state: "未通过" });
                // Update the state of the repair
                item.State = "未通过";
                for (let i = 0; i < tableData.value.length; i++) {
                    if (tableData.value[i].Num === item.Num) {
                        tableData.value[i].State = "未通过";
                        break;
                    }
                }
                console.log("Repair rejected:", item.Num);
            } catch (error) {
                console.error("Failed to reject repair:", error);
            }
        };

        // 出勤人员登记，用El消息盒子，点击弹出
        const editItem = (item: Repair, field: keyof Repair, label: string) => {
            ElMessageBox.prompt(`请输入${label}`, `${label}`, {
                confirmButtonText: "确定",
                cancelButtonText: "取消",
            })
                .then(async ({ value }) => {
                    item[field] = value;

                    // 提交数据到后端
                    try {
                        await apiClient.put(`/api/repairs/${item.Num}/update`, { [field]: value });

                        // 在这里更新状态为已完成
                        if (
                            item.Solution !== "正在出勤" &&
                            item.Stuff !== "正在出勤" &&
                            item.Consumables !== "暂无"
                        ) {
                            item.State = "已完成";
                            await apiClient.put(`/api/repairs/${item.Num}/update`, { State: "已完成" });
                            ElMessage({
                                type: "success",
                                message: `出勤登记完成`,
                            });
                        }

                        ElMessage({
                            type: "success",
                            message: `修改成功: ${label}`,
                        });
                    } catch (error) {
                        console.error(`Failed to update ${label}:`, error);
                        ElMessage({
                            type: "error",
                            message: `修改失败: ${label}`,
                        });
                    }
                })
                .catch(() => {
                    ElMessage({
                        type: "info",
                        message: "修改取消",
                    });
                });
        };



        // ...
        return {
            workflowVisible,
            hideItem,
            getCurrentStep,
            handleClick,
            tableData,
            toggleDetail,
            detailsVisible,
            approve,
            reject,
            editItem,
        };
    },

};

</script>
  
<style scoped>
.el-scrollbar {
    display: flex;
    justify-content: center;
    align-items: center;
}

.icon-state {
    margin-right: 4px;
}

.progress-card {
    margin: 20px;
    margin-top: 10px;
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
    /* margin-top: -5px; */
    /* margin-left: 15px; */
    width: 24px;
    height: 24px;
    cursor: pointer;
    filter: invert(45%) sepia(30%) saturate(4401%) hue-rotate(192deg) brightness(88%) contrast(78%);
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

.el-descriptions {
    margin-left: 20px;
    margin-bottom: 40px;
    /* border-radius: 10px; */
    width: 1150px;
    /* border: solid 1px #e7e5e5; */
    box-shadow: 0px 6px 22px 0px rgba(0, 0, 0, 0.10);
    padding: 20px 50px 20px 50px;
    /* background-color: rgb(246, 246, 246); */

}

.delete-icon {
    width: 24px;
    height: 24px;
    cursor: pointer;
    filter: invert(45%) sepia(30%) saturate(4401%) hue-rotate(192deg) brightness(88%) contrast(78%);
}

/* .custom-label-color {
  --el-text-color-primary: gray;
} */
</style>
  