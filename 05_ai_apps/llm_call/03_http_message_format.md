# HTTP协议 - 请求数据格式

## 一、请求报文结构

一个完整的 HTTP 请求报文由三部分组成：**请求行**、**请求头**、**请求体**。

### 1.请求行
> **内容**：请求方式、资源路径、协议版本
> **示例**：'POST /api/courses HTTP/1.1'

### 2.请求头
> **格式**：'Key:value'（键值对）

> **示例**：
> - 'Accept: application/json,text/plain,*/*' （*/* 代表接受所有类型）
> - 'Content-Type: application/json'
> - 'Host: localhost:90'
> - 'User-Agent: Mozilla/5.0...Chroma/143.0.0.0'

### 3.请求体
> **内容**：请求参数部分（GET 请求没有请求体，POST 请求可以包含）
> **示例**：'{"phone": "18808088080","channel": 1,"name": "虎虎","gender":1,"age": 32}'

---

## 二、请求方式对比：GET vs POST

|请求方式|参数位置|请求体|大小限制|
|:---|:---|:---|:---|
|**GET**|请求行中（URL中）|无|浏览器中有大小限制|
|**POST**|请求体中（Body中）|有|通常没有大小限制|

* **GET 示例**：'/api/courses?name=Python&status=1'
* **POST 示例**：适合大量传输数据，如文件上传。

---

## 三、完整请求报文明细示例（参考）
```http
POST /api/courses HTTP/1.1
Accept: application/json, text/plain, */*
Accept-Encoding: gzip, deflate, br, zstd
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Connection: keep-alive
Content-Length: 139
Content-Type: application/json
Host: localhost:90
Origin: http://localhost:90
Referer: http://localhost:90/resource/course
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/143.0.0.0

{"phone':"18808088080","channel":1, 'name":"","gender":1,"age":"32"}
```

# HTTP 协议 - 响应数据格式

一个完整的 HTTP 响应报文同样由三部分组成：**响应行**、**响应头**、**响应体**。

## 一、响应报文结构

### 1. 响应行 (Response Line)
> **内容**：协议版本、状态码
> **示例**：`HTTP/1.1 200`

### 2. 响应头 (Response Headers)
> **格式**：`Key: Value` (键值对)
> **示例**：
- `Server: nginx/1.24.0`
- `Date: Tue, 16 Dec 2025 12:38:08 GMT`
- `Content-Type: application/json`
- `Transfer-Encoding: chunked`
- `Connection: keep-alive`

### 3. 响应体 (Response Body)
> **内容**：存放服务器响应的具体数据（如 JSON、HTML 等）
> **示例**：`{"code": 1, "msg": "success", "data": null}`

---

## 二、常见 HTTP 状态码 (Status Codes)

状态码用于表示服务器对请求的处理结果：

| 状态码 | 含义 | 说明 |
| :--- | :--- | :--- |
| **200** | 请求成功 | 客户端请求成功，服务器正常返回数据 |
| **400** | 请求参数错误 | 客户端发送的请求有语法错误或参数不对 |
| **404** | 资源不存在 | 请求的 URL 输入有误，或网站资源被删除了 |
| **500** | 服务器内部错误 | 服务器发生了不可预期的错误，无法完成请求 |

---

*(附：完整响应报文明细供参考)*
```http
HTTP/1.1 200
Server: nginx/1.24.0
Date: Tue, 16 Dec 2025 12:38:08 GMT
Content-Type: application/json
Transfer-Encoding: chunked
Connection: keep-alive

{"code": 1, "msg": "success", "data": null}
```