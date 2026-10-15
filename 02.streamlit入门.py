# 引入
import streamlit as st

import streamlit as st

st.set_page_config(
    page_title="Streamlit入门",
    page_icon="🧊",
    # 网页的布局
    layout="wide",
    # 控制侧边栏的状态
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.baidu.com',
        'Report a bug': "https://www.baidu.com",
        'About': "# 这是一个Streamlit入门页面 ~" # 提示信息
    }
)

# 大标题
st.title("Streamlit 入门演示")
st.header("Streamlit 一级标题")
st.subheader("Streamlit 二级标题")

st.write("---")
st.write("===")
st.write("???")
st.write("###")


# st.image("./resources/cat.jpg",width=300)
st.image("resources/cat.jpg")

st.audio("resources/news.mp3")

st.video("./resources/news.mp4")

st.logo("./resources/logo.png")

student_data = {
    "姓名":["王磊","王玲","王林","吴丽","五五"],
    "学号":["1111111","2222222","3333333","4444444","5555555"],
    "语文":[1,2,3,4,5],
    "数学":[2,4,6,8,10],
    "英语":[1,3,5,7,9]
}

st.table(student_data)

# 输入框
name = st.text_input("请输入姓名")
st.write(f"您输入的姓名为：{name}")

# 密码输入框
password = st.text_input("请输入密码：",type="password")
st.write(f"您输入的密码为：{password}")

# 单选按钮
gender = st.radio("请输入你的性别",["男","女","未知"],index = 2) # index 为默认选项
st.write(f"您的性别为：{gender}")