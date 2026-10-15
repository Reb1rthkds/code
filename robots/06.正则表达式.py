import re

s1 = "我的手机号是18809091231你记住了吗？我的另一个手机号是18800001266，QQ号是1779989922和1344444444444444444444你记住了吗？"
s2 = "18809091231是我的手机号你记住了吗？我的另一个手机号是18800001266，QQ号是1779989922你记住了吗？"

"""
    # match - 从字符的开头开始匹配（返回Match对象）
    # search - 从任意位置开始，搜索第一个匹配项（返回Match对象）
    # findall - 从任意位置开始，搜索所有匹配项（返回list）

"""

# match - 从字符的开头开始匹配（返回Match对象） 只会匹配第一个匹配项
# result = re.match(r"1[3-9]\d{9}",s1)  # ----None
# print(result.group())   # 报错

# result = re.match(r"1[3-9]\d{9}",s2)
# print(result.group())
# print(result.span()) # 获取匹配项的索引
# print(result.start()) # 获取匹配项的开始索引
# print(result.end()) # 获取匹配项的结束索引

# search - 从任意位置开始，搜索第一个匹配项（返回Match对象）
# result = re.search(r"1[3-9]\d{9}",s1)
# print(result.group())
# print(result.span())

# findall - 从任意位置开始，搜索所有匹配项（返回list）

# s1 = "我的手机号是18809091231你记住了吗？我的另一个手机号是18800001266，QQ号是1779989922和1344444444444444444444你记住了吗？"
result = re.findall(r"1[3-9]\d{9}",s1)
print(result)
