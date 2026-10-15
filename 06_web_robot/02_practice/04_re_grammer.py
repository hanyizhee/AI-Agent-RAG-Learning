import re

s1 = "18809090000是我的手机号，188开头的，以00结尾的;我的另一个手机号是15500008888，两个QQ号分别是1259989092和13809091293821，邮箱为python666@163.com，请给我发邮件。"

# print(re.findall("188.*",s1))
# print(re.findall("188.?",s1))
# print(re.findall("188.+",s1))

# print(re.findall(r"188\d{8}",s1)) # 匹配8个
# print(re.findall(r"155\d{6,10}",s1)) # 匹配六到十位
# print(re.findall(r"155\d{6,}",s1)) # 匹配至少六位

# print(re.findall(r"1[38]\d{8}",s1)) # [38] 匹配3或8
# print(re.findall(r"1[^38]\d{8}",s1)) # [^38] 匹配非3或8
# print(re.findall(r"1[3-9]\d{8}",s1)) # [3-9] 匹配3到9
# print(re.findall(r"^1[3-9]\d{9}",s1)) # ^ 匹配开头
# print(re.findall(r"1[3-9]\d{9}$",s1)) # $ 匹配结尾

# print(re.findall(r"\w+@\w+\.\w+",s1)) # \w 匹配任何单词字符（a-z、A-Z、0-9、_、其他语言字符） -- 默认行为
# print(re.findall(r"\w+@\w+\.\w+",s1,re.ASCII)) # \w 匹配任何单词字符（a-z、A-Z、0-9、_）

