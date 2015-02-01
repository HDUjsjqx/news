### 新闻文章写些什么

主要就是写 when, where, what, how, 我们青协在什么时候，什么地点，做了什么，有
啥感悟和想法，形式没有特别要求，字数不限，关键是写出自己的**真实感受和想法**，
这个不是强制性的总结，不需要特定格式和特定内容，想写什么写什么。注意:

* 不要用模板去套写
* 不要有任何形式的空泛的套话，无意义的意义

### 本地环境要求

* Linux
* Python 2.7+
* pip(apt-get installl python-pip)
* virtualenv(pip install virtualenv)

        $ git clone git@github.com:HDUjsjqx/news.git
        $ cd news
        $ virtualenv venv  # 创建虚拟环境
        $ source venv/bin/activate  # 激活虚拟环境
        (venv)$ pip install pelican markdown ghp-import  # 安装相关依赖和工具

### 如何更新网站

截至2014.12.22，我们的 [news](http://news.hdujsjqx.org) 目前是托管在 github 上
的，当我们把写好的 markdown 文件 push 到 github 上后，网站还是没有更新的，下面
说明一下如何更新网站:

* 写文章。文本语法使用 markdown(.md 结尾)， 开头都要有相应的元数据，比如

        Title: “点滴温暖，感恩于心”--感恩节活动     # 标题
        Date: 2014-11-26 21:09                      # 日期时间
        Category: 2014                              # 分类, 暂时按照年份
        Tags: 青协                                  # 标签，请打上不同的标签
        Slug: gan-en-jie                            # 这个与链接有关，这篇文章为 http://news.hdujsjqx.org/gan-en-jie

  文章的内容见前面所说的`新闻文章写些什么`。如果感觉可以，并且你有相应的权限，
  那么可以 push 到 github 上了。

        $ git add xxx.md
        $ git commit -m 'Add post: xxxx'
        $ git push origin master

* 现在，我们假设你已经写好了一篇文章，我们首先在 news 目录下使用 `make html`
  命令把 markdown 文件转成 html， 这时候，你应该可以在 `output` 文件夹下发现
  你写好的文章了。

* 预览了之后，感觉效果也不错，是时候更新网站了。但是，在这之前，还有一件重要的
  事情要做。由于我们使用了 custom domain(也就是可以通过 http://news.hdujsjqx.org 访问)
  来访问，所以**务必**记得手动在 `output` 文件夹下添加一个 CNAME 文件，内容为
  `news.hdujsjqx.org`。 好了之后，建议使用使用 `ghp-import` 来帮助我们更
  加简单快捷地完成这一任务, 在 news 目录下运行 `ghp-import -p output`，是的，
  稍等一下你就可以看到你的文章已经可以在我们的网站上看到了。

* 恩，总结一下。

        $ git push origin master  # 将本地的新的 markdown 文件推送到 github
        $ ghp-import -p output    # 更新网站

