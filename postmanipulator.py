#this was quickly hacked up... I am going to refactor this shit big time and add a spammer as well and pageclasses
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import sys
import time

def loginToFacebook(driver, username, password):
    #driver = webdriver.Remote(command_executor='http://localhost:9515', desired_capabilities=DesiredCapabilities.CHROME)#Chrome()
    driver.get("http://www.facebook.com")
    time.sleep(4)
    driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(username)
    driver.find_element(By.XPATH, '//*[@id="pass"]').send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="u_0_n"]').click()
    
def removeTopPost(driver):
    time.sleep(4)
    driver.find_element(By.XPATH, '//*[@id="u_jsonp_2_16"]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="u_h_0"]/div/ul/li[8]/a/span/span').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="u_s_1"]/div[3]/button').click()

def gotoProfile(driver):
    time.sleep(4)
    driver.find_element(By.XPATH, '//*[@id="pagelet_welcome_box"]/div/div/div/div[2]/a[1]').click()
    
def main():
    driver = webdriver.Remote(command_executor='http://localhost:9515', desired_capabilities=DesiredCapabilities.CHROME)
    username = "haarisabbasi@gmail.com"#sys.argv[0]
    password = "Wutang"#sys.argv[1]
    loginToFacebook(driver,username, password)
    gotoProfile(driver)
    counter = 1
    while counter > 0:
        removeTopPost(driver)
        counter = counter -1


if __name__ == "__main__":
    main()
  
