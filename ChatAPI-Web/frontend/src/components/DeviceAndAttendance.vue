<template>
    <view-box>
        <div class="device-and-attendance">
            <el-row>
                <el-col :span="12">
                    <div class="grid-content">
                        <h2>设备保修登记</h2>
                        <el-form ref="deviceForm" :model="deviceForm" label-width="100px">
                            <el-form-item label="姓名" prop="name">
                                <el-input v-model="deviceForm.name"></el-input>
                            </el-form-item>
                            <el-form-item label="设备类型" prop="deviceType">
                                <el-select v-model="deviceForm.deviceType" placeholder="请选择设备类型">
                                    <el-option v-for="type in deviceTypes" :key="type.value" :label="type.label"
                                        :value="type.value"></el-option>
                                </el-select>
                            </el-form-item>
                            <el-form-item label="保修描述" prop="description">
                                <el-input type="textarea" v-model="deviceForm.description"></el-input>
                            </el-form-item>
                            <el-form-item>
                                <el-button type="primary" @click="submitDeviceForm">提交</el-button>
                                <el-button @click="resetDeviceForm">重置</el-button>
                            </el-form-item>
                        </el-form>
                    </div>
                </el-col>
                <el-col :span="12">
                    <div class="grid-content">
                        <h2>出勤情况登记</h2>
                        <el-form ref="attendanceForm" :model="attendanceForm" label-width="100px">
                            <el-form-item label="姓名" prop="name">
                                <el-input v-model="attendanceForm.name"></el-input>
                            </el-form-item>
                            <el-form-item label="出勤日期" prop="attendanceDate">
                                <el-date-picker v-model="attendanceForm.attendanceDate" type="date"
                                    placeholder="选择出勤日期"></el-date-picker>
                            </el-form-item>
                            <el-form-item>
                                <el-button type="primary" @click="submitAttendanceForm">提交</el-button>
                                <el-button @click="resetAttendanceForm">重置</el-button>
                            </el-form-item>
                        </el-form>
                    </div>
                </el-col>
            </el-row>
            <h2>数据展示</h2>
            <el-tabs v-model="activeTab">
                <el-tab-pane label="设备保修记录" name="device">
                    <el-table :data="deviceRecords" style="width: 100%">
                        <el-table-column prop="name" label="姓名" width="180"></el-table-column>
                        <el-table-column prop="deviceType" label="设备类型" width="180"></el-table-column>
                        <el-table-column prop="description" label="保修描述"></el-table-column>
                    </el-table>
                </el-tab-pane>
                <el-tab-pane label="出勤记录" name="attendance">
                    <el-table :data="attendanceRecords" style="width: 100%">
                        <el-table-column prop="name" label="姓名" width="180"></el-table-column>
                        <el-table-column prop="attendanceDate" label="出勤日期" width="180">
                        </el-table-column>
                    </el-table>
                </el-tab-pane>
            </el-tabs>
        </div>
    </view-box>
</template>

<script>
export default {
    name: 'DeviceAndAttendance',
    data() {
        return {
            deviceForm: {
                name: '',
                deviceType: '',
                description: '',
            },
            attendanceForm: {
                name: '',
                attendanceDate: '',
            },
            deviceTypes: [
                { label: '笔记本电脑', value: 'laptop' },
                { label: '台式机', value: 'desktop' },
                { label: '打印机', value: 'printer' },
            ],
            deviceRecords: [],
            attendanceRecords: [],
            activeTab: 'device',
        };
    },
    methods: {
        submitDeviceForm() {
            // 提交设备保修表单的处理逻辑
        },
        resetDeviceForm() {
            this.$refs.deviceForm.resetFields();
        },
        submitAttendanceForm() {
            // 提交出勤情况表单的处理逻辑
        },
        resetAttendanceForm() {
            this.$refs.attendanceForm.resetFields();
        },
    },
};
</script>

<style scoped>
view-box {
    margin: 0 auto;
    width: 70%;
    height: auto;
    margin-top: 100px;
    display: flex;
    justify-content: space-around
}

.device-and-attendance {
    margin: 20px;
}

.grid-content {
    padding: 20px;
    background-color: #f7f7f7;
    border-radius: 4px;
    box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}
</style>
