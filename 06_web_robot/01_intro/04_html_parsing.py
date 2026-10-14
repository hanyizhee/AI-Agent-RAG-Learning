# 网页解析: 网页解析指的是从原始HTML文档中提取数据的过程,也是网络爬虫的关键步骤,从一堆标签文本中提取出需要的数据。
# lxml:是一个高性能的HTML/XML文档的解析库,支持基于Xpath语法来解析和获取网页数据。

# 安装:pip install lxml

from lxml import html

# 读取 html 文件
with open("06_web_robot/resources/仙逆人物志.html", "r", encoding="utf-8") as f:
    html_content = f.read()

    # 解析 html 文本，并将其转换为一个文档对象
    doc = html.fromstring(html_content)

    # 解析表头 - xpath语法
    th_list = doc.xpath("//table/thead/tr/th/text()")
    print(th_list)

    # 解析表格中的数据 - xpath语法
    # 获取第一行数据
    td_list = doc.xpath("//table/tbodt/tr[1]/td/text()")

    # 获取所有行数据
    tr_list = doc.xpath("//table/tbody/tr")
    for tr in tr_list:
        td_list = tr.xpath("td/text()")
        print(td_list)

# Xpath:是一种用于在HTML/XML文档中导航或定位元素的查询语言,让你能够准确的定位文档中的特定元素、属性或文本。

# /                 从根节点的直接子元素                 /html/body/div/h1
# //                从当前节点的任意子元素               /html/body/div//h1
# .                 当前节点下查找                      ./a与.//a
# [n]               选择第n个元素                       //p[2]
# [last()]          选择最后一个元素                    //p[last()]
# [@attr]           选择有该属性的元素                  //p[@color]
# [@attr='value']   选择该属性值等于指定值的元素         //p[@color='red']
# *                 匹配任何元素节点                    //body/div/*
# @*                匹配元素的任何属性                  //body/div/a/@*
# text()            获取文本内容                        //div/p/text()


# <html lang="zh-CN">
# <head>
# <meta charset="UTF-8">
# <title>仙逆人物志 - 修真世界</title>
# </head>
# <body>
# <div>
# <h1>Python</h1>
# <p>一门简介、快速、易用的编程语言。</p>
# <p>人生苦短,我用Python。</p>
# <p color="red">AI大模型开发、AI智能应用开发。</p>
# <a href="https://www.itcast.cn">@R</a>
# </div>
# </body>
# </html>













