from selenium import webdriver

from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:\\Users\\Nxt\\PycharmProjects\\automation\\Drivers\\chromedriver.exe")

driver.get("https://www.google.com/")

title = driver.title

driver.find_element_by_name("q").send_keys("Software Testing notes")


#driver.quit()

