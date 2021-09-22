from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver =webdriver.Chrome()

driver.get("https://orteil.dashnet.org/cookieclicker/")

driver.implicitly_wait(5)

cookie = driver.find_element_by_id("bigCookie")
cookie_count =driver.find_element_by_id("cookies")
items = [driver.find_element_by_id("productPrice" + str(i)) for i in range(1,-1,-1)]

actions = ActionChains(driver)

actions.click(cookie)

for i in range(5000):
    actions.perform()
    count = int(cookie_count.text.split(" ")[0])
    for item in items:
        value = int(item.text)
        if value <= count:
            upgrade_acitons =ActionChains(driver)
            upgrade_acitons.move_to_element(item)
            upgrade_acitons.click()
            upgrade_acitons.perform()


# driver.get("https://techwithtim.net")
# link =driver.find_element_by_link_text("Python Programming")
# link.click()

# try:
#     element = WebDriverWait(driver,10).until(
#         EC.presence_of_element_located((By.LINK_TEXT,"Beginner Python Tutorials"))
#         )
#     element.click()
# except:
#     driver.quit()


time.sleep(15)
driver.quit()#quit 退出整个浏览器 close 关闭标签

