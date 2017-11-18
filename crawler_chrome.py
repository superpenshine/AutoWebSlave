from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import os

#user parameteres
driver_path = 'C:/Users/SIMSHEN/Downloads/AutoWebSlave/chromedriver.exe'
jenkins_server_domain = "tst-ci.th.gov.bc.ca"
jenkins_project_name = "slave"
jenkins_username = "SIMSHEN"
jenkins_password = "Zsh462404"

url = "https://" + jenkins_server_domain + "/jenkins/job/"+ jenkins_project_name +"/configure"
chrome_driver = driver_path
os.environ["webdriver.chrome.driver"] = chrome_driver        
browser = webdriver.Chrome(chrome_driver)
browser.get(url)

#handle login page first
username = browser.find_element_by_xpath("//input[@name='j_username']")
password = browser.find_element_by_xpath("//input[@name='j_password']")

username.send_keys(jenkins_username)
password.send_keys(jenkins_password)

#browser.find_element_by_xpath("//button[@id = 'yui-gen1-button']").click()
browser.find_element_by_xpath("//button[text()='log in']").click()

#browser.find_element_by_xpath("//button[text()='Add build step']").click()
#browser.find_element_by_xpath("//a[text()='Execute SonarQube Scanner']").click();

#fill in the configuration and quit
try:

	add_build_step = WebDriverWait(browser, 15).until(
		expected_conditions.visibility_of(browser.find_element_by_xpath("//button[text()='Add build step']")))
	add_build_step.click()
	print ("Page is ready!")
except TimeoutException:
	print ("Loading took too much time!")










######project = driver.find_element_by_xpath("/html/body/div[@id='page-body']/div[@id='main-panel']/div[@class='dashboard']/div[2]/table/tbody/tr[@id='job_demo']/td[3]/a")