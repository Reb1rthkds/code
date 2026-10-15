from lxml import html


# 读取html文件
with open("resource/tiobe.html","r",encoding="utf-8") as f:
    html_text = f.read()

# 解析html的文本，将其转换成一个文档对象
    document = html.fromstring(html_text)

# 解析表头 - xpath语法
    th_list = document.xpath("//table/thead/tr/th/text()")
    print(th_list)


# 解析表格中的数据 - xpath语法

    # td_list = document.xpath("//table/tbody/tr/td/text()")
    # print(td_list)
    # //......:从任意位置开始匹配
    tr_list = document.xpath("//table/tbody/tr[2]/td/text()")
    print(tr_list)

    # last():表示最后一个
    tr_list = document.xpath("//table/tbody/tr[last()-1]/td/text()")
    print(tr_list)


    # p[@class]表示匹配有class属性的p标签
    p_list = document.xpath("//p[@class]/text()")
    print(p_list)

    # p[@class = 'xn']表示匹配有class属性为xn的p标签
    p_list = document.xpath("//p[@class = 'xn']/text()")
    print(p_list)

    # *:表示任意元素
    tr_list = document.xpath("//thead/tr/*/text()")
    print(tr_list)


    # @src：表示匹配src属性
    # @*：表示匹配任意属性
    # a_list = document.xpath("//td/img/@src")
    a_list = document.xpath("//td/img/@*")
    print(a_list)