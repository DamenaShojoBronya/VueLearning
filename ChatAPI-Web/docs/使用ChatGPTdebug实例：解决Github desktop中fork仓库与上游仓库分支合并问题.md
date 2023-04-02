@[TOC]
# 1.ChatGPT官网
ChatGPT主界面：
https://chat.openai.com/chat
ChatGPT api：
https://platform.openai.com/account/api-keys



# 2.注册教程
https://sms-activate.org/cn/info/ChatGPT
如果你想注册了需要国外手机号，可以参考这个发号平台的教程，注意这些都是免费版的，只能用Chatgpt3.5

# 3.提问流程
问题应该尽可能的描述清楚，并且给出详细的报错信息。
![iH8bvv.png](https://img-blog.csdnimg.cn/img_convert/7ac5decfeedf7d06ed3001ff53eccb8d.png)
这里我没有告诉他我们做到了哪一步，于是ChatGPT给出了一个使用git命令的模板。所以，我先说明这里已经进行到了第四步，然后强调用的是图形化的github desktop而不是git命令行。
![iH8OpU.png](https://img-blog.csdnimg.cn/img_convert/83efee18aea6d7e4656bbf6c1b8b7b80.png)
这里ChatGPT就基于github desktop的操作来说明了，我搜了大半天也没见几个教程是不用命令行的，可见ChatGPT的强大。但是问题还没解决，根据他提示的分支名冲突继续追问
![iH8843.png](https://img-blog.csdnimg.cn/img_convert/8577e1f53d3afe11362d21ed1456f7eb.png)
ChatGPT认为不大可能是分支同名的问题，并且提到在Github网页端上去手动创建Pull Request。试试看这个方法，成功了，但是为什么？继续追问
![iH8INy.png](https://img-blog.csdnimg.cn/img_convert/9aa2d96a284b064a81a0bdf9dbe682be.png)
这里给出了几种可能，我们来看第一种。果然，在Github Desktop里配置的upsteam并不是上游仓库，而是fork仓库

# 4.ChatGPT还可以解答更多问题
从最基础的翻译，比较机械的报错排障，到根据需求写代码，甚至是哲学问题，虽然不可能全部一键得出令人满意的答案，但是很多时候都能给我们提供很多思路。

这里重点介绍了利用ChatGPT进行一个debug的流程，同时也是大部分提问的流程。代码没学会没关系，学会提问就够了！看样子，提出清晰的问题也将是能力的重要一环。
