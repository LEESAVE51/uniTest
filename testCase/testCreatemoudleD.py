import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import os, time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



class CreateModuleD(unittest.TestCase):
    #删除模板
    #环境预置
    def setUp(self):
        self.dr = webdriver.Chrome()
        self.dr.implicitly_wait(3)
        self.dr.get("http://192.168.1.249:8080/ticai/dist/main.html#login.html")
        print("打开浏览器")
        dr = self.dr
        dr.frameA = dr.find_element_by_id("page")
        dr.switch_to.frame(dr.frameA)
        dr.find_element_by_class_name("el-input__inner").send_keys("lsw")
        dr.find_element_by_class_name("s-submit-area").click()
        time.sleep(5)
        dr.switch_to.parent_frame()
        dr.frameB = dr.find_element_by_id("page")
        dr.switch_to.frame(dr.frameB)

    # 恢复环境
    def tearDown(self):
        self.dr.quit()
        print("关闭浏览器")  # print里面一定要有内容。

    #测试用例（操作步骤）
    def test_CreateModuleD(self):
        dr = self.dr
        dr.find_element_by_xpath("//*[@id='app']/div/div[2]/ul/li[1]/dl/dt[3]").click()
        time.sleep(10)
        # 切换到父表单
        dr.switch_to.parent_frame()
        # 切换表单
        dr.frameC = dr.find_element_by_id("page")
        dr.switch_to.frame(dr.frameC)
        # 选择模板
        # 首先定位table
        self.table = dr.find_element_by_xpath("//*[@id='app']/div/div[2]/div[2]/div/div/div[4]/table")
        # table的总行数，包含标题
        self.table_rows = self.table.find_elements_by_tag_name('tr')
        print("总行数:", len(self.table_rows))
        # table的总列数
        '''
        在table中找到第一个tr,之后在其下找到所有的th,即是table的总列数
        '''
        self.table_cols = self.table_rows[0].find_elements_by_tag_name('td')
        print("总列数:", len(self.table_cols))
        # 获取某单元格的text:获取第一行第二列的text,[不算标题行]
        self.row1_col2 = self.table_rows[1].find_elements_by_tag_name('td')[1].text
        print("第一行第二列的text:", self.row1_col2)
        # 删除最后一行
        self.table_rows[0].find_element_by_tag_name('input').click()
        time.sleep(2)



        #driver.switch_to_alert().accept()
        #time.sleep(2)









        #print("test3")
        self.assertEqual(True, True)

if __name__ == '__main__':
    unittest.main()