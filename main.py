import jieba
from bs4 import BeautifulSoup


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
    print(phraseArr)

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

    return textList

# 主函数
def main():
    path1 = 'D:/资料/学习资料/计算机/软件工程/2023/论文查重程序测试样例/orig.txt'
    path2 = 'D:/资料/学习资料/计算机/软件工程/2023/论文查重程序测试样例/orig_0.8_del.txt'

    original_text1 = ReadFile(path1)
    original_text2 = ReadFile(path2)

    text1 = ExtractionText(original_text1)
    text2 = ExtractionText(original_text2)

if __name__ == "__main__":
    main()
