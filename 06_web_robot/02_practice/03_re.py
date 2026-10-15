# 正则表达式

# 正则表达式(Regular Expression)是一种由特定语法规则组成的文本模式,用来描述、匹配字符串中符合特定规则的字符序列。就相当于一种模式匹配工具,允许用户通过简介的语法进行复杂文本的搜索、匹配、提取和替换工作。

import re

s1="18809090000是我的手机号,你记住了吗?我的另一个手机号是18800008888,两个QQ号分别是155998992 和 18809091293821 你记住了吗?"

s2="我的手机号是18809090000,你记住了吗?我的另一个手机号是18800008888,两个QQ号分别是155998992 和 18809091293821 你记住了吗?"

# match - 从字符串的开头开始匹配（匹配第一个匹配项） ----> Match 对象
result = re.match(r"1[3-9]\d{9}",s1)
print(result)
print(result.group()) # 获取到匹配项
print(result.span()) # 获取匹配项的索引
print(result.start()) # 获取匹配项的开始索引
print(result.end()) # 获取匹配项的结束索引

# search - 从任意位置开始，搜索第一个匹配项 ----> Match 对象
result = re.search(r"1[3-9]\d{9}",s2)
print(result)
print(result.group())
print(result.span())
print(result.start())
print(result.end())

# findall - 从任意位置开始，搜索所有匹配项 ----> list
result = re.findall(r"1[3-9]\d{9}",s2)
print(result)

# 什么是正则表达式,有什么用?
# 定义的是字符串的组成规则,根据规则匹配或替换文本中符合这个规则的字符串


# 字符串前的r标识什么意思?
# r表示当前这个字符串中的转义字符无效,作为普通字符串使用


# re模块提供的如下三个函数的作用与区别?
# match(“正则表达式”,“文本字符串”)
# search(“正则表达式”,“文本字符串”)
# findall(“正则表达式”,“文本字符串”)




