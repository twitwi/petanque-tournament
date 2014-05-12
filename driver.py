from selenium import webdriver

driver = webdriver.Firefox()

def setTextArea(txtId, txtValue):
    e = driver.find_element_by_id(txtId)
    e.clear()
    e.send_keys(txtValue)

def clickCss(cssSelector):
    e = driver.find_element_by_css_selector(cssSelector)
    e.click()

def waitForCss(cssSelector):
    e = driver.find_element_by_css_selector(cssSelector)

def implicit(n):
    driver.implicitly_wait(n) # seconds

def defaultImplicit():
    implicit(10)

defaultImplicit()

