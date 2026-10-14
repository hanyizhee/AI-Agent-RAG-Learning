# 网络爬虫基础

网络机器人:也称为网络爬虫,是一种按照一定的预设规则,自动浏览并抓取网络数据的程序或脚本。

开始 --> 发送HTTP请求 --> 解析结果提取数据 --> 数据处理(清洗) --> 数据存储 --> 结束（存储数据结束之后，再次回到发送HTTP请求位置）

数据清洗:是指对采集到的原始数据进行处理、修正、转换和标准化的过程,目的是让数据变得规范、准确。

## 网络机器人-合规性(robots协议)

robots协议也称为爬虫协议、爬虫规则,是指网站根目录下存放的一份文本文件robots.txt,用于告诉爬虫哪些页面可以抓取,哪些页面不能抓取。(君子协议)


> - User-Agent: 用户代理,通过该请求头确认爬虫的类型
> - Disallow: 禁止访问的资源
> - Allow: 允许访问的资源
> - sitemap: 网站地图,帮助爬虫更高效地获取网站内容
> - Crawl-delay: 爬取间隔时间,避免频繁访问造成网站压力过大

```text
# 通用规则(针对所有爬虫)
User-agent: *
Disallow: /wp-admin/
Allow: /wp-admin/admin-ajax.php
Sitemap: https://www.tiobe.com/sitemap_index.xml
Crawl-delay: 5

# 特定规则(针对豌豆荚爬虫)
User-agent: Wandoujia Spider
Disallow: /

# 特定规则(针对谷歌广告爬虫)
User-agent: Mediapartners-Google
Disallow: /subject_search
Disallow: /amazon_search
Disallow: /search
Disallow: /group/search
```