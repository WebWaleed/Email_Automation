import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import sys
import contextlib

# Create a context manager to suppress stdout and stderr
class SuppressOutput(contextlib.ContextDecorator):
    def __enter__(self):
        self._stdout = sys.stdout
        self._stderr = sys.stderr
        sys.stdout = open(os.devnull, 'w')
        sys.stderr = open(os.devnull, 'w')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        sys.stdout.close()
        sys.stderr.close()
        sys.stdout = self._stdout
        sys.stderr = self._stderr



check=""
df = pd.read_csv('Result.csv')
emails = df['Email'].tolist()
passwords = df['Password'].tolist()



chrome_options = Options()
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument("--incognito")

check = input('Please enter an ISP from Yahoo, Gmail, and Outlook: ')
print('----------------------- isp seleted')
with SuppressOutput():
    driver = webdriver.Chrome(options=chrome_options)
if check == "gmail":
   
    driver.get("https://mail.google.com")
    time.sleep(3)
    
    email_input_xpath = "/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div[1]/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input"
    email_input = driver.find_element(By.XPATH, email_input_xpath)
    if emails:
        # email_input.send_keys(emails[0])
        for character in emails[0]:
            email_input.send_keys(character)
            time.sleep(0.1)
        next_button_xpath = '//*[@id="identifierNext"]/div/button'
        next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, next_button_xpath)))
        next_button.click()
    
    time.sleep(3)
    
    pass_input_xpath = "/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input"
    pass_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, pass_input_xpath)))
    
    if passwords:
        # pass_input.send_keys(passwords[0])
        for character in passwords[0]:
            pass_input.send_keys(character)
            time.sleep(0.3)
        sign_in_button_xpath = '//*[@id="passwordNext"]/div/button/span'
        sign_in_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, sign_in_button_xpath)))
        sign_in_button.click()
    
    time.sleep(3)
    user_input = int(input('1. Compose message and send mail: \n2. Read first mail from mailbox: \n3. Report first email from spam to not spam :\n\n select option: '))
    if user_input== 1:
        Compose_button_xpath = '/html/body/div[6]/div[3]/div/div[2]/div[1]/div[1]/div/div'
        Compose_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, Compose_button_xpath)))
        Compose_button.click()

    
        to_input_xpath = '//*[@class="agP aFw"]'
        to_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, to_input_xpath)))
        for i in emails:
            to_input.send_keys(i+",")
        subject_text = input("Enter the email subject: \n")
        subject_input_xpath = '//input[@name="subjectbox"]'
        subject_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, subject_input_xpath)))
        subject_input.send_keys(subject_text)
                
        sent_button_xpath = '/html/body/div[25]/div/div/div/div[1]/div[2]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/div/div/div[4]/table/tbody/tr/td[1]/div/div[2]/div[1]'
        
        sent_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, sent_button_xpath)))
        sent_button.click()
        time.sleep(3)
        driver.quit()
    elif user_input== 2:
        read_first_email_button_xpath = '/html/body/div[6]/div[3]/div/div[2]/div[2]/div/div/div/div[2]/div/div[1]/div/div/div[9]/div[1]/div[1]/div/div[1]/div[2]/div/table/tbody/tr[1]'
        read_first_email = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, read_first_email_button_xpath)))
        read_first_email.click()
        time.sleep(3)
        driver.quit()
    elif user_input== 3:
        more_button_xpath ='//*[@class="n6"]'
        more_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, more_button_xpath)))
        more_button.click()
        time.sleep(3)
        spam_button_xpath ='//*[@class="TN bzz aHS-bnv"]'
        spam_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, spam_button_xpath)))
        spam_button.click()
        time.sleep(3)
        try:
            nothing_in_spam_xpath ='//*[@id=":1"]/div/div[2]/div[5]/div[1]/div[1]/div[2]/table/tbody/tr/td'
            nothing_in_spam = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, nothing_in_spam_xpath)))
            print('------- Nothing in Spam -------')
            driver.quit()
        except:
            selct_button_xpath ='//*[@id=":o1"]'
            selct_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, selct_button_xpath)))
            selct_button.click()
            time.sleep(3)
            # nospam_button_xpath =' //*[@class="Bn"]' 
            nospam_button_xpath = '//*[@id=":1"]/div/div[2]/div[1]/div[2]/div[1]/div/div/div[3]/div'
            nospam_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, nospam_button_xpath)))
            nospam_button.click()
            
            time.sleep(3)
            driver.quit()
    else:
        print('----- Please select option from given list -----')
        time.sleep(3)
        driver.quit()

