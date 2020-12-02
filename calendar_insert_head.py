from google_login import logIntoGoogle
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


def insert_event(p_driver, p_title, p_desc, p_start_date, p_start_time, p_end_time,p_end_date,):
    def tab():
        time.sleep(0.6)
        dummyactoinchain = ActionChains(p_driver)
        dummyactoinchain.send_keys(Keys.TAB)
        dummyactoinchain.perform()
    def enter():
        time.sleep(0.6)
        dummyactoinchain = ActionChains(p_driver)
        dummyactoinchain.send_keys(Keys.ENTER)
        dummyactoinchain.perform()
    def type(string):
        time.sleep(0.6)
        dummyactionchain = ActionChains(p_driver)
        dummyactionchain.send_keys(string)
        dummyactionchain.perform()

    time.sleep(1)
    create_button = p_driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[1]')
    create_button.click()

    type(p_title)

    tab()
    tab()

    type(p_start_date)

    tab()

    type(p_start_time)

    tab()

    type(p_end_time)

    tab()

    type(p_end_date)

    tab()
    tab()
    tab()
    enter()
    time.sleep(0.5)
    type(p_desc)

    tab()

    enter()
    type(Keys.ARROW_DOWN)
    enter()

    tab()
    tab()



    enter()

