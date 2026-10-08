import streamlit as st
import os
from openai import OpenAI

# 设置页面的配置项
st.set_page_config(
    page_title="AI智能伴侣",
    page_icon="🤖",
    # 布局
    layout="wide",
    # 控制的是侧边栏的状态
    initial_sidebar_state="expanded",
    menu_items={}
)


#  大标题
st.title("AI智能伴侣")

# Logo
st.logo("resources/cat.png")

# 系统提示词
system_prompt = "你是一名非常可爱的AI助理,你的名字叫小甜甜,请你使用温柔可爱的语气回答用户的问题"

# 初始化聊天信息
if "messages" not in st.session_state:
    st.session_state.messages = []

# 展示聊天信息
for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])
    # if message["role"] == "user":
    #     st.chat_message("user").write(message["content"])
    # else:
    #     st.chat_message("assistant").write(message["content"])

# 创建与AI大模型交互的客户端对象(DEEPSEEK_API_KEY 环境变量的名字,值就是DeepSeek的API_KEY的)
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'), base_url="https://api.deepseek.com")

# 聊天输入框
prompt = st.chat_input("请输入你的问题")
if prompt: # 字符串会自动转换为布尔值，如果字符串非空，则为Ture; ""否则为False
    # st.write(f"用户:{prompt}")
    st.chat_message("user").write(prompt)
    print("---------->调用AI大模型，提示词: ",prompt)
    # 保存用户输入的提示词
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 调用AI大模型 
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role":"system","content": system_prompt},
            *st.session_state.messages
        ],
        stream=True #启用流式输出
    )
    # 输出大模型返回的结果（非流式输出的解析方式）
    # print("<---------- 大模型返回的结果: ",response.choices[0].message.content)
    # st.chat_message("assistant").write(response.choices[0].message.content)


    # 输出大模型返回的结果（流式输出的解析方式）
    response_message = st.empty()# 创建一个空的组件，并用于展示大模型返回的结果
    full_response = "" # 保存大模型返回的结果
    for chunk in response: # 大模型返回的结果是一个流式输出，需要逐个处理
        if chunk.choices[0].delta.content is not None: # 判断当前输出的流式结果是否为None
            content = chunk.choices[0].delta.content # 获取大模型返回的结果
            full_response += content # 保存大模型返回的结果
            response_message.chat_message("assistant").write(full_response) # 展示大模型返回的结果

    # 保存大模型返回的结果
    st.session_state.messages.append({"role":"assistant","content":full_response})