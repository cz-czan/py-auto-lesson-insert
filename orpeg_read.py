from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import datetime
def getCurrentWeek(driver, p_orpeg_login, p_orpeg_pswd):
    class Lekcja:
        def __init__(self, czas, lekcja, dzien_tygodnia):
            self.time = czas
            self.name =  lekcja
            self.week_day_number = dzien_tygodnia

    def calculateWeekDay(p_left_css_attribute):
        #weekday_dict = {0: 'mon', 1: 'tue', 2: 'wed', 3: 'thu', 4: 'fri', 5: 'sat', 6: 'sun'} for the sake of simplicity
        #when later defining the calculateDate function, returning the short for the weekday has been depracted

        p_left_css_attribute = p_left_css_attribute - 62
        x = (p_left_css_attribute - (p_left_css_attribute % 118)) / 118
        return x

    driver.get('https://nowa.otwartaszkola.pl/student/')
    el_orpeg_login_form = driver.find_element_by_id("j_username")
    el_orpeg_pswd_form = driver.find_element_by_id("j_password")
    el_orpeg_submit = driver.find_element_by_id("LoginButton_DoLogin")

    # Logging into ORPEG acc
    el_orpeg_login_form.send_keys(p_orpeg_login)
    el_orpeg_pswd_form.send_keys(p_orpeg_pswd)
    el_orpeg_submit.click()

    # throwing login, pass, and submit elements into the trash
    del el_orpeg_submit
    del el_orpeg_login_form
    del el_orpeg_pswd_form

    # Entering Plan Lekcji
    driver.find_element_by_css_selector('#menu > li:nth-child(3)').click()

    # Getting list of lesson elements along with the date ( day of week ) etc
    time.sleep(1)
    lekcja_list = []
    lesson_element_list = driver.find_elements_by_class_name('fc-event-vert')
    for x in lesson_element_list:
        y = Lekcja(x.find_elements_by_class_name('fc-event-time\n')[0].get_property('innerText'),
                   x.find_elements_by_class_name('fc-event-title\n')[0].get_property('innerText'),
                   calculateWeekDay(int(x.value_of_css_property('left').split('px')[0])))
        lekcja_list.append(y)

    for x in lekcja_list: #the prints are for development purposes
        print(x.name)
        print(x.time)
        print(x.week_day_number)
        print('\n')
    return lekcja_list