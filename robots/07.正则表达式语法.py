import re
s = "18809090000是我的手机号，188开头的，以00结尾的：我的另一个手机号是15500008888，两个QQ号分别是1259989092和13809091293821，邮箱为pyth0n666@163.com,请给我发邮件"

# 正则表达式
# . 任意字符
# print(re.findall(r"188.*",s)) # * 匹配任意个
# print(re.findall(r"188.+",s)) # + 匹配一个或多个
# print(re.findall(r"188.?",s)) # ? 匹配零个或一个


# \d 任意数字
# print(re.findall(r"188\d{8}",s)) # {8} 匹配8个
# print(re.findall(r"155\d{6,10}",s)) # {6,10} 匹配6到10个
# print(re.findall(r"155\d{6,}",s)) # {6,} 匹配6个或更多

# []
# print(re.findall(r"1[38]\d{8}",s)) # [38] 匹配3或8
# print(re.findall(r"1[^38]\d{8}",s)) # [^38] 匹配除3或8以外的任意字符
# print(re.findall(r"1[3-9]\d{8}",s)) # [3-9] 匹配3到9
# print(re.findall(r"^1[3-9]\d{7,8}",s)) # ^ 匹配字符串的开头
# print(re.findall(r"^1[3-9]\d{9}$",s)) # $ 匹配字符串的结尾

#
# # \w
# print(re.findall(r"\w+@\w+\.\w+",s)) # \w 匹配任意字母、数字、下划线和其他语言字符  ----默认行为
# print(re.findall(r"\w+@\w+\.\w+",s,re.ASCII)) # \w 匹配任意字母、数字、下划线 ----ASCII行为


# 注意
s2 = "现在的时间是2026-02-06 10:02:25, 今天的天气还可以, 气温是28度 "
# print(re.findall(r"\d{4}-\d{2}-\d{2}",s2))
print(re.findall(r"(\d{4})-(\d{2})-(\d{2})",s2))