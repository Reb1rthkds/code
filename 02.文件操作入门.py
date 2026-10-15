# 文件操作

# 打开文件
f = open("resources/望庐山瀑布.txt","r",encoding="utf-8")

# 读取文件内容
# content = f.read() # 读取所有内容
# print(content)

# content_list = f.readlines()
#
# for list in content_list:
#     print(list.strip())  # 删除行末的换行符


# # 写入文件
# f1 = open("resources/静夜思.txt","w",encoding="utf-8")
#
# f1.write("静夜思(李白)\n\n")
# f1.write("窗前明月光，\n")
# f1.write("疑是地上霜。\n")
# f1.write("举头望明月，\n")
# f1.write("低头思故乡。\n")  # 写入文件
#

# # 关闭文件
# f.close()



# ================================释放文件资源=================================

# 繁琐的文件资源释放操作！！！！
# 写入文件
f1 = open("resources/静夜思.txt","w",encoding="utf-8")

try:
    # 写入内容
    f1.write("静夜思(李白)\n\n")
    f1.write("窗前明月光，\n")
    # i = 1 / 0
    f1.write("疑是地上霜。\n")
    f1.write("举头望明月，\n")
    f1.write("低头思故乡。\n")

# 关闭文件
finally:
    print("文件已关闭")
    f.close()


# 推荐方式
# 打开文件
with open("resources/静夜思.txt","w",encoding="utf-8") as f:
    # 写入文件内容
    f.write("静夜思(李白)\n\n")
    f.write("窗前明月光，\n")
    f.write("疑是地上霜。\n")
    f.write("举头望明月，\n")
    f.write("低头思故乡。\n")


# 文件尾部追加内容
with open("resources/静夜思.txt","a",encoding="utf-8") as f:
    f.write("追加内容\n")


