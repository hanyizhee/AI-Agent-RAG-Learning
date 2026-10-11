import json

# dump(): 将python对象序列化为json格式字符串并写入文件
# load():从文件中读取json格式数据，并将其反序列化为python对象


# 写入json数据文件
user={
    "name":"涛哥",
    "age":"18",
    "gender":"男",
    "hobbies":["reading","swimming"]
}

with open("05_ai_apps/practice/resources/user.json","w",encoding="utf-8") as f:
    # ensure_ascii: 默认为Ture,确保持有的数据输出的数据都是ascii编码(非ASCII码会进行转义);False，非ASCII码不进行转义保留原样输出
    # indent: 会在输出的json数据中添加缩进（格式化）
    json.dump(user,f,ensure_ascii=False,indent=4)

# 读取json数据文件

with open("05_ai_apps/practice/resources/user.json","r",encoding="utf-8") as f:
    user = json.load(f)
    print(type(user))