from selenium import webdriver
from driver import *

def createNewUser(name, email, passwd):
    driver.get('http://www.protournoi.fr/inscription-classique')
    setTextArea('taikai_joueur_registration_username', name)
    setTextArea('taikai_joueur_registration_email', email)
    setTextArea('taikai_joueur_registration_plainPassword_first', passwd)
    setTextArea('taikai_joueur_registration_plainPassword_second', passwd)
    clickCss('#taikai_joueur_registration_typeInscription_1')
    clickCss('.btn.btn-submit[type="submit"]')
    waitForCss('.btn[href="/logout"]')

def invite(people): # needs to have an open window at the right page
    setTextAreaXpath('//*[@id="taikai_tournoibundle_joueursanonymestype_joueursAnonymes"]/descendant::input[@type="text"][last()]', people)
    clickCss('.btn#ajout_invite')

def submitInvites():
    clickCss('.btn#joueurs_anonymes_submit')
