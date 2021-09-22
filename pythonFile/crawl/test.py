
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
 
# 模拟登陆qq邮箱
driver = webdriver.Chrome()
driver.get("https://mail.qq.com/")
# time.sleep(5)
# 切换iframe
driver.switch_to.frame("login_frame")  #switch_to.frame()reference是传入的参数，用来定位frame，可以传入id、name、index以及selenium的WebElement对象
# 用户名 密码
driver.find_element_by_name("u").send_keys("xxxxxxxx@qq.com") 
# elem_user.send_keys("xxxxxxxx@qq.com")    # 登录邮箱
driver.find_element_by_name("p").send_keys("password")
# elem_pwd.send_keys("password")             # 登录密码
elem_but = driver.find_element_by_id("login_button")
# elem_pwd.send_keys(Keys.RETURN)
elem_but.click()
time.sleep(5)
driver.quit()