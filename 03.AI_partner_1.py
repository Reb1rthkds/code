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

# 初始化聊天信息
if 'messages' not in st.session_state:
    st.session_state.messages = []

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


# 大标题
st.title("AI智能伴侣")
st.write("欢迎使用AI智能伴侣")


# logo
st.logo("resources/logo.png")

# 系统提示词
system_prompt = "你是一个可爱的小助手，请你用可爱的语气回答用户的问题"

# 创建与AI大模型交互的客户端对象（DEEPSEEK_API_KEY 环境变量的名字，值就是deepseek的API_KEY）
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'),base_url="https://api.deepseek.com")


# 消息输入框
prompt = st.chat_input("请输入您要问的问题")
if prompt:
    st.chat_message("user").write(prompt)
    print("------> 调用AI大模型，提示词：",prompt)
    # 保存用户消息
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 调用 AI大模型 与 AI大模型进行交互
    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
        stream=False,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}}
    )

    # 输出大模型返回的结果
    print("<------ 这是大模型返回的结果：", response.choices[0].message.content)
    st.chat_message("assistant").write(response.choices[0].message.content)

    # 保存大模型返回的结果
    st.session_state.messages.append({"role":"assistant","content":response.choices[0].message.content})