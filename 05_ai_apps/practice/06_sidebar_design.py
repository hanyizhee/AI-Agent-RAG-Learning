import streamlit as st # 引入streamlit库
import os # 引入os库
from openai import OpenAI # 引入OpenAI库

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
system_prompt ="""
        你叫%s,现在是用户的真实伴侣,请完全代入伴侣角色。:
        规则:
            1.每次只回1条消息
            2.禁止任何场景或状态描述性文字
            3.匹配用户的语言
            4.回复简短,像微信聊天一样
            5.有需要的话可以用♥等emoji表情
            6.用符合伴侣性格的方式对话
            7.回复的内容,要充分体现伴侣的性格特征
        伴侣性格:
            -%s
        你必须严格遵守上述规则来回复用户。

    """
# 初始化聊天信息
if "messages" not in st.session_state:
    st.session_state.messages = []

# 昵称
if "nick_name" not in st.session_state:
    st.session_state.nick_name = "小甜甜"
# 性格
if "nature" not in st.session_state:
    st.session_state.nature = "活泼开朗的东北姑娘"

# 展示聊天信息
for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])
    # if message["role"] == "user":
    #     st.chat_message("user").write(message["content"])
    # else:
    #     st.chat_message("assistant").write(message["content"])

# 创建与AI大模型交互的客户端对象(DEEPSEEK_API_KEY 环境变量的名字,值就是DeepSeek的API_KEY的)
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'), base_url="https://api.deepseek.com")

# 左侧的侧边栏 - with: streamlit 中的上下文管理器

with st.sidebar:
    st.subheader("伴侣信息")
    # 昵称输入框
    nick_name = st.text_input("昵称",placeholder="请输入昵称",value=st.session_state.nick_name)
    if nick_name is not None:
        st.session_state.nick_name = nick_name
    # 性格输入框
    nature = st.text_area("性格",placeholder="请输入性格",value=st.session_state.nature)
    if nature is not None:
        st.session_state.nature = nature

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
            {"role":"system","content": system_prompt % (st.session_state.nick_name,st.session_state.nature)},
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