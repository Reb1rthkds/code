import streamlit as st

import os
from openai import OpenAI

st.set_page_config(
    page_title="AI智能伴侣",
    page_icon="🤖",
    # 网页的布局
    layout="wide",
    # 控制侧边栏的状态
    initial_sidebar_state="expanded",
    menu_items={}
)

# 大标题
st.title("AI智能伴侣")
st.write("欢迎使用AI智能伴侣")


# logo
st.logo("resources/logo.png")

# 初始化聊天信息
if 'messages' not in st.session_state:
    st.session_state.messages = []


# 初始化昵称
if 'nickname' not in st.session_state:
    st.session_state.nickname = "小甜甜"

# 初始化性格
if 'nature' not in st.session_state:
    st.session_state.nature = "一个活泼开朗的东北姑娘"

# 展示聊天信息
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.write(message["content"])

# for messages in st.session_state.messages:
#     if  messages["role"] == "user":
#         st.chat_message("user").write(messages["content"])
#     elif messages["role"] == "assistant":
#         st.chat_message("assistant").write(messages["content"])
for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])



# 系统提示词
system_prompt = """
        你叫 %s，现在是用户的真实伴侣，请完全代入伴侣角色。：
        规则：
            1．每次只回1条消息
            2．禁止任何场景或状态描述性文字
            3.匹配用户的语言
            4.回复简短，像微信聊天一样
            5.有需要的话可以用等emoji表情
            6.用符合伴侣性格的方式对话
            7.回复的内容，要充分体现伴侣的性格特征
        伴侣性格：
            - %s
            你必须严格遵守上述规则来回复用户
"""
# 创建与AI大模型交互的客户端对象（DEEPSEEK_API_KEY 环境变量的名字，值就是deepseek的API_KEY）
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'),base_url="https://api.deepseek.com")



# 左侧侧边栏
# st.sidebar.subheader("伴侣信息")
# nickname = st.sidebar.text_input("昵称")
# nickname = st.sidebar.text_input("昵称")
# nickname = st.sidebar.text_input("昵称")
# nickname = st.sidebar.text_input("昵称")
# nickname = st.sidebar.text_input("昵称")
# nickname = st.sidebar.text_input("昵称")
# nickname = st.sidebar.text_input("昵称")
# nickname = st.sidebar.text_input("昵称")

# with 是streamlit的语法，用于创建一个上下文管理器，用于管理组件的显示和隐藏
with st.sidebar:
    st.subheader("伴侣信息")

    # 昵称输入框
    nickname = st.text_input("昵称",value=st.session_state.nickname,placeholder="请输入昵称")
    if nickname:
        st.session_state.nickname = nickname

    # 性格输入框
    nature = st.text_area("性格",value=st.session_state.nature,placeholder="请输入性格")
    if nature:
        st.session_state.nature = nature

# 消息输入框
prompt = st.chat_input("请输入您要问的问题")
if prompt:
    st.chat_message("user").write(prompt)
    print("------> 调用AI大模型，提示词：",prompt)
    # 保存用户消息
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 调用 AI大模型 与 AI大模型进行交互

    # 输出日志
    # print([
    #     {"role": "system", "content": system_prompt},
    #     *st.session_state.messages
    #      ] )
    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[
            {"role": "system", "content": system_prompt % (st.session_state.nickname, st.session_state.nature)},
            *st.session_state.messages    # 核心代码
        ],
        stream=True,
    )

    # 输出大模型返回的结果（非流式输出的解析方式）
    # print("<------ 这是大模型返回的结果：", response.choices[0].message.content)
    # st.chat_message("assistant").write(response.choices[0].message.content)

    response_message = st.empty() # 创建一个空组件，用于展示大模型返回的结果

    # 流式输出大模型返回的结果
    full_response = ""
    for chunk in response:
        # st.chat_message("assistant").write(chunk.choices[0].delta.get("content", ""))
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            full_response += content
            response_message.chat_message("assistant").write(full_response)

    # 保存大模型返回的结果
    st.session_state.messages.append({"role":"assistant","content":full_response})