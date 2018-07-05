import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


class MyTestCase(unittest.TestCase):
    #环境预置
    def setUp(self):
        print("环境预置")

    # 恢复环境
    def tearDown(self):
        print("恢复环境")  # print里面一定要有内容。

    #测试用例（操作步骤）
    def test_somethingA(self):
        print("test2")
        self.assertEqual(True, True)

if __name__ == '__main__':
    unittest.main()