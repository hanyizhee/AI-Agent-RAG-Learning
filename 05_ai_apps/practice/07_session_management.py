# 读文件

# 1.打开文件
f = open(".//resources/API-key.txt","r",encoding = "utf-8")

# 2.读取文件内容
# content = f.read() # 读取所有内容
# print(content)

content_list = f.readlines() # 读取所有行
for line in content_list: # 遍历每一行
    print(line.strip()) # 去掉行末的换行符

# 3.关闭文件
f.close()


# 写文件（方式一）

# 1.打开文件
f = open(".//resources/ceshi.txt","w",encoding = "utf-8")

try:
    # 2.写入文件内容
    f.write("123456\n")
    f.write("654321\n") # 如果文件已经存在，再次写入会覆盖原来的文字
finally: # 无论程序是否正常运行，这段Python代码都会正常运行
    # 3.关闭文件
    f.close()


# 写文件（方式二）

# 1.打开文件
with open (".//resources/ceshi.txt","w",encoding = "utf-8") as f:
    # 2.写入文件内容
    f.write("123456\n")
    f.write("654321\n")