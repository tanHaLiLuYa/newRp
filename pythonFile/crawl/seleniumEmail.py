from selenium import webdriver
import time
import requests
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

#登录页面
#实例 driver
driver = webdriver.Chrome()
driver.get("https://exmail.qq.com/login")

# ActionChains(driver).***opration(opra)***.perform()
#切换到密码登录页面
driver.find_element_by_partial_link_text("帐号密码登录").click()
#填写密码 账号
driver.find_elements_by_id("inputuin")[0].send_keys('tanpeng@cbiconsulting.com')
driver.find_elements_by_id("pp")[0].send_keys("122579tP")
# 登录
driver.find_elements_by_id("btlogin")[0].click()

#进入 收件箱
driver.find_element_by_id("folder_1").click()

#切换inframe
# driver.find_element_by_xpath("//iframe[@name='mainFrame']")
driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@name='mainFrame']"))

time.sleep(3)#等待页面加载
mailList =[]
# urlList =[]
#翻页
while len(driver.find_elements_by_id("nextpage"))>1: 
    for tab in driver.find_elements_by_xpath("//div[@class='toarea']/table"):
        itemDic ={}
        itemDic["发件人：时间"] =tab.find_element_by_xpath(".//td[@class='tl tf']").get_attribute("title") +":" +\
            tab.find_element_by_xpath(".//td[@class='dt']").text
        itemDic["标题"] = tab.find_element_by_xpath(".//div[@class='txt_hidden']/u").text
        #用于返回
        
        #进入子页面
        clickE = tab.find_element_by_xpath(".//td[@class='ci']")
        ActionChains(driver).context_click(clickE).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        # driver.close()
        time.sleep(2)
        tab.find_element_by_xpath(".//a[@ck='goback']").click()
        # ActionChains(driver).key_down(Keys.CONTROL).send_keys("w").key_up(Keys.CONTROL).perform()
        # driver.close()
        # handle = driver.current_window_handle
        # handles = driver.window_handles
        # for newHandle in handles:
        #     if newHandle!=handle:
        #         driver.switch_to.window(newHandle)
        #         # print(driver.current_window_handle)
        #         # >>>> 获取想要的元素的代码
               
        #         ac = ActionChains(driver).key_down(Keys.CONTROL).send_keys("9").key_up(Keys.CONTROL)
        #         ac.perform()
        #         driver.close()
        #         # print(handles[0])
        #         driver = driver.switch_to.window(handles[0])

        mailList.append(itemDic)
        # print(itemDic)
    #下一页
    driver.find_element_by_id("nextpage").click()
    time.sleep(3)
# print(urlList)

# print(len(mailList))
time.sleep(3)
driver.quit()

