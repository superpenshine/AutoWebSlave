from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import os, time

#user parameteres

jenkins_username = "SIMSHEN"
jenkins_password = "Zsh462404"
driver_path = 'C:/Users/SIMSHEN/Downloads/AutoWebSlave/geckodriver.exe'
jenkins_project_name = "slave"

jenkins_project_initial_version = "1.0"
jenkins_server_domain = "tst-ci.th.gov.bc.ca"
sonar_admin_username = "admin"
sonar_admin_password = "test"
sonar_auth = "false"

#parse info
url = "https://" + jenkins_server_domain + "/jenkins/job/"+ jenkins_project_name +"/configure"
chrome_driver = driver_path
properties = "sonar.projectKey = "+jenkins_project_name
properties += "\nsonar.projectName = "+jenkins_project_name
properties += "\nsonar.projectVersion = "+jenkins_project_initial_version
properties += "\nsonar.sources = D:\\\\Jenkins_ci\\\\Jenkins\\\\jobs\\\\"+jenkins_project_name+"\\\\workspace"
properties += "\nsonar.login = "+sonar_admin_username
properties += "\nsonar.password = "+sonar_admin_password
properties += "\nsonar.forthAuthentication = "+sonar_auth


os.environ["webdriver.chrome.driver"] = chrome_driver        
browser = webdriver.Firefox()
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

#fill in the configuration and quit + loading configure wait
try:
	#killing the save button
	stupid = WebDriverWait(browser, 15).until(
		expected_conditions.element_to_be_clickable((By.XPATH, "//div[@class='bottom-sticker-inner']")))
	browser.execute_script("arguments[0].style = arguments[1]", stupid, "display: none;")
	time.sleep(1)
	browser.find_element_by_xpath("//button[text()='Add build step']").click()
	print ("Wait phase 1 finishes!")

except TimeoutException:
	print ("Loading took too much time!")

#waitwait for sonar plugin-list-load
try:
	execute_sonar = WebDriverWait(browser, 15).until(
		expected_conditions.element_to_be_clickable((By.XPATH, "//a[text()='Execute SonarQube Scanner']")))
	execute_sonar.click()

except TimeoutException:
	print ("Wait phase 2 finisehs !")

#wait for soanr plugin-load
try:
	execute_sonar = WebDriverWait(browser, 15).until(
		expected_conditions.element_to_be_clickable((By.XPATH, "//a[text()='Execute SonarQube Scanner']")))
	execute_sonar.click()

except TimeoutException:
	print ("Wait phase 2 finisehs !")
	sonar_properties = WebDriverWait(browser, 15).until(
		expected_conditions.element_to_be_clickable((By.XPATH, "//textarea[@name='_.properties']")))
	sonar_properties.send_keys(properties);

