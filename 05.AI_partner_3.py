import streamlit as st
import os
from openai import OpenAI
import json
from datetime import datetime

# 设置页面配置
st.set_page_config(
    page_title="AI智能伴侣",
    page_icon="🤖",
    # 网页的布局
    layout="wide",
    # 控制侧边栏的状态
    initial_sidebar_state="expanded",
    menu_items={}
)

# 生成会话标识
def generate_session_name():
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# 保存会话信息函数
def save_session():
    # 1.保存当前的会话信息
    if st.session_state.current_session:
        # 构建新的会话对象
        session_data = {
            "nickname": st.session_state.nickname,
            "nature": st.session_state.nature,
            "current_session": st.session_state.current_session,
            "messages": st.session_state.messages
        }

        # 创建文件夹（如果sessions不存在）
        if not os.path.exists("sessions"):
            os.mkdir("sessions")

        # 保存会话信息
        with open(f"sessions/{st.session_state.current_session}.json", "w", encoding="utf-8") as f:
            json.dump(session_data, f, ensure_ascii=False, indent=2)


# 加载所有会话信息
def load_sessions():
    session_list = []
    # 加载session目录下的文件
    if os.path.exists("sessions"):
        file_list = os.listdir("sessions")
        for filename in file_list:
            if filename.endswith(".json"):
                session_list.append(filename[:-5])
    session_list.sort(reverse=True) # 排序，降序排序
    return session_list

# 加载指定会话数据
def load_session(session_name):
    try:
        if os.path.exists(f"sessions/{session_name}.json"):
            # 读取会话数据
            with open(f"sessions/{session_name}.json", "r", encoding="utf-8") as f:
                session_data = json.load(f)
                st.session_state.messages = session_data["messages"]
                st.session_state.nickname = session_data["nickname"]
                st.session_state.nature = session_data["nature"]
                st.session_state.current_session = session_name
    except Exception:
        st.error("加载会话失败！")



# 删除会话信息
def delete_session(session_name):
    try:
        if os.path.exists(f"sessions/{session_name}.json"):
            os.remove(f"sessions/{session_name}.json") # 删除文件
            # 如果删除的是当前会话，则需要更新消息列表
            if session_name == st.session_state.current_session:
                # 构建新的会话
                st.session_state.messages = []
                # st.session_state.nickname = "小甜甜"
                # st.session_state.nature = "一个活泼开朗的东北姑娘"
                st.session_state.current_session = generate_session_name()
    except Exception:
        st.error("删除会话失败！")

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

# 会话标识
if "current_session" not in st.session_state:
    st.session_state.current_session = generate_session_name()


#


# 展示聊天信息
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.write(message["content"])

# for messages in st.session_state.messages:
#     if  messages["role"] == "user":
#         st.chat_message("user").write(messages["content"])
#     elif messages["role"] == "assistant":
#         st.chat_message("assistant").write(messages["content"])
st.text(f"当前会话：{st.session_state.current_session}")
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
    # 会话信息
    st.subheader("AI控制面板")

    # 新建会话
    if st.button("新建会话",width="stretch",icon="✏️"):
        # 1.保存当前的会话信息
        save_session()

        # 2.创建新的会话
        if st.session_state.messages:# 如果当前聊天信息非空，True
            st.session_state.messages = []
            st.session_state.current_session = generate_session_name()
            save_session()
            st.rerun() # 重新运行页面



    # 会话历史
    st.text("会话历史")
    session_list = load_sessions()
    for session in session_list:
        col1,col2 = st.columns([4,1])
        with col1:
            # 加载会话信息
            # 三元运算符：如果条件为真，则返回第一个表达式的值；否则返回第二个表达式的值 ---> 语法：值1 if 条件 else 值2
            if st.button(session,width="stretch",icon="📄",key = f"load_{session}",type="primary" if session == st.session_state.current_session else "secondary"):
                load_session(session)
                st.rerun()
        with col2:
            # 删除会话信息
            if st.button("",width="stretch",icon="❌",key = f"delete_{session}"):
                delete_session(session)
                st.rerun()


        # st.button(session,width="stretch",icon="📄")
        # st.button("",width="stretch",icon="❌")


    # 分割线
    st.divider()

    # 伴侣信息
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

    # 保存会话信息
    save_session()