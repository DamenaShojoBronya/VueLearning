<template>
    <view-box>
        <div class="article-container">
            <div class="article-header">
                <h1 class="article-title">北海校区领导带队赴华为技术服务（广西）有限公司参观交流</h1>
                <p class="article-meta">by <a href="/blog/author/林佩静" class="author-link">林佩静</a>
                    <span class="article-date">2023/4/13</span> </p>
            </div>
            <div class="article-image"> </div>
            <div class="article-content">
                <p>为进一步加强校企合作，探索校区与华为公司在人才培养、教学科研等方面的沟通合作，3月13日，学校校长助理、北海校区校长陈名松带队赴华为技术服务（广西）有限公司参观交流。
                    华为广西政企商业业务部总监何东岷热情接待。校区领导王鑫、曹计划、王军，相关学院负责人及职能部门负责人一行参与了此次参观交流。</p>
                <p>何东岷引导北海校区一行参观华为技术服务（广西）有限公司展厅，讲解了华为企业总体战略布局、华为在广西区域整体建设运行情况、
                    以及华为公司发展的历史沿革，技术革新，通过现代科技展示了华为产品的特色及在各个场景中的实际应用效果。</p>
                <p>参观过程中，双方针对深入开展校企合作、人才培养、学生就业事宜展开交流。陈名松表示，桂电北海校区目前正在紧锣密鼓与华为公司共建ICT产业学院，
                    期待双方的合作源远流长、前景广阔，双方要在校企联合人才培养工作上下功夫，积极推动校企资源与信息共享，
                    希望华为公司为北海校区学子们提供更多就业、实习机会，让他们在华为有长足发展，真正促进校、企、生三方共赢。</p>
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
    background: url("../../assets/北海校区领导带队赴华为技术服务（广西）有限公司参观交流.png") no-repeat center;
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
