import os
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class myClass:
    def __init__(self):
        self.myVar = 5

    def getText(self):
        a = open("output.txt", "w", encoding='utf-8')
        for path, subdirs, files in os.walk(r'D:\Media\Music\New Fav 1\Completed'):
            for filename in files:
                a.write(str(filename) + os.linesep)

    def preProcess(self):
        filename = "output.txt"
        with open(filename) as f:
            content = f.readlines()

        # you may also want to remove whitespace characters like `\n` at the end of each line
        content = [x.strip() for x in content]
        content = [x.split('.')[0]   for x in content]
        # content = [if(x)  for x in content]
        print(content)


    def automate(self):
        driver = webdriver.Chrome(r"E:\C\Python\test\Selenium Tutorial\Drivers\chromedriver.exe")

        driver.set_page_load_timeout(10)
        driver.get("https://accounts.spotify.com/en/login?continue=https:%2F%2Fopen.spotify.com%2Fsearch%2F")
        driver.find_element_by_id('login-username').send_keys("gmail_id")
        driver.find_element_by_id('login-password').send_keys("password")
        driver.find_element_by_id("login-button").send_keys(Keys.ENTER)
        # WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        # (By.XPATH, "//li[2]/div/a/div/span"))).click()
        # WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
        # (By.XPATH, "//input[@class='SearchInputBox__input']"))).send_keys("songs")
        driver.find_element_by_css_selector('[data-testid="search-input"]').click()

    def test(self):
        username="shashank.shukla1947@gmail.com"
        password=""
        driver = webdriver.Chrome(r"E:\C\Python\test\Selenium Tutorial\Drivers\chromedriver.exe")
        driver.get("https://open.spotify.com/browse/featured")

        driver.find_element_by_xpath("//span[text()='Search']").click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input"))).send_keys("Aadat")

        driver.find_element_by_xpath("//button[text()='Log in']").click()

        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@id='login-username']"))).send_keys(username)
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@id='login-password']"))).send_keys(password)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//button[@id='login-button']"))).click()
        items = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='react-contextmenu-wrapper']/div/div/a")))
        print(len(items))


    def xPath(self):
        driver = webdriver.Chrome(r"E:\C\Python\test\Selenium Tutorial\Drivers\chromedriver.exe")
        driver.get("https://www.amazon.in/")

        driver.find_element_by_xpath("//div[@id='nav-tools']/a[@class='nav-a nav-a-2 nav-progressive-attribute']").click()


o1 = myClass()
# o1.getText()
#
# o1.preProcess()
# o1.automate()
o1.test()
#o1.xPath()
