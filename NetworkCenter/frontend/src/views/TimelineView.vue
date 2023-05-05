<template>
    <view-box>
        <el-timeline>
            <el-timeline-item center timestamp="2023/4/12" placement="top">
                <el-card>
                    <h4>Update Github template</h4>
                    <p>Tom committed 2018/4/12 20:46</p>
                </el-card>
            </el-timeline-item>
            <el-timeline-item timestamp="2023/3/20" placement="top">
                <el-card>
                    <h4>创建项目并上传代码仓库</h4>
                    <p>Create project&Update Github Firsly</p>
                </el-card>
            </el-timeline-item>
            <el-timeline-item center timestamp="2018/4/2" placement="top">
                Event start
            </el-timeline-item>
            <el-timeline-item timestamp="2018/4/2" placement="top">
                Event end
            </el-timeline-item>
        </el-timeline>
        <el-timeline>
            <el-timeline-item center timestamp="2018/4/12" placement="top">
                <el-card>
                    <h4>Update Github template</h4>
                    <p>Tom committed 2018/4/12 20:46</p>
                </el-card>
            </el-timeline-item>
            <el-timeline-item timestamp="2018/4/3" placement="top">
                <el-card>
                    <h4>Update Github template</h4>
                    <p>Tom committed 2018/4/3 20:46</p>
                </el-card>
            </el-timeline-item>
            <el-timeline-item center timestamp="2018/4/2" placement="top">
                Event start
            </el-timeline-item>
            <el-timeline-item timestamp="2018/4/2" placement="top">
                Event end
            </el-timeline-item>
        </el-timeline>
    </view-box>
</template>
  

<style scope>
view-box {
    margin:0 auto;
    width: 70%;
    height: auto;
    margin-top: 100px;
    display: flex;
    justify-content: space-around
}

el-timeline {

}
.el-timeline-item__wrapper:nth-of-type(1){
    margin-left:-200px;
    position:absolute;
    background-color: aqua;
}
</style>