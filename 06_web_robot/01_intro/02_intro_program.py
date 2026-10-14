import requests
from lxml import html

# 定义url
target_url = "https://www.tiobe.com/tiobe-index/"

# 发送结果，获取数据
response = requests.get(target_url)

# 输出数据到控制台
# print(response.text)

doc = html.fromstring(response.text)

# 解析数据
# 解析表头中的数据1
th_list = doc.xpath("//table[@id='top20']/thead/tr/th/text()")
print(th_list)

# 解析表格中的数据
tr_list = doc.xpath("//table[@id='top20']/tbody/tr")
for tr in tr_list:
    td_list = tr.xpath("td/text()")
    print(td_list)


# 获取TIOBE编程语言排行榜单

# 1. 查看TIOBE网站的robots.txt文件,明确资源获取的规则

# 2. 安装requests库,用于发送网络请求 (pip install requests)

# 3. 编写python代码,访问TIOBE网站,获取数据

# Requests库的作用是什么?
# Requests库是Python中最流行、最优雅的HTTP客户端库,让Python代码发送HTTP请求变得极其简单