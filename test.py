# from selenium import webdriver
# import time
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.select import Select
#
# driver = webdriver.Chrome(r"E:\C\Python\test\Selenium Tutorial\Drivers\chromedriver.exe")
#
# driver.set_page_load_timeout(10)
# # driver.get("https://www.amazon.in")
# # driver.find_element_by_name("field-keywords").send_keys("The Alchemist")
# # driver.find_element_by_class_name("nav-input").send_keys(Keys.ENTER)
# # link = driver.find_element_by_link_text('The Alchemist')
# # driver.get(link.get_attribute('href'))
# # # link.click()
# # # driver.find_element_by_link_text('Add to Cart').click()
# # driver.find_element_by_id("add-to-cart-button").click()
# # time.sleep(4)
# # driver.quit()
#
# driver.get("https://www.amazon.in")
#
# sel = Select(driver.find_element_by_xpath("//select[@class='nav-search-field']"))
# #select by select_by_visible_text() method
# sel.select_by_visible_text("the alchemist")
# time.sleep(0.8)
# #select by select_by_index() method
# sel.select_by_index(0)
# # driver.find_element_by_class_name("nav-input").send_keys(Keys.ENTER)
# # link = driver.find_element_by_link_text('The Alchemist')
# # driver.get(link.get_attribute('href'))
# # # link.click()
# # # driver.find_element_by_link_text('Add to Cart').click()
# # driver.find_element_by_id("add-to-cart-button").click()
# time.sleep(4)
# driver.quit()

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(r"E:\C\Python\test\Selenium Tutorial\Drivers\chromedriver.exe")

driver.set_page_load_timeout(10)
driver.get("https://www.amazon.in")
driver.find_element_by_name("field-keywords").send_keys("The Alchemist")
driver.find_element_by_class_name("nav-input").send_keys(Keys.ENTER)
link = driver.find_element_by_link_text('The Alchemist')
driver.get(link.get_attribute('href'))
driver.find_element_by_id("add-to-cart-button").click()
time.sleep(4)
driver.quit()