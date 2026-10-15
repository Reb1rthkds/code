# csv 操作 - 方式一:文件操作的原始方式
# # 写
# with open("csv_data/01.csv","w",encoding="utf-8") as f:
#     f.write("姓名,性别,年龄,爱好\n")
#     f.write("kds,男,18,'python,java'\n")
#     f.write("kds,男,18,c\n")
#     f.write("kds,男,18,go\n")
#     f.write("kds,男,18,js\n")
#     f.write("kds,男,18,c++\n")
#
# # 读
# with open("csv_data/01.csv","r",encoding="utf-8") as f:
#     for line in f:
#         print(line.strip())


# csv 操作 - 方式二:csv 模块(推荐)
import csv

# 写
with open("csv_data/02.csv","w",encoding="utf-8", newline="") as f:      # -----newline = "" 避免空行
    write = csv.DictWriter(f,fieldnames=["姓名","性别","年龄","爱好"])
    write.writeheader() # 写入表头
    write.writerow({"姓名":"kds","性别":"男","年龄":18,"爱好":"python"}) # 一行一行写
    write.writerow({"姓名":"kds","性别":"男","年龄":18,"爱好":"java"})
    write.writerow({"姓名":"kds","性别":"男","年龄":18,"爱好":"c"})
    write.writerow({"姓名":"kds","性别":"男","年龄":18,"爱好":"go"})
    write.writerow({"姓名":"kds","性别":"男","年龄":18,"爱好":"js"})
    write.writerow({"姓名":"kds","性别":"男","年龄":18,"爱好":"c++"})


# 读
with open("csv_data/02.csv","r",encoding="utf-8") as f:
    read = csv.DictReader(f)
    for row in read:
        print(row)



