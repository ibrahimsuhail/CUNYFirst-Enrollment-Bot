import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.webdriver.firefox.webdriver
from twilio.rest import Client
import smtplib
import time

'''change these variables to fit your needs'''
'''Go to twilio.com and create a free account'''
                          

accountsid =  'YOUR TWILIO SID'                # accountsid for twilio account, required to receive texts
authtoken =   'YOUR TWILIO AUTH TOKEN'                # authtoken for twilio account, required to receive texts
mycellphone = 'YOUR CELL #'                # your cell phone number
twiliocell =  'YOUR TWILIO #'                 # twilio cellnumber that will be used to send texts to your actual phone
username =    'YOUR CUNYFIRST USERNAME@login.cuny.edu'               # CUNYFIRST USERNAME           
password =    'YOUR CUNYFIRST PASSWORD'       
# refresh interval in seconds          
interval = 30
user = 'ANOTHER EMAIL THAT WILL SEND U THE EMAIL'
pwd = 'Above emails password'
recipient = '' # ur main email
subject='CUNYFIRST ENROLLMENT SHOPPING CART'
body = 'CLASS PROB OPEN'

def textmyself(message):
        twilioCli = Client(accountsid, authtoken)
        twilioCli.messages.create(body=message, from_=twiliocell, to=mycellphone)
        print("successfully sent the text")

def send_email(user, pwd, recipient, subject, body):
    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
            """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print('successfully sent the mail')
    except:
        print("failed to send mail")
    
'''Add shopping cart link is very important to this script. Go to CUNYFIRST, Click Enroll. Then choose your Term.
    Once you are are on the Shopping Cart Page, Right + Click on 'add' and Click on 'Copy Link Location'.
    Then copy and paste in here with single quotes. It should look like the link below'''
 
# CHANGE    THESE TWO VARIABLES
addshoppingcartlink = 'https://cssa.cunyfirst.cuny.edu/psc/cnycsprd/EMPLOYEE/CAMP/c/SA_LEARNER_SERVICES_2.SSR_SSENRL_CART.GBL?Page=SSR_SSENRL_CART&Action=A&ACAD_CAREER=UGRD&EMPLID=23641362&ENRL_REQUEST_ID=&INSTITUTION=QNS01&STRM=1212'
driver = webdriver.Firefox(executable_path='PATH TO geckodriver') #if on pc swith / with \ and add "r" before 'PATH

print("Starting Firefox and heading to CUNYFIRST")
driver.get('https://home.cunyfirst.cuny.edu')
login = WebDriverWait(driver, timeout=30).until(
    EC.presence_of_element_located((By.NAME, "usernameH")))
login.clear()
login.send_keys(username)
passs = driver.find_element_by_name("password")
passs.send_keys(password, Keys.ENTER)
driver.implicitly_wait(30)
studentcenter = WebDriverWait(driver, timeout=30).until(
    EC.presence_of_element_located((By.LINK_TEXT, "Student Center")))
studentcenter.click()
driver.get(addshoppingcartlink)
shoppingcartlen = len(driver.find_elements_by_xpath("//table[@id='SSR_REGFORM_VW$scroll$0']/tbody/tr")) - 2
shoppingcart = {}

    
latestshoppingcart = {}
latestshoppingcartclasses = len(
    driver.find_elements_by_xpath("//table[@id='SSR_REGFORM_VW$scroll$0']/tbody/tr")) - 2

while True:
    driver.refresh()
    for i in range(0, latestshoppingcartclasses):
        classname = driver.find_element_by_id("win0divP_CLASS_NAME$" + str(i)).text
        status = driver.find_element_by_xpath(
            "//div[@id='win0divDERIVED_REGFRM1_SSR_STATUS_LONG$" + str(i) + "']/div/img").get_attribute('alt')
        latestshoppingcart[classname] = status
        if (status == "Open"): 
            # uncomment if u want email notification
            # send_email(user, pwd, recipient, subject, body) 
            textmyself("class open!!!")
            print(status)      
            print(str(i))
            cb = 'P_SELECT${0}'.format(i) 
            print(cb)  
            driver.find_element_by_id(cb).click()
            driver.execute_script("javascript:submitAction_win0(document.win0,'DERIVED_REGFRM1_LINK_ADD_ENRL');")
            driver.find_element_by_css_selector("#DERIVED_REGFRM1_SSR_PB_SUBMIT").click()
            

        else: 
            print(status)
            # uncomment to test texting
            # textmyself("test")
            # break
            
    print("refresh in {0} seconds".format(interval))
    time.sleep(interval)
        