elif check=="yahoo":
  
    driver.get("https://login.yahoo.com/?.src=ym&pspid=159600001&activity=mail-direct&.lang=en-US&.intl=us&.done=https%3A%2F%2Fmail.yahoo.com%2Fd")
    time.sleep(3)
        
    email_input_xpath = "/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/form/div[1]/div[3]/input"
    email_input = driver.find_element(By.XPATH, email_input_xpath)
    
    if emails[1]:
        # email_input.send_keys(emails[1])
         for character in emails[1]:
            email_input.send_keys(character)
            time.sleep(0.1)
    next_button_xpath = '//*[@id="login-signin"]'
    next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, next_button_xpath)))
    next_button.click()
    
    time.sleep(3)
    
    pass_input_xpath = "/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/form/div[2]/input"
    pass_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, pass_input_xpath)))
    
    if passwords:
        # pass_input.send_keys(passwords[1])
        for characters in passwords[1]:
            pass_input.send_keys(characters)
            time.sleep(0.3)
    
    sign_in_button_xpath = '//*[@id="login-signin"]'
    sign_in_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, sign_in_button_xpath)))
    sign_in_button.click()
    user_input = int(input('1. Compose message and send mail: \n2. Read first mail from mailbox: \n3. Report first email from spam to not spam :\n\n select option: '))
    
    if user_input == 1:
        time.sleep(3)
        Compose_button_xpath = '//*[@id="mail-app-component-container"]/nav/div/div/button'
        Compose_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, Compose_button_xpath)))
        Compose_button.click()
    
        # //*[@id="message-to-field"]
        # subject_text = input("Enter the email subject: \n")
        to_input_xpath = '//*[@id="message-to-field"]'
        to_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, to_input_xpath)))
        for i in emails:
            to_input.send_keys(i+",")
        subject_text = input("Enter the email subject: \n")
        subject_input_xpath = '//*[@id="compose-subject-input"]'
        subject_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, subject_input_xpath)))
        subject_input.send_keys(subject_text)
        
        sent_button_xpath = '//*[@id="compose-styler"]/div/div[2]/div[2]/div[1]/div[1]/button'
        sent_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, sent_button_xpath)))
        sent_button.click()
        time.sleep(3)
        driver.quit()
        
    elif user_input== 3:
        
         More_button_xpath ='//*[@id="left-rail-more-menu"]/div/div'
         More_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, More_button_xpath)))
         More_button.click()
         time.sleep(3)
         spam_button_xpath ='//*[@id="left-rail-more-menu-item-2"]/div'
         spam_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, spam_button_xpath)))
         spam_button.click()
         time.sleep(3)
         try:
            nothing_in_spam_xpath ='//*[@id="mail-reader-container"]/div/div/div/div/div/div/div[1]/div/div/div/div'
            nothing_in_spam = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, nothing_in_spam_xpath)))
            print('------- Nothing in Spam -------')
            driver.quit()
         except:
             select_button_xpath ='//*[@id="mail-reader-container"]/div/div/div/div/div/div/div[1]/div/div/ul/li[2]/div/div[1]/span'
             select_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, select_button_xpath)))
             select_button.click()
             time.sleep(3)
             notspam_button_xpath ='//*[@id="mail-app-component-container"]/div[3]/div/div[2]/div/button[5]'
             notspam_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, notspam_button_xpath)))
             notspam_button.click()
         time.sleep(3)
         driver.quit()
    else:
        print('----- Please select option from given list -----')
        time.sleep(3)
        driver.quit()
