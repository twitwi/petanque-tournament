from selenium import webdriver
from driver import *
import data as cfg

def login():
    driver.get('https://www.gandi.net/login')
    e = driver.find_element_by_id("logintext")
    e.send_keys(cfg.user+'\t') 
    implicit(100) # seconds
    driver.find_element_by_css_selector("a[href='/login/out']")
    defaultImplicit()

def updateForward(base, newValue):
    driver.get('https://www.gandi.net/admin/domain/'+cfg.gandiDomain+'/email/forward/update/forward-'+base)
    e = driver.find_element_by_id("account")
    if e.get_attribute('value') == '':
        return False
    e = driver.find_element_by_id("forward")
    e.clear()
    e.send_keys(newValue)
    e = driver.find_element_by_css_selector(".button.primary[type='submit']")
    e.click()
    e = driver.find_element_by_css_selector(".filter_link.xport")
    return True

def newForward(base, newValue):
    driver.get('https://www.gandi.net/admin/domain/'+cfg.gandiDomain+'/email/create?f=1')
    e = driver.find_element_by_id("account")
    e.clear()
    e.send_keys(base)
    e = driver.find_element_by_id("forward")
    e.clear()
    e.send_keys(newValue)
    e = driver.find_element_by_css_selector(".button.primary[type='submit']")
    e.click()
    e = driver.find_element_by_css_selector(".filter_link.xport")

def setForward(base, newValue):
    if not updateForward(base, newValue):
        newForward(base, newValue)

# login()
# for i in ['remi-92-4b2e', 'remi-93-b497', 'remi-94-ff94', 'remi-95-230b', 'remi-96-d1b1']:
#     implicit(100) # seconds
#     setForward(i, 'blabla@heeere.com')
#     defaultImplicit()


### EXAMPLE
# cat /dev/urandom | hexdump -C | awk '{i = i + 1; printf("remi-%02d-%s%s@heeere.com -- \n", i, $2, $3,$4,$5)}' | head -20 >> mails.txt
# ipython

# import gandi
# gandi.login()

# with open('mails.txt') as f:
#     for l in f:
#         if l.endswith('@heeere.com -- \n'):
#             gandi.setForward(l[:-16], 'remi@heeere.com')

