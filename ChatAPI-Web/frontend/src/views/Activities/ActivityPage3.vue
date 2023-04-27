<template>
    <view-box>
        <div class="article-container">
            <div class="article-header">
                <h1 class="article-title">【访企拓岗促就业】北海校区领导一行赴南宁开展校企合作交流和访企拓岗</h1>
                <p class="article-meta">by <a href="/blog/author/李翔宇" class="author-link">李翔宇</a>
                    <span class="article-date">2023/3/7</span> </p>
            </div>
            <div class="article-image"> </div>
            <div class="article-content">
                <p>3月4-5日，学校校长助理、北海校区校长陈名松，校区常务副校长王鑫，副校长孙永厚及电子信息学院、计算机工程学院相关负责人一行到华为技术服务（广西）有限公司、广西昊华科技股份有限公司等开展校企合作交流和访企拓岗。</p>
                <p>在华为技术服务（广西）有限公司交流会上，双方就桂林电子科技大学北海校区华为ICT学院建设方案进行了沟通交流，陈名松表示，以华为ICT学院建设为契机，推动校区专业建设、校企合作课程资源建设、双师型师资队伍建设，希望华为技术服务（广西）有限公司组织产业生态链相关企业到校区招聘毕业生，为校区毕业生提供更多和更高质量的就业机会；在广西昊华科技股份有限公司交流会上，双方就兼职教师聘用、科研合作、教师利用假期深入企业参与相关项目、学生实习、企业招聘校区毕业生就业等方面开展广泛交流，达成初步共识。</p>
                <p>据悉，校区领导还走访了广西晟德电子科技有限责任公司等企业。</p>
                <!-- <div class="article-image" id="pic1"></div> -->
            </div>
        </div>

    </view-box>
</template>

<style scoped>
a {
    color: inherit;
    text-decoration: inherit;
}

h3,
p {
    display: block;
    margin-block-start: 1em;
    margin-block-end: 1em;
    margin-inline-start: 0px;
    margin-inline-end: 0px;
    line-height: 34px;
}

view-box {
    margin: 0 auto;
    margin-top: 150px;
    width: 100%;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    background-color: #f7f7f7;
}

.article-container {
    width: 733.33px;
    height: auto;
    position: relative;
    background-color: white;
    padding: 60px 60px;
    text-align: start;
}

.article-header {
    font-size: 1.125rem;
    line-height: 1.75rem;
    max-width: 65ch;
    text-align: start;
}

.article-title {
    font-size: 2em;
    font-weight: 600;
    line-height: 3.25rem;
    color: #333;
}

.article-meta {
    font-size: 1rem;
    padding-top: 0.5em;
    color: #999;
}

.author-link {
    color: #007bff;
    text-decoration: none;
}

.author-link:hover {
    text-decoration: underline;
}

.article-date {
    margin-left: 1em;
    font-weight: 400;
    font-size: 0.875rem;
}

.article-image {
    width: 740px;
    height: 340px;
    background: url("../../assets/卡片2.jpg") no-repeat center;
    background-size: cover
}

#pic1 {
    background: url("../../assets/颁奖典礼现场.png") no-repeat center;
    background-size: cover;
    height: 760px;
}

.article-content {
    margin: 1.5em auto 0;
    font-size: 1.125rem;
    color: #666;
}

.button-container {
    display: flex;
    justify-content: center;
    margin-top: 0.5em;
    margin-left: 0.5em;
}

.ycdc-retro-btn {
    text-decoration: none;
    /* Update the styles accordingly */
}

@media screen and (max-width: 767px) {
    .article-title {
        font-size: 1.5em;
        line-height: 38px;
    }

    .article-container {
        max-width: 350px;
    }

    .article-header,
    .article-image,
    .article-content {
        flex-direction: column;
        align-items: center;
    }



    .article-image {
        max-width: 350px;
        max-height: 200px;
    }

    #pic1 {
        max-height: 350px;
    }
}
</style>
