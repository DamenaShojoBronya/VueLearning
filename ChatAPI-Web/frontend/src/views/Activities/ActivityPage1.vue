<template>
    <view-box>
        <div class="article-container">
            <div class="article-header">
                <h1 class="article-title">北海校区学子在华为ICT大赛2022-2023全国总决赛中再创佳绩</h1>
                <p class="article-meta">by
                    <a href="/blog/author/林佩静" class="author-link">林佩静</a>
                    <span class="article-date">2023/4/13</span>
                </p>
            </div>
            <div class="article-image"> </div>
            <div class="article-content">
                <p>4月13日，华为ICT大赛2022—2023全国总决赛颁奖典礼在海南三亚举行，大赛吸引了全国1200余所院校70000余名学生报名参赛。
                    其中，北海校区3位教授指导的学生团队分别荣获全国云赛道特等奖1项、全国计算赛道和网络赛道一等奖2项的好成绩。</p>
                <p>本届赛事自启动以来，北海校区参赛队认真筹备、一路过关斩将，经过大赛组委会层层选拔、与各大高校精彩角逐，
                    陈名松教授指导的学生团队杨思宇、凌其伍、张日俊荣获总决赛云赛道特等奖，黄廷辉教授指导的学生团队徐扬来、蔡卓鸿、刘子良荣获总决赛计算赛道一等奖，
                    谭印教授指导的学生团队陈正学、周上超、磨安诚荣获总决赛网络赛道一等奖。这是校区学子在2018年获得华为ICT大赛全球总决赛云赛道二等奖、
                    2019年获得华为ICT大赛全球总决赛云赛道一等奖、2021年获得华为ICT大赛全国总决赛云赛道和网络赛道二等奖后第四次获得全国总决赛大奖，该三个团队以优异成绩成功晋级全球总决赛。</p>
                <p>据悉，华为ICT大赛是华为公司面向全球大学生打造的ICT人才竞技交流赛事，旨在为华为ICT学院和有意愿成为ICT学院高校的学生提供国际化的学习平台，
                    提升学生的ICT知识水平，加强学生的实践动手能力以及运用新技术、新平台的创新创造能力。2021年3月，华为ICT大赛首次纳入2020全国普通高校大学生竞赛排行榜内竞赛项目名单，
                    这代表华为ICT大赛成为中国高等教育学会认可的含金量高、参赛价值大的竞赛项目之一。</p>
                <div class="article-image" id="pic1"></div>
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
    background: url("../assets/ICT.jpg") no-repeat center;
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
