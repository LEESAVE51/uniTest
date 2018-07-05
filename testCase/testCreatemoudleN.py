import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


class CreateModuleG(unittest.TestCase):
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
    def test_CreateModuleG(self):
        dr = self.dr
        dr.find_element_by_xpath("//*[@id='app']/div/div[2]/ul/li[1]/dl/dt[3]").click()
        time.sleep(10)
        dr.switch_to.parent_frame()
        dr.frameC = dr.find_element_by_id("page")
        dr.switch_to.frame(dr.frameC)
        Target = dr.find_element_by_xpath("//*[@id='app']/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]")
        #Target = dr.find_element_by_xpath("//div[@id='app']/div/div[2]/div/div[2]/div[2]/div/div[4]")
        print(self.dr.title)

        ActionChains(self.dr).context_click(Target).perform()
        dr.implicitly_wait(5)

        dr.find_element_by_xpath("//*[@id='app']/div/div[2]/div[1]/div[2]/div[2]/div/div[2]/text()").click()
        time.sleep(5)




        #print("test3")
        self.assertEqual(True, True)

if __name__ == '__main__':
    unittest.main()