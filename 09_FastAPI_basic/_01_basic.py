# Web:全球广域网,也称为万维网(www World Wide Web),能够通过浏览器访问到的网站。
# 通过浏览器地址栏访问到的网站都是Web网站，也叫Web应用
# Web网站由三个核心部分组成:前端程序（页面展示）、服务端程序（业务逻辑处理）、数据库（数据存储和管理）。
# 前端程序:负责前端页面的展示,网页由 HTML(负责网页的结构)、CSS(负责网页的表现)、JavaScript(负责网页的动作)三个部分组成。
# FastAPI是一个现代、快速、高性能的Web框架,用于基于标准的Python类型提示构建API接口服务。
# 官网:https://fastapi.org.cn
# API接口:应用程序编程接口(Application Programming Interface),就是对外提供的功能入口,供别人来调用(比如:天气查询的API接口)。
from fastapi import FastAPI

# 创建 FastAPI 应用实例
app = FastAPI()

# 定义API接口
@app.get("/")
def root():
    return {"message":"Hello World"}

@app.get("/users")
def get_users():
    return [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"}
    ]


# 启动服务 ----> uvicorn: Python中的轻量web服务器
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app,host="0.0.0.0",port=8000)