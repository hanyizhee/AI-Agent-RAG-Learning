# 大模型部署‑DeepSeek官方开放API（云端部署）
> 属于云端大模型部署方式，模型运行在DeepSeek远程服务器，**不需要本地下载GGUF模型权重文件**。

## 1. 基础概念
- 官方平台地址：<https://platform.deepseek.com/>
- API基础访问地址：`https://api.deepseek.com`[[(GitHub)]](https://github.com/hkai-ai/LLM_OFFICIAL_DOCUMENTATION/blob/main/deepseek/README.md?f_link_type=f_linkinlinenote&flow_extra=eyJkb2NfaWQiOiJhNzNlYjBlNDVkYmVlZWUzLTBkNjIwYzBmMTJmNzAzZjYiLCJpbmxpbmVfZGlzcGxheV9wb3NpdGlvbiI6MCwiZG9jX3Bvc2l0aW9uIjowfQ%3D%3D "[(GitHub)]")
- 工作模式：MaaS（模型即服务），通过HTTP网络请求调用远端DeepSeek大模型。

- 特点：
    - ✅无需本地显卡，几乎不消耗本机显存、内存
    - ✅开箱即用，不用下载模型文件
    - ❌必须联网；对话数据上传DeepSeek服务器；调用消耗token，产生费用；必须使用API‑Key鉴权

### 与Ollama本地API对比
|对比项|DeepSeek官方云端API|Ollama本地API|
|---|---|---|
|模型位置|DeepSeek远程服务器|本机磁盘GGUF模型文件|
|访问地址|`https://api.deepseek.com`|`http://localhost:11434`|
|密钥|**必须配置API‑Key**|不需要密钥|
|网络|必须联网|支持离线运行|
|硬件消耗|几乎不占用本机显卡显存|占用本机显存、内存|

## 2. 使用步骤
1. 访问DeepSeek开放平台，注册账号并完成实名认证。
2. 在平台页面创建 **API‑Key**，复制保存密钥（仅展示一次，丢失无法找回）。
3. 代码中配置密钥，发送HTTP请求调用接口。
4. 账户余额不足时，接口会调用失败，需要充值。

## 3. Python调用示例（requests原生）
```python
import requests

# 将此处替换为自己申请的API‑Key
api_key = "sk‑xxxxxxxxxxxxxxxxxxxx"
url = "https://api.deepseek.com/v1/chat/completions"

headers = {
    "Content‑Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

payload = {
    "model": "deepseek‑r1",
    "messages": [{"role": "user", "content":"解释什么是大模型量化"}]
}

resp = requests.post(url, json=payload, headers=headers)
print(resp.json())