from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from orpeg_read import getCurrentWeek
from google_login import logIntoGoogle
from calendar_insert_head import insert_event
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import datetime
import getpass
import time
import string
cr_opts = Options()

driver = webdriver.Chrome(options= cr_opts)


lesson_list = getCurrentWeek(driver, input("\nORPEG login:"), getpass.getpass(prompt="\nORPEG pswd:"))


logIntoGoogle(driver, input('\nGoogle login:'), getpass.getpass(prompt='\nGoogle pswd:'),
              p_url='https://calendar.google.com/calendar/r/week')


def calculateDate(p_lesson_weekday_number):
    dict_weekday = {'Mon': 0, 'Tue': 1, 'Wed': 2, 'Thu': 3, 'Fri': 4, 'Sat': 5, 'Sun': 6}
    var_today_weekday = datetime.datetime.now().strftime("%a")
    var_today_weekday_number = dict_weekday[var_today_weekday]
    if var_today_weekday_number == p_lesson_weekday_number:
        return datetime.datetime.now()
    desired_date = None
    if p_lesson_weekday_number > var_today_weekday_number:
        desired_date = datetime.datetime.now() + \
                       datetime.timedelta(days=p_lesson_weekday_number - var_today_weekday_number)
    else:
        desired_date = datetime.datetime.now() - \
                       datetime.timedelta(days=var_today_weekday_number - p_lesson_weekday_number)
    return desired_date

def formatDate(p_datetime_object):
    #this function formats a datetime object into a string for google calendar
    string = ''
    string += p_datetime_object.strftime('%b %d, %Y')

user = input("\nUser's name:")

for lesson in lesson_list:
    insert_event(driver, user + ' ' + lesson.name, 'inserted by auto_lesson_insert',
                 calculateDate(lesson.week_day_number).strftime('%b %d, %Y'),
                 lesson.time.split(' - ')[0] + 'am', lesson.time.split(' - ')[1] + 'am',
                 calculateDate(lesson.week_day_number).strftime('%b %d, %Y')
                 )