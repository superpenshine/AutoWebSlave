from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import os, time

def set_up_driver(firefox_driver):

	os.environ["webdriver.firefox.driver"] = firefox_driver


def jenkins_login(jenkins_username, jenkins_password):

	username = browser.find_element_by_xpath("//input[@name='j_username']")
	password = browser.find_element_by_xpath("//input[@name='j_password']")

	username.send_keys(jenkins_username)
	password.send_keys(jenkins_password)

	browser.find_element_by_xpath("//button[text()='log in']").click()


def add_build_steps(browser):

	add_build_step_button = WebDriverWait(browser, 150).until(
			expected_conditions.element_to_be_clickable((By.XPATH, "//button[text()='Add build step']")))

	if (not SonarQube_AlreadyExsist(browser)):

		add_build_step_button.click()
		WebDriverWait(browser, 150).until(
			expected_conditions.element_to_be_clickable((By.XPATH, "//a[text()='Execute SonarQube Scanner']"))).click()

	if (not ZAP_AlreadyExsist(browser)):

		add_build_step_button.click()
		WebDriverWait(browser, 150).until(
			expected_conditions.element_to_be_clickable((By.XPATH, "//a[text()='Execute ZAP']"))).click()


def SonarQube_AlreadyExsist(browser):

	try:
		browser.find_element_by_xpath("//b[text()='Execute SonarQube Scanner']")

	except:
		return False

	return True


def ZAP_AlreadyExsist(browser):

	try:
		browser.find_element_by_xpath("//b[text()='Execute ZAP']")

	except:
		return False

	return True


def set_up_sonar(browser, properties):

	sonar_properties = WebDriverWait(browser, 150).until(
		expected_conditions.element_to_be_clickable((By.XPATH, "//textarea[@name='_.properties']")))
	sonar_properties.clear()
	sonar_properties.send_keys(properties)

	sonar_arguments = WebDriverWait(browser, 150).until(
		expected_conditions.element_to_be_clickable((By.XPATH, "//input[@id='textarea._.additionalArguments']")))
	sonar_arguments.clear()
	sonar_arguments.send_keys("-X")


def set_up_zap(browser, session_name, session_context_name, session_include_in_context):

	custom_tools_installation = WebDriverWait(browser, 150).until(
		expected_conditions.element_to_be_clickable((By.XPATH, "//label[normalize-space(text())='System Installed: ZAP Installation Directory']/input")))
	custom_tools_installation.click()

	zap_setting_dir = WebDriverWait(browser, 150).until(
		expected_conditions.element_to_be_clickable((By.XPATH, "//input[@name='_.zapSettingsDir']")))
	zap_setting_dir.clear()
	zap_setting_dir.send_keys("d:\\Jenkins_ci\\ZedAttackProxy")

	persist_session = WebDriverWait(browser, 150).until(
		expected_conditions.element_to_be_clickable((By.XPATH, "//label[normalize-space(text())='Persist Session']/input")))
	persist_session.click()
	#persist_session.click()

	session_name_field = WebDriverWait(browser, 150).until(
		expected_conditions.element_to_be_clickable((By.XPATH, "//input[@checkdependson='sessionFilename']")))
	session_name_field.clear()
	session_name_field.send_keys(session_name)

	session_context_name_field = WebDriverWait(browser, 150).until(
		expected_conditions.element_to_be_clickable((By.XPATH, "//input[@name='_.contextName']")))
	session_context_name_field.clear()
	session_context_name_field.send_keys(session_context_name)

	session_include_in_context_field = WebDriverWait(browser, 150).until(
		expected_conditions.element_to_be_clickable((By.XPATH, "//textarea[@name='_.includedURL']")))
	session_include_in_context_field.clear()
	session_include_in_context_field.send_keys(session_include_in_context)

	generate_report = WebDriverWait(browser, 150).until(
		expected_conditions.element_to_be_clickable((By.XPATH, "//input[@name='_.generateReports']")))
	generate_report.click()
	generate_report.click()

	generate_report_format = WebDriverWait(browser, 150).until(
		expected_conditions.element_to_be_clickable((By.XPATH, "//select[@name='selectedReportFormats']/option[text()='html']")))
	generate_report_format.click()

	#scanning options
	spider_scan = WebDriverWait(browser, 150).until(
		expected_conditions.element_to_be_clickable((By.XPATH, "//label[text()='Spider Scan']")))
	spider_scan.click()
	spider_scan.click()


def set_up_zap_auth(browser, website_login_name, website_login_password, website_logged_in_indicator, login_form_target, username_parameter, password_parameter, starting_point):

	auth = WebDriverWait(browser, 150).until(
		expected_conditions.element_to_be_clickable((By.XPATH, "//input[@name='_.authMode']")))
	auth.click()
	auth.click()

	auth_username_field = WebDriverWait(browser, 150).until(
		expected_conditions.element_to_be_clickable((By.XPATH, "//td[@class='setting-main']/table/tbody/tr/td/input[@name='_.username']")))
	auth_username_field.clear()
	auth_username_field.send_keys(website_login_name)

	auth_password = WebDriverWait(browser, 150).until(
		expected_conditions.element_to_be_clickable((By.XPATH, "//td[@class='setting-main']/table/tbody/tr/td/input[@name='_.password']")))
	auth_password.clear()
	auth_password.send_keys(website_login_password)

	auth_in_indi_field = WebDriverWait(browser, 150).until(
		expected_conditions.element_to_be_clickable((By.XPATH, "//td[@class='setting-main']/table/tbody/tr/td/input[@name='_.loggedInIndicator']")))
	auth_in_indi_field.clear()
	auth_in_indi_field.send_keys(website_logged_in_indicator)
#
	auth_target_field = WebDriverWait(browser, 150).until(
		expected_conditions.element_to_be_clickable((By.XPATH, "//td[@class='setting-main']/table/tbody/tr/td/input[@name='_.loginURL']")))
	auth_target_field.clear()
	auth_target_field.send_keys(login_form_target)

	auth_username_parameter_field = WebDriverWait(browser, 150).until(
		expected_conditions.element_to_be_clickable((By.XPATH, "//td[@class='setting-main']/table/tbody/tr/td/input[@name='_.usernameParameter']")))
	auth_username_parameter_field.clear()
	auth_username_parameter_field.send_keys(username_parameter)

	auth_password_parameter_field = WebDriverWait(browser, 150).until(
		expected_conditions.element_to_be_clickable((By.XPATH, "//td[@class='setting-main']/table/tbody/tr/td/input[@name='_.passwordParameter']")))
	auth_password_parameter_field.clear()
	auth_password_parameter_field.send_keys(password_parameter)

	starting_point_field = WebDriverWait(browser, 150).until(
		expected_conditions.element_to_be_clickable((By.XPATH, "//td[@class='setting-main']/input[@name='_.targetURL']")))
	starting_point_field.clear()
	starting_point_field.send_keys(starting_point)

#default user parameteres

jenkins_username = "SIMSHEN"
jenkins_password = "Zsh462404"
driver_path = "C:/Users/SIMSHEN/Downloads/AutoWebSlave/geckodriver.exe"
jenkins_project_name = "slave"
session_context_name = "Demo"
session_include_in_context = "http://rip-my-professor.herokuapp.com.*"
website_login_name = "hshen"
website_login_password = "1234qwer"
website_logged_in_indicator = "\Q<title>Site administration | Django site admin</title>\E"
login_form_target = "http://rip-my-professor.herokuapp.com/admin/login/?next=/admin/"
username_parameter = "username"
password_parameter = "password"
starting_point = "http://rip-my-professor.herokuapp.com/admin/"

#default optional parameters

jenkins_project_initial_version = "1.0"
jenkins_server_domain = "tst-ci.th.gov.bc.ca"
sonar_admin_username = "admin"
sonar_admin_password = "test"
sonar_auth = "false"
session_name = "zap_session"
authentication_required = True

#parse info

with open("configure.txt") as f:
	content = f.readlines()

for line in content:

	if (line[0] != '#' and line[0] != '\n'):

		name, value = line.rstrip('\n').split(' = ')

		if (name == 'jenkins_username'):
			jenkins_username = value
			continue
		if (name == 'jenkins_password'):
			jenkins_password = value
			continue
		if (name == 'driver_path'):
			driver_path = value
			continue
		if (name == 'jenkins_project_name'): 
			jenkins_project_name = value
			continue
		if (name == 'session_context_name'):
			session_context_name = value
			continue
		if (name == 'session_include_in_context'):
			session_include_in_context = value;
			continue
		if (name == 'website_login_name'):
			website_login_name = value
			continue
		if (name == 'website_login_password'):
			website_login_password = value
			continue
		if (name == 'website_logged_in_indicator'):
			website_logged_in_indicator = value
			continue
		if (name == 'login_form_target'):
			login_form_target = value
			continue
		if (name == 'username_parameter'):
			username_parameter = value
			continue
		if (name == 'password_parameter'):
			password_parameter = value
			continue
		if (name == 'starting_point'):
			starting_point = value
			continue
		if (name == 'jenkins_project_initial_version'):
			jenkins_project_initial_version = value
			continue
		if (name == 'jenkins_server_domain'):
			jenkins_server_domain = value;
			continue
		if (name == 'sonar_admin_username'):
			sonar_admin_username = value
			continue
		if (name == 'sonar_admin_password'):
			sonar_admin_password = value
			continue
		if (name == 'sonar_auth'):
			sonar_auth = value
			continue
		if (name == 'session_name'):
			session_name = value
			continue
		if (name == 'authentication_required'):
			if (value == 'True'):authentication_required = True
			elif (value == 'False'): authentication_required = False
			continue
		else:
			raise Exception("Unknown parameter")

url = "https://" + jenkins_server_domain + "/jenkins/job/" + jenkins_project_name + "/configure"
firefox_driver = driver_path
properties = "sonar.projectKey = " + jenkins_project_name
properties += "\nsonar.projectName = " + jenkins_project_name
properties += "\nsonar.projectVersion = " + jenkins_project_initial_version
properties += "\nsonar.sources = D:\\\\Jenkins_ci\\\\Jenkins\\\\jobs\\\\" + jenkins_project_name + "\\\\workspace"
properties += "\nsonar.login = " + sonar_admin_username
properties += "\nsonar.password = " + sonar_admin_password
properties += "\nsonar.forthAuthentication = " + sonar_auth
session_context_name += "%{BUILD_ID}"

#main

set_up_driver(firefox_driver)
browser = webdriver.Firefox()
browser.get(url)

#handle login page first
jenkins_login(jenkins_username, jenkins_password)

#loading page and disable the save key
try:
	stupid = WebDriverWait(browser, 150).until(
		expected_conditions.element_to_be_clickable((By.XPATH, "//div[@class='bottom-sticker-inner']")))
	browser.execute_script("arguments[0].style = arguments[1]", stupid, "display: none;")

except TimeoutException:
	print ("Loading configuration page took too much time !")

#loading configuration wait
try:
	add_build_steps(browser)
	print ("Adding SonarQube/Owasp ZAP build steps finishes!")

except TimeoutException:
	print ("Adding SonarQube/Owasp Zap build steps took too much time!")

#sonar
try:
	set_up_sonar(browser, properties)
	print ("sonar plugin configuration finished!")

except TimeoutException:
	print ("Sonar plugin-load timeout !")

#zap
try:
	set_up_zap(browser, session_name, session_context_name, session_include_in_context)
	#authentication
	if (authentication_required):
		set_up_zap_auth(browser, website_login_name, website_login_password, website_logged_in_indicator, login_form_target, username_parameter, password_parameter, starting_point)
	
	print ("zap plugin configuration finished!")

except TimeoutException:
	print ("Sonar plugin-load timeout !")

#recover the save button
try:
	browser.execute_script("arguments[0].style = arguments[1]", stupid, "display: ;")

except:
	print("Error recovering save button")