import unittest
from filehandle import read_file, write_answer


class TestFileHandle(unittest.TestCase):
    def test_read_file1(self):
        text = read_file('D:/资料/学习资料/计算机/软件工程/2023/论文查重程序测试样例/orig.txt')
        self.assertIsInstance(text, str)

    def test_write_file(self):
        res = write_answer('D:/资料/学习资料/计算机/软件工程/2023/答案.txt', 0.123)
        self.assertIsNone(res)

    def test_write_file2(self):
        res = write_answer('D:/资料/学习资料/计算机/软件工程/2023/答案.txt', 0.711)
        self.assertIsNone(res)

    def test_write_file3(self):
        res = write_answer('', 0.711)
        self.assertIsNone(res)
