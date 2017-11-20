from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import os, time

#user parameteres

jenkins_username = "SIMSHEN"
jenkins_password = "Zsh462404"
driver_path = "C:/Users/SIMSHEN/Downloads/AutoWebSlave/geckodriver.exe"
jenkins_project_name = "slave"
session_context_name = "http://rip-my-professor.herokuapp.com.*"

jenkins_project_initial_version = "1.0"
jenkins_server_domain = "tst-ci.th.gov.bc.ca"
sonar_admin_username = "admin"
sonar_admin_password = "test"
sonar_auth = "false"
session_name = "zap_session"
session_include_in_context = "http://rip-my-professor.herokuapp.com.*"

#parse info
url = "https://" + jenkins_server_domain + "/jenkins/job/"+ jenkins_project_name +"/configure"
firefox_driver = driver_path
properties = "sonar.projectKey = "+jenkins_project_name
properties += "\nsonar.projectName = "+jenkins_project_name
properties += "\nsonar.projectVersion = "+jenkins_project_initial_version
properties += "\nsonar.sources = D:\\\\Jenkins_ci\\\\Jenkins\\\\jobs\\\\"+jenkins_project_name+"\\\\workspace"
properties += "\nsonar.login = "+sonar_admin_username
properties += "\nsonar.password = "+sonar_admin_password
properties += "\nsonar.forthAuthentication = "+sonar_auth


os.environ["webdriver.chrome.driver"] = firefox_driver        
browser = webdriver.Firefox()
browser.get(url)

#handle login page first
username = browser.find_element_by_xpath("//input[@name='j_username']")
password = browser.find_element_by_xpath("//input[@name='j_password']")

username.send_keys(jenkins_username)
password.send_keys(jenkins_password)

browser.find_element_by_xpath("//button[text()='log in']").click()

#fill in the configuration and quit + loading configuration wait
try:
	#killing the save button
	stupid = WebDriverWait(browser, 150).until(
		expected_conditions.element_to_be_clickable((By.XPATH, "//div[@class='bottom-sticker-inner']")))

	browser.execute_script("arguments[0].style = arguments[1]", stupid, "display: none;")
	time.sleep(1)

	browser.find_element_by_xpath("//button[text()='Add build step']").click()
	browser.find_element_by_xpath("//a[text()='Execute SonarQube Scanner']").click();

	browser.find_element_by_xpath("//button[text()='Add build step']").click()
	browser.find_element_by_xpath("//a[text()='Execute ZAP']").click();

	print ("Adding SonarQube/Owasp ZAP build step finishes!")

except TimeoutException:

	print ("Loading configure page took too much time!")

#sonar
try:
	sonar_properties = WebDriverWait(browser, 150).until(
		expected_conditions.element_to_be_clickable((By.XPATH, "//textarea[@name='_.properties']")))
	sonar_properties.send_keys(properties);

	browser.find_element_by_xpath("//input[@id='textarea._.additionalArguments']").send_keys("-X")

	print ("sonar plugin configuration finished!")

except TimeoutException:

	print ("Sonar plugin-load timeout !")

#zap
try:
	custom_tools_installation = WebDriverWait(browser, 150).until(
	expected_conditions.element_to_be_clickable((By.XPATH, "//label[normalize-space(text())='System Installed: ZAP Installation Directory']/input")))
	custom_tools_installation.click()

	browser.find_element_by_xpath("//input[@name='_.zapSettingsDir']").send_keys("d:\\Jenkins_ci\\ZedAttackProxy")

	persist_session = browser.find_element_by_xpath("//label[normalize-space(text())='Persist Session']/input")
	persist_session.click()
	persist_session.click()

	browser.find_element_by_xpath("//input[@checkdependson='sessionFilename']").send_keys(session_name)

	browser.find_element_by_xpath("//input[@name='_.contextName']").send_keys(session_context_name)

	browser.find_element_by_xpath("//textarea[@name='_.includedURL']").send_keys(session_include_in_context)

	#authentication

	zap_authentication = browser.find_element_by_xpath("//input[@name='_.authMode']")
	zap_authentication.click()

	

	print ("sonar plugin configuration finished!")

except TimeoutException:

	print ("Sonar plugin-load timeout !")
