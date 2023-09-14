import jieba
from bs4 import BeautifulSoup
import re

# 分词
def Participle(text):
    seg_list = jieba.lcut(text)  # 默认是精确模式
    return(seg_list)

# 文件读取
def ReadFile(path):
    with open(path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

# 清晰特殊字符 标点符号
def Clean(phraseArr):
    # 去除特殊字符和标点符号的正则表达式
    pattern = r'[\n\s、，。！？：；“”‘’【】『』【】（）【】《》<>"\',.!?;:()【】【】]'
    # 使用正则表达式替换特殊字符和标点符号为空字符串
    filtered_list = [re.sub(pattern, '', element) for element in phraseArr]

    # 去除空字符串元素
    filtered_list = [element for element in filtered_list if element]

    return filtered_list

# 从html中提取文本
def ExtractionText(html):
    # 创建Beautiful Soup对象
    soup = BeautifulSoup(html, 'html.parser')
    # 提取所有的<td>标签
    td_tags = soup.find_all('td')
    textList = []
    # 提取文本内容并存储
    for td in td_tags:
        textList.append(td.text)

    string = ''.join(textList)
    return string

# 判断文本是否html代码
def IsHtml(text):
    soup = BeautifulSoup(text, 'html.parser')
    td_tags = soup.find_all('td')
    if(len(td_tags)):
        return True
    else:
        return False

# 主函数
def main():
    path1 = 'D:/资料/学习资料/计算机/软件工程/2023/论文查重程序测试样例/orig.txt'
    path2 = 'D:/资料/学习资料/计算机/软件工程/2023/论文查重程序测试样例/orig_0.8_del.txt'
    path3 = 'D:/资料/学习资料/计算机/软件工程/2023/论文查重程序测试样例/orig_0.8_add.txt'

    original_text1 = ReadFile(path1) # 原文
    original_text2 = ReadFile(path2) # html
    original_text3 = ReadFile(path3) # 抄袭文

    text1 = Participle(original_text1)
    text2 = Participle(ExtractionText(original_text2))
    text3 = Participle(original_text3)

    print(Clean(text2))

if __name__ == "__main__":
    main()
