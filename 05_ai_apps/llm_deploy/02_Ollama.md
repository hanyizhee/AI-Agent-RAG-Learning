# 大模型部署‑本地部署（Ollama）

## 1. Ollama基础概念
Ollama**不是大模型**，是开源的本地大模型运行管理工具。
- 官网：<https://ollama.com/>
- 功能：下载GGUF模型权重、调度显卡显存/内存、提供命令行交互、对外暴露本地API接口
- 特点：支持离线运行，对话数据不会上传外网

### 关键概念区分
|对象|说明|
|---|---|
|Ollama|运行工具，提供模型运行环境，负责加载调度模型|
|DeepSeek‑R1|GGUF格式大模型权重文件，真正负责推理计算的AI大脑|
|Ollama本地API|本地程序调用模型的通信接口，默认地址：`http://localhost:11434`|

## 2. 本地API vs DeepSeek云端API
|对比项|Ollama本地API|DeepSeek云端API|
|---|---|---|
|访问地址|`http://localhost:11434`|`https://api.deepseek.com`|
|模型位置|存储在本机磁盘|运行在DeepSeek远程服务器|
|网络|可离线使用|必须联网|
|密钥|不需要API‑Key|需要申请API‑Key，按token计费|
|硬件消耗|占用本机显存、内存|几乎不消耗本机硬件|

## 3. 模型量化说明
示例模型：`deepseek‑r1:7b‑qwen‑distill‑q4_K_M`
- `Q4`：4bit量化，压缩模型大小，降低显存占用
- `K`：K‑quants混合量化算法
- `M`：Medium中等档位，平衡模型效果与显存消耗

> 硬件参考：RTX3060‑6G，该量化版本约占用4.5‑4.8G显存；原始Q8版本7B模型显存占用8G以上，本机无法流畅运行。

## 4. Ollama常用命令
```cmd
# 下载拉取模型
ollama pull deepseek‑r1:7b‑qwen‑distill‑q4_K_M

# 命令行交互对话
ollama run deepseek‑r1:7b‑qwen‑distill‑q4_K_M

# 查看本地已下载模型列表
ollama list

# 在交互窗口清空上下文，释放显存
/clear