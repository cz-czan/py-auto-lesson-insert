
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import getpass

def logIntoGoogle(p_webdriver, p_login, p_pswd, p_url = None):
    if p_url == None:
        pass
    else:
        p_webdriver.get(p_url)
    email_element = p_webdriver.find_element_by_id("identifierId")
    email_element.send_keys(p_login)
    p_webdriver.find_element_by_id("identifierNext").click()
    time.sleep(1)

    pswd_input_element = WebDriverWait(p_webdriver, 20).until(
        EC.element_to_be_clickable((By.ID, "password")))

    actions = ActionChains(p_webdriver)
    actions.move_to_element(pswd_input_element)
    actions.click()
    actions.send_keys(p_pswd)
    actions.perform()
    p_webdriver.find_element_by_id("passwordNext").click()
    #if __name__ != '__main__':
     #   p_webdriver.quit()

if __name__ == '__main__':
    from sys import argv
    driver = webdriver.Chrome(options = Options())
    logIntoGoogle(argv[1], argv[2], argv[3], p_url="https://calendar.google.com/calendar/r")