else:
    driver.get("https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=163&ct=1729684179&rver=7.5.2211.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f0%2f%3fstate%3d1%26redirectTo%3daHR0cHM6Ly9vdXRsb29rLmxpdmUuY29tL21haWwvMC8%26RpsCsrfState%3d2b769ac8-f90d-dd8c-6713-711258cfc0da&id=292841&aadredir=1&whr=outlook.com&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015")
    time.sleep(3)
    
    email_input_xpath = "/html/body/div[1]/div/div/div/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/form/div[2]/div/div/input"
    email_input = driver.find_element(By.XPATH, email_input_xpath)
    for character in emails[2]:
        email_input.send_keys(character)
        time.sleep(0.1)
    # if emails:
    #     email_input.send_keys(emails[0])
    
    next_button_xpath = '//*[@id="idSIButton9"]'
    next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, next_button_xpath)))
    next_button.click()
    
    time.sleep(3)
    
    pass_input_xpath = "/html/body/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div[2]/div[2]/div/form/div[3]/div/div/input"
    pass_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, pass_input_xpath)))
    
    for character in passwords[2]:
            pass_input.send_keys(character)
            time.sleep(0.3)
    # if passwords:
    #     pass_input.send_keys(passwords[0])
    
    sign_in_button_xpath ='//*[@id="idSIButton9"]'
    sign_in_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, sign_in_button_xpath)))
    sign_in_button.click()
    
    time.sleep(3)
    
    sign_in_button_xpath = '//*[@id="acceptButton"]'
    sign_in_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, sign_in_button_xpath)))
    sign_in_button.click()
        
    user_input = int(input('1. Compose message and send mail: \n2. Read first mail from mailbox: \n3. Report first email from spam to not spam :\n\n select option: '))
    
    if user_input == 1:
        time.sleep(3)
        sign_in_button_xpath = '//*[@id="114-group"]/div/div[1]/div/div/span/button[1]/span/span[1]'
        sign_in_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, sign_in_button_xpath)))
        sign_in_button.click()
        time.sleep(3)
        # //*[@id="message-to-field"]
        # subject_text = input("Enter the email subject: \n")
        to_input_xpath = '//*[@id="docking_InitVisiblePart_0"]/div/div[3]/div[1]/div/div[2]/div/span/span[2]/div/div[1]'
        to_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, to_input_xpath)))
        for i in emails:
            to_input.send_keys(i+",")
        subject_text = input("Enter the email subject: \n")
        subject_input_xpath = '//*[@id="docking_InitVisiblePart_0"]/div/div[3]/div[2]/span/input'
        subject_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, subject_input_xpath)))
        subject_input.send_keys(subject_text)
        
        sent_button_xpath = "/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div[3]/div/div/div[3]/div[1]/div/div/div[2]/div/div[2]/div[1]"
        sent_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, sent_button_xpath)))
        sent_button.click()
        time.sleep(3)
        driver.quit()

    elif user_input== 3:
        # //*[@id="EmptyState_MainMessage"]
        junkmail_button_xpath ='//*[@id="folderPaneDroppableContainer"]/div[1]/div[3]/div/div/div[2]/div'
        junkmail_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, junkmail_button_xpath)))
        junkmail_button.click()
        time.sleep(3) 

        try:
            nothing_in_spam_xpath ='//*[@id="EmptyState_MainMessage"]'
            nothing_in_spam = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, nothing_in_spam_xpath)))
            print('------- Nothing in Spam -------')
            driver.quit()
        except:
            # sign_in_button_xpath ='//*[@id="AQAAAAAAARcBAAAAKaNf+QAAAAA="]/div/div/div/div/div[2]/div[1]/div/div/label/div/i'
            select_button_xpath ='//*[@class="XG5Jd TszOG"]'
            select_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, select_button_xpath)))
            select_button.click()
            time.sleep(3)
            radio_button_xpath ='//*[@id="540"]/span'
            radio_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, radio_button_xpath)))
            radio_button.click()
            moreoption_button_xpath ='//*[@id="Ribbon-540Dropdown"]/div/ul/li[1]/div/ul/li[2]/button/div'
            moreoption_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, moreoption_button_xpath)))
            moreoption_button.click()
            okay_button_xpath ='/html/body/div[8]/div[2]/div/div[3]/button[1]'
            okay_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, okay_button_xpath)))
            okay_button.click()
            time.sleep(3)
            driver.quit()
    else:
        print('----- Please select option from given list -----')
        time.sleep(3)
        driver.quit()

    