from fnmatch import fnmatch
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.ui import Select
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
import time

from selenium.webdriver.remote import webelement

# path to chromdriver
PATH = "C:\chromedriver.exe"

driver = webdriver.Chrome(PATH)


application_url = driver.get('https://nasacentral.force.com/s/application/a03t000000CtjtCAAR/app859735')
time.sleep(3)
#log in info
user_name = driver.find_element_by_id('47:2;a').send_keys('YOUR USERNAME HERE')
pass_word = driver.find_element_by_id('59:2;a').send_keys('YOUR PASSWORD HERE')
time.sleep(1)
# click log in 
login_click = driver.find_element_by_xpath('//*[@id="centerPanel"]/div/div[2]/div/div[2]/div/div[3]').click()
time.sleep(3)
#click next
first_next_click = driver.find_element_by_xpath('//*[@id="flowContainer"]/article/div/div[3]/footer/div[2]').click()
time.sleep(8)
#enter gpa and click next
try:
    gpa_xpath = '//*[@id="CustomerPortalTemplate"]/div[2]/div/div[2]/div[1]/div/div/article/div/div/div[2]/div/div/div[3]/flowruntime-flow-screen-input/flowruntime-input-wrapper2/div/lightning-input/div'
    gpa_enter = driver.find_element_by_xpath(gpa_xpath).click()
    gpa_enter.send_keys(3.5)
    gpa_next_xpath = '//*[@id="CustomerPortalTemplate"]/div[2]/div/div[2]/div[1]/div/div/article/div/div/div[2]/footer/div[2]/button'
    gpa_next_click = driver.find_element_by_xpath(gpa_next_xpath).click()
except:
    pass

#############################################################UNFINISHED###################################################

## select school and type stuff for school

# drop down school selection and dates
boulder_info = [['Boulder'], ['Aug 18, 2018', 'Jun 19, 2019']]
UTSA_info = [['San Antonio'], ['Aug 12, 2019', 'Jul 29, 2020']]
UT_info = [['Austin'], ['Jul 29, 2020', 'May 21, 2023']]

schools_info = [[],[]]
for i in range(2):
    school_enter_xpath = '//*[@id="CustomerPortalTemplate"]/div[2]/div/div[2]/div[1]/div/div/article/div/div/div[2]/flowruntime-lwc-body/div/flowruntime-list-container/div/flowruntime-screen-field[4]/flowruntime-list-container/div/flowruntime-screen-field/flowruntime-list-container/div/flowruntime-screen-field[1]/flowruntime-lwc-field/div/flowruntime-lookup/lightning-lookup/lightning-lookup-desktop/lightning-grouped-combobox/div[1]/div/lightning-base-combobox/div/div[1]'
    school_element = driver.find_element_by_xpath(school_enter_xpath)
    school_element.click()
    school_element.send_keys(school_names)
    time.sleep(5)
    school_element.send_keys(Keys.ARROW_DOWN)
    time.sleep(0.5)
    school_element.send_keys(Keys.RETURN)
    

#  major and minor selection
    major_xpath = '//*[@id="CustomerPortalTemplate"]/div[2]/div/div[2]/div[1]/div/div/article/div/div/div[2]/flowruntime-lwc-body/div/flowruntime-list-container/div/flowruntime-screen-field[4]/flowruntime-list-container/div/flowruntime-screen-field/flowruntime-list-container/div/flowruntime-screen-field[7]/flowruntime-lwc-field/div/flowruntime-lookup/lightning-lookup/lightning-lookup-desktop/lightning-grouped-combobox/div[1]/div/lightning-base-combobox/div/div[1]'
    minor_xpath = '//*[@id="CustomerPortalTemplate"]/div[2]/div/div[2]/div[1]/div/div/article/div/div/div[2]/flowruntime-lwc-body/div/flowruntime-list-container/div/flowruntime-screen-field[4]/flowruntime-list-container/div/flowruntime-screen-field/flowruntime-list-container/div/flowruntime-screen-field[8]/flowruntime-lwc-field/div/flowruntime-lookup/lightning-lookup/lightning-lookup-desktop/lightning-grouped-combobox/div/div/lightning-base-combobox/div/div[1]'
    school_element = driver.find_element_by_xpath(school_enter_xpath)
    school_element.click()
    school_element.send_keys(school_names)
    time.sleep(5)
    school_element.send_keys(Keys.ARROW_DOWN)
    time.sleep(0.5)
    school_element.send_keys(Keys.RETURN)
