<template>
    <view-box>

        <div class="common-layout">
            <el-container>
                <el-aside width="200px">Aside</el-aside>
                <el-main>

                    <el-card class="box-card">
                        <template #header>
                            <div class="card-header">
                                <span>Card name</span>
                            </div>

                        </template>



                        <el-table :data="tableData" style="width: 100%" max-height="450">
                            <el-table-column fixed prop="date" label="Date" width="150" />
                            <el-table-column prop="name" label="Name" width="120" />
                            <el-table-column prop="state" label="State" width="120" />
                            <el-table-column prop="city" label="City" width="120" />
                            <el-table-column prop="address" label="Address" width="600" />
                            <el-table-column prop="zip" label="Zip" width="120" />
                            <el-table-column fixed="right" label="Operations" width="120">
                                <template #default>
                                    <el-button link type="primary" size="small" @click="handleClick">Detail</el-button>
                                    <el-button link type="primary" size="small">Edit</el-button>
                                </template>
                            </el-table-column>
                        </el-table>

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
    margin-top: 100px;
    display: flex;
    justify-content: space-around
}

.card-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
}
</style>

<script setup>
const handleClick = () => {
    console.log('click')
}

const tableData = [
    {
        date: '2016-05-03',
        name: 'Tom',
        state: 'California',
        city: 'Los Angeles',
        address: 'No. 189, Grove St, Los Angeles',
        zip: 'CA 90036',
        tag: 'Home',
    },
    {
        date: '2016-05-02',
        name: 'Tom',
        state: 'California',
        city: 'Los Angeles',
        address: 'No. 189, Grove St, Los Angeles',
        zip: 'CA 90036',
        tag: 'Office',
    },
    {
        date: '2016-05-04',
        name: 'Tom',
        state: 'California',
        city: 'Los Angeles',
        address: 'No. 189, Grove St, Los Angeles',
        zip: 'CA 90036',
        tag: 'Home',
    },
    {
        date: '2016-05-01',
        name: 'Tom',
        state: 'California',
        city: 'Los Angeles',
        address: 'No. 189, Grove St, Los Angeles',
        zip: 'CA 90036',
        tag: 'Office',
    },
]
</script>

<script>
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
