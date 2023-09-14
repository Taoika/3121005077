import jieba
from bs4 import BeautifulSoup
import re
from gensim import corpora

# 分词
def Participle(text):
    seg_list = jieba.lcut(text)  # 默认是精确模式
    return(seg_list)

# 文件读取
def ReadFile(path):
    with open(path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

# 内容清洗
def Clean(arr):
    result = []
    for item in arr:
        # 仅匹配中英文
        if (re.match(u"[a-zA-Z0-9\u4e00-\u9fa5]", item)):
            result.append(item)
            return result
        else:
            pass

    return result

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

# 频率计算
def CalcFrequency(text1List1, textList2):
    textList=[text1List1, textList2]
    # 将所有文本中的词语映射到唯一的ID
    dictionary = corpora.Dictionary(textList)
    # 创建一个语料库，将文本转化为词袋（bag-of-words）表示
    corpus = [dictionary.doc2bow(text) for text in textList]
    return corpus

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

    CalcFrequency(text1, text2)

if __name__ == "__main__":
    main()
