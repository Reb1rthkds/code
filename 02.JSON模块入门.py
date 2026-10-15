import json

# 写入json文件
user = {
    "name": "张三",
    "age": 18,
    "gender": "男",
    "is_student": True,
    "courses": ["Math", "English"],
    "hobbies":["Reading", "Gaming"],
    "address": None
}

# 写入json数据文件
with open("resources/user.json","w",encoding="utf-8") as f:
    # ensure_ascii:默认为True，确保所有的数据都是ascii码（非ascii码进行转换），设置为False则不进行转换
    # indent:会在输出的json数据中添加缩进（格式化）
    json.dump(user, f, ensure_ascii = False, indent=2)

# 读取json数据文件
with open("resources/user.json","r",encoding="utf-8") as f:
    user = json.load(f)
    print(user)
    print(type(user))
