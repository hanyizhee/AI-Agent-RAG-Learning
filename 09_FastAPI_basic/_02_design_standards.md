# 开发规范:
>Restful指的是遵循REST架构风格的API接口服务,而REST (REpresentational State Transfer),表述性状态转换,它是一种软件架构风格。

| REST风格url                   | 请求方式 | 备注            | 
|-------------------------------|----------|-----------------|
| http://localhost:8000/users/1 | GET      | 查询id为1的用户 |
| http://localhost:8000/users/1 | DELETE   | 剖除id为1的用户 |
| http://localhost:8000/users   | POST     | 新增用户        |
| http://localhost:8000/users   | PUT      | 修改用户        |

> **注意:** REST是风格,是约定方式,约定不是规定,可以打破。

> **注意:** 描述功能模块通常使用复数形式 (加s),表示此类资源,而非单个资源。如:users、books、items。
