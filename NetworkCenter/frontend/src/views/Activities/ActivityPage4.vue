<template>
    <view-box>
        <div class="article-container">
            <div class="article-header">
                <h1 class="article-title">北海校区校长陈名松一行赴杭州开展信息化建设专题调研</h1>
                <p class="article-meta">by <a href="/blog/author/谭印" class="author-link">谭印</a>
                    <span class="article-date">2022/11/9</span> </p>
            </div>
            <div class="article-image"> </div>
            <div class="article-content">
                <p>11月5日，学校校长助理、北海校区校长陈名松，校区常务副校长王鑫及校区网络中心负责人一行赴浙江农林大学就信息化建设工作开展调研。浙江农林大学信息与教育技术中心主任莫路锋热情接待并陪同调研。</p>
                <p>莫路锋介绍了浙江农林大学信息化建设“一库一表”工程相关情况。他表示，农林大学通过建设中心数据库、建设报表及办事大厅，实现了数据一次审核、报表数据自动统计生成、真正做到全校行政事务“一网通办”，提升学校综合治理能力现代化战略目标。</p>
                <p>陈名松从北海校区发展历程、办学定位、办学特色、人才培养等方面介绍了校区的基本情况。他表示，通过此次调研活动，学习了浙江农林大学在信息化建设、信息系统应用推广服务等方面积累的成功经验，北海校区将借鉴经验并立足实际，不断推进校区信息化与教学、科研、管理和服务等各项工作有效融合，进一步提升校区信息化建设发展水平，为校区转型发展提供强有力支持。</p>
                <p>次日，陈名松一行赴杭州孝道科技有限公司进行考察交流。</p>
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
    background: url("../../assets/卡片3.jpg") no-repeat center;
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
