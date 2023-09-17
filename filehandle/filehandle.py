# 文件读取
def read_file(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            text = file.read()
        return text
    except IOError as e:
        print(f"读文件时发生错误: {e}")


# 答案写入
def write_answer(path, sim):
    judge = '判定为抄袭' if sim > 0.6 else '不认定为抄袭'
    try:
        with open(path, 'w') as file:
            file.write('相似度:' + '%.2f%%' % (sim * 100))
            file.write('\n' + judge)
        print(f"成功将答案写入文件", path)
    except IOError as e:
        print(f"写入文件时发生错误：{e}")
