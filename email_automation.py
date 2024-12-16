import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import os
#Funtions 
##### Sent mail 
def send_mail(driver, isp_value, x_path, emails):
    
    Compose_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, x_path['compose_button_xpath'])))
    Compose_button.click()


    to_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, x_path['to_input_xpath'])))
    for i in emails:
        to_input.send_keys(i+",")
    print('----------------- goto subject ')
    subject_text = input("Enter the email subject: \n")
    
    subject_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, x_path['subject_input_xpath'])))
    subject_input.send_keys(subject_text)
            
    
    sent_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, x_path['sent_button_xpath'])))
    sent_button.click()
    time.sleep(3)
    
    re_btn= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, x_path['re_btn_xpath'])))
    re_btn.click()
    time.sleep(3)
    return driver
    

######  Read first email 
###### 1 gmail  2 yahoo 3 outlook
def read_first_mail(driver, isp_value, x_path):
    read_first_email = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, x_path['read_first_email_xpath'])))
    read_first_email.click()
    time.sleep(3)
    re_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, x_path['re_btn_xpath'])))
    re_btn.click()
    time.sleep(3)
##### notspam 
def notspam(driver , isp_value , x_path):
    if isp_value == 1:
        
        more_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, x_path['more_button_xpath'])))
        more_button.click()
        time.sleep(3)
        spam_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, x_path['spam_button_xpath'])))
        spam_button.click()
        time.sleep(3)
        try:
            nothing_in_spam = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, x_path['nothing_in_spam_xpath'])))
            print('------- Nothing in Spam -------\n')
            re_btn= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, x_path['re_btn_xpath'])))
            re_btn.click()
            time.sleep(3)
            less_btn= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, x_path['less_btn_xpath'])))
            less_btn.click()
            time.sleep(3)
        except:
            selct_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, x_path['selct_button_xpath'])))
            selct_button.click()
            time.sleep(3)
            nospam_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, x_path['nospam_button_xpath'])))
            nospam_button.click()
            time.sleep(3)
            re_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, x_path['re_btn_xpath'])))
            re_btn.click()
            time.sleep(3)
            less_btn= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, x_path['less_btn_xpath'])))
            less_btn.click()
            time.sleep(3)

    elif isp_value == 2:
        
        more_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, x_path['more_button_xpath'])))
        more_button.click()
        time.sleep(3)
        spam_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, x_path['spam_button_xpath'])))
        spam_button.click()
        time.sleep(3)
        try:
            nothing_in_spam = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, x_path['nothing_in_spam_xpath'])))
            print('------- Nothing in Spam -------')
            driver.quit()
        except:
            selct_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, x_path['selct_button_xpath'])))
            selct_button.click()
            time.sleep(3)
            # nospam_button_xpath =' //*[@class="Bn"]' 
            nospam_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, x_path['nospam_button_xpath'])))
            nospam_button.click()
            time.sleep(3)
            re_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, x_path['re_btn_xpath'])))
            re_btn.click()
            time.sleep(3)
    else:
        
        junkmail_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, x_path['junkmail_button_xpath'])))
        junkmail_button.click()
        time.sleep(3) 
    
        try:
            nothing_in_spam = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, x_path['nothing_in_spam_xpath'])))
            print('------- Nothing in Spam -------\n')
            re_btn= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, x_path['re_btn_xpath'])))
            re_btn.click()
            time.sleep(3)
        except:
            # sign_in_button_xpath ='//*[@id="AQAAAAAAARcBAAAAKaNf+QAAAAA="]/div/div/div/div/div[2]/div[1]/div/div/label/div/i'
            select_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, x_path['select_button_xpath'])))
            select_button.click()
            time.sleep(3)
            radio_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, x_path['radio_button_xpath'])))
            radio_button.click()
            moreoption_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, x_path['moreoption_button_xpath'])))
            moreoption_button.click()
            okay_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, x_path['okay_button_xpath'])))
            okay_button.click()
            time.sleep(3)
            re_btn= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, x_path['re_btn_xpath'])))
            re_btn.click()
            time.sleep(3)

check=""
# df = pd.read_csv('Result.csv')
# emails = df['Email'].tolist()
# passwords = df['Password'].tolist()
df = pd.read_csv('data.csv')

# Extract email and password lists
emails = df['Email'].tolist()
passwords = df['Password'].tolist()

# Initialize lists for Gmail, Yahoo, and Outlook emails and their associated passwords
gmail_emails = []
gmail_passwords = []
yahoo_emails = []
yahoo_passwords = []
outlook_emails = []
outlook_passwords = []

# Filter emails by provider and associate with passwords
for email, password in zip(emails, passwords):
    if '@gmail.com' in email:
        gmail_emails.append(email.strip())
        gmail_passwords.append(password.strip())
    elif '@yahoo.com' in email:
        yahoo_emails.append(email.strip())
        yahoo_passwords.append(password.strip())
    elif '@outlook.com' in email or '@hotmail.com' in email:
        outlook_emails.append(email.strip())
        outlook_passwords.append(password.strip())


chrome_options = Options()
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')
chrome_options.add_argument('--ignore-certificate-errors') 
chrome_options.add_experimental_option("excludeSwitches", ["enable-bluetooth"])
chrome_options.add_argument('--disable-web-security')
chrome_options.add_argument('--log-level=3') 
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-software-rasterizer')

outer_flag = True


while outer_flag:
    # inp = int(input('1. Start application: \n2. Exit application\nselect option: '))
    # if inp == 1:
    print("\n------------------------------- \nPlease choose an ISP option from \n1. Gmail \n2. Yahoo \n2. Outlook \n4. Exit application")
    isp = int(input('\nEnter ISP number: '))
    print("-------------------------------\n")
    
    if isp == 1:
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://mail.google.com")
        time.sleep(3)
        
        email_input_xpath = "/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div[1]/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input"
        email_input = driver.find_element(By.XPATH, email_input_xpath)
        if emails:
            # email_input.send_keys(emails[0])
            for character in gmail_emails[0]:
                email_input.send_keys(character)
                time.sleep(0.1)
            next_button_xpath = '//*[@id="identifierNext"]/div/button'
            next_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, next_button_xpath)))
            next_button.click()
        time.sleep(5)
    
        
        pass_input_xpath = "/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input"
        pass_input = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, pass_input_xpath)))
        
        if passwords:
            # pass_input.send_keys(passwords[0])
            for character in gmail_passwords[0]:
                pass_input.send_keys(character)
                time.sleep(0.3)
            sign_in_button_xpath = '//*[@id="passwordNext"]/div/button/span'
            sign_in_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, sign_in_button_xpath)))
            sign_in_button.click()
        inner_flag = True
        while inner_flag:
            # user_input = int(input('\n------------------------\n1. Compose message and send mail: \n2. Read first mail from mailbox: \n3. Report first email from spam to not spam: \n4. change password: \n5. back to other isp \n\n select option: '))
            print('Perform following actions for gmail\n')
            user_input = int(input('1. Compose message and send mail: \n2. Read first mail from mailbox: \n3. Report first email from spam to not spam: \n4. Exit application \n\n select option: '))
            print("-------------------------------\n")
            
            if user_input== 1:
                x_path = {'compose_button_xpath': '/html/body/div[6]/div[3]/div/div[2]/div[1]/div[1]/div/div',
                          'to_input_xpath': '//*[@class="agP aFw"]',
                          'subject_input_xpath': '//input[@name="subjectbox"]',
                          'sent_button_xpath':"//*[@role='button' and text()='Send']",
                          're_btn_xpath':'//*[@id="gb"]/div[2]/div[1]/div[4]/div/a'
                }
                send_mail(driver, isp, x_path, emails)
                
                
            elif user_input == 2:
                x_path={
                    'read_first_email_xpath':'/html/body/div[6]/div[3]/div/div[2]/div[2]/div/div/div/div[2]/div/div[1]/div/div/div[9]/div[1]/div[1]/div/div[1]/div[2]/div/table/tbody/tr[1]',
                    're_btn_xpath':'//*[@id="gb"]/div[2]/div[1]/div[4]/div/a'
                    
                }
                read_first_mail(driver, isp,x_path)
            
            elif user_input == 3 :
                x_path = {'more_button_xpath': '//*[@class="n6"]',
                          'spam_button_xpath': '//*[@class="TN bzz aHS-bnv"]',
                          'nothing_in_spam_xpath': '//*[@id=":1"]/div/div[2]/div[5]/div[1]/div[1]/div[2]/table/tbody/tr/td',
                          'selct_button_xpath':'/html/body/div[6]/div[3]/div/div[2]/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div[5]/div[1]/div[1]/div[1]/div/table/tbody/tr[1]/td[2]',
                          'nospam_button_xpath':"//*[@class='Bn' and text()='Not spam']",
                          're_btn_xpath':'//*[@id="gb"]/div[2]/div[1]/div[4]/div/a',
                          'less_btn_xpath':'/html/body/div[6]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/span'
                          
                }
                notspam(driver,isp,x_path)
            # elif user_input == 4:
            #     inner_flag = False
            elif user_input == 4:
                print('Application closed')
                inner_flag = False
                outer_flag = False
                driver.quit()
            
            else:
                print('please select valid operation......')
        ############################
    elif isp==2:
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://login.yahoo.com/?.src=ym&pspid=159600001&activity=mail-direct&.lang=en-US&.intl=us&.done=https%3A%2F%2Fmail.yahoo.com%2Fd")
        yahoo_tab = driver.current_window_handle        
        email_input_xpath = "/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/form/div[1]/div[3]/input"
        email_input = driver.find_element(By.XPATH, email_input_xpath)

        if emails[1]:
            # email_input.send_keys(emails[1])
            for character in yahoo_emails[0]:
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
            for characters in yahoo_passwords[0]:
                pass_input.send_keys(characters)
                time.sleep(0.3)

                # Yahoo sign-in button
        sign_in_button_xpath = '//*[@id="login-signin"]'
        sign_in_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, sign_in_button_xpath)))
        sign_in_button.click()

        # Authentication part with try-except
        try:
            # Check if authentication is required
            aoth_btn_xpath = '//*[@id="challenge-selector-challenge"]/form/ul/li/button'
            aoth_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, aoth_btn_xpath)))
            aoth_btn.click()
            time.sleep(5)

            # Open Gmail in a new tab to retrieve the verification code
            driver.execute_script("window.open('https://mail.google.com', '_blank');")
            driver.switch_to.window(driver.window_handles[-1])
            time.sleep(3)
            
            # Input email in Gmail login
            email_input_xpath = "/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div[1]/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input"
            email_input = driver.find_element(By.XPATH, email_input_xpath)
            if emails:
                for character in gmail_emails[0]:
                    email_input.send_keys(character)
                    time.sleep(0.1)
            
            # Click Next button after email input
            next_button_xpath = '//*[@id="identifierNext"]/div/button'
            next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, next_button_xpath)))
            next_button.click()
            time.sleep(3)
            
            # Input password
            pass_input_xpath = "/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input"
            pass_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, pass_input_xpath)))
            if passwords:
                for character in gmail_passwords[0]:
                    pass_input.send_keys(character)
                    time.sleep(0.3)
            
            # Click sign-in button
            sign_in_button_xpath = '//*[@id="passwordNext"]/div/button/span'
            sign_in_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, sign_in_button_xpath)))
            sign_in_button.click()
            time.sleep(3)
            
            # Read the first email for the verification code
            read_first_email_xpath = '/html/body/div[6]/div[3]/div/div[2]/div[2]/div/div/div/div[2]/div/div[1]/div/div/div[9]/div[1]/div[1]/div/div[1]/div[2]/div/table/tbody/tr[1]'
            read_first_email = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, read_first_email_xpath)))
            read_first_email.click()
            time.sleep(3)
            
            # Retrieve verification code
            b_element = driver.find_element(By.XPATH, "/html/body/div[6]/div[3]/div/div[2]/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div[2]/div[2]/div/div[3]/div/div/div/div/div/div[1]/div[2]/div[3]/div[3]/div/div[2]/div[2]/table/tbody/tr/td/table[2]/tbody/tr[2]/td/table/tbody/tr/td/div/p[3]/b/b")
            b_text = b_element.text

            # Return to Yahoo and input the verification code
            driver.close()
            driver.switch_to.window(driver.window_handles[0])  # Switch back to Yahoo tab
            verific_input_xpath = '//*[@id="verification-code-field"]'
            verific_input = driver.find_element(By.XPATH, verific_input_xpath)
            for character in b_text:
                verific_input.send_keys(character)
                time.sleep(0.1)
            
            # Click Verify button
            verify_btn_xpath = '//*[@id="verify-code-button"]'
            verify_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, verify_btn_xpath)))
            verify_btn.click()

        except Exception as e:
            print("Authentication not required or an error occurred:", e)

        # Menu and action loop
        inner_flag = True
        while inner_flag:
            print('Perform following actions for Yahoo\n')
            user_input = int(input('1. Compose message and send mail: \n2. Read first mail from mailbox: \n3. Report first email from spam to not spam: \n4. Exit application \n\nSelect option: '))
            print("-------------------------------\n")

            if user_input == 1:
                x_path = {
                    'compose_button_xpath': '//*[@id="mail-app-component-container"]/nav/div/div/button',
                    'to_input_xpath': '//*[@id="message-to-field"]',
                    'subject_input_xpath': '//*[@id="compose-subject-input"]',
                    'sent_button_xpath': '//*[@id="compose-styler"]/div/div[2]/div[2]/div[1]/div[1]/button',
                    're_btn_xpath': '/html/body/div[1]/header/div/div/div[3]/div/div[1]/div[1]/a'
                }
                send_mail(driver, isp, x_path, emails)
                
            elif user_input == 2:
                x_path = {
                    'read_first_email_xpath': '/html/body/div[2]/div/div[1]/div/div[2]/div[3]/main/div/div/div/div/div/div/div[1]/div/div/ul/li[2]',
                    're_btn_xpath': '/html/body/div[1]/header/div/div/div[3]/div/div[1]/div[1]/a'
                }
                read_first_mail(driver, isp, x_path)

            elif user_input == 3:
                x_path = {
                    'more_button_xpath': '//*[@id="left-rail-more-menu"]/div/div',
                    'spam_button_xpath': '//*[@id="left-rail-more-menu-item-2"]/div',
                    'nothing_in_spam_xpath': '//*[@id="mail-reader-container"]/div/div/div/div/div/div/div[1]/div/div/div/div',
                    'selct_button_xpath': '//*[@id="mail-reader-container"]/div/div/div/div/div/div/div[1]/div/div/ul/li[2]/div/div[1]/span',
                    'nospam_button_xpath': '//*[@id="mail-app-component-container"]/div[3]/div/div[2]/div/button[5]',
                    're_btn_xpath': '/html/body/div[1]/header/div/div/div[3]/div/div[1]/div[1]/a'
                }
                notspam(driver, isp, x_path)

            elif user_input == 4:
                print('Application closed')
                inner_flag = False
                driver.quit()

            else:
                print('Please enter a correct option')
            
            time.sleep(3)
    elif isp == 3:
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=163&ct=1729684179&rver=7.5.2211.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f0%2f%3fstate%3d1%26redirectTo%3daHR0cHM6Ly9vdXRsb29rLmxpdmUuY29tL21haWwvMC8%26RpsCsrfState%3d2b769ac8-f90d-dd8c-6713-711258cfc0da&id=292841&aadredir=1&whr=outlook.com&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015")
        time.sleep(3)
        
        email_input_xpath = "/html/body/div[1]/div/div/div/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/form/div[2]/div/div/input"
        email_input = driver.find_element(By.XPATH, email_input_xpath)
        for character in outlook_emails[0]:
            email_input.send_keys(character)
            time.sleep(0.1)
        # if emails:
        #     email_input.send_keys(emails[0])
        
        next_button_xpath = '//*[@id="idSIButton9"]'
        next_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, next_button_xpath)))
        next_button.click()
        
        time.sleep(3)
        
        pass_input_xpath = "/html/body/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div[2]/div[2]/div/form/div[3]/div/div/input"
        pass_input = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, pass_input_xpath)))
        
        for character in outlook_passwords[0]:
                pass_input.send_keys(character)
                time.sleep(0.3)
        # if passwords:
        #     pass_input.send_keys(passwords[0])
        
        sign_in_button_xpath ='//*[@id="idSIButton9"]'
        sign_in_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, sign_in_button_xpath)))
        sign_in_button.click()
        
        time.sleep(3)
        
        stay_in_button_xpath = '//*[@id="acceptButton"]'
        stay_in_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, stay_in_button_xpath)))
        stay_in_button.click()
        inner_flag = True
        while inner_flag:
            print('Perform following actions for outlook\n')
            user_input = int(input('1. Compose message and send mail: \n2. Read first mail from mailbox: \n3. Report first email from spam to not spam: \n4. Exit application \n\n select option: '))
            print("-------------------------------\n")
            if user_input== 1:
                x_path = {'compose_button_xpath': '//*[@id="114-group"]/div/div[1]/div/div/span/button[1]/span/span[1]',
                          'to_input_xpath': '//*[@id="docking_InitVisiblePart_0"]/div/div[3]/div[1]/div/div[2]/div/span/span[2]/div/div[1]',
                          'subject_input_xpath': '//*[@id="docking_InitVisiblePart_0"]/div/div[3]/div[2]/span/input',
                          'sent_button_xpath':'/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div[3]/div/div/div[3]/div[1]/div/div/div[2]/div/div[2]/div[1]',
                          're_btn_xpath':'//*[@id="O365_AppName"]'
                          
                }
                send_mail(driver, isp, x_path,emails)
                # inner_flag = False
            # if user_input == 2:
            #     read_first_mail(driver, isp, '/html/body/div[6]/div[3]/div/div[2]/div[2]/div/div/div/div[2]/div/div[1]/div/div/div[9]/div[1]/div[1]/div/div[1]/div[2]/div/table/tbody/tr[1]')
            # ############################
            elif user_input == 2:
                x_path={'read_first_email_xpath': '//*[@class="XG5Jd TszOG"]',
                       're_btn_xpath':'//*[@id="O365_AppName"]'    
                }
                read_first_mail(driver, isp,x_path)
                # inner_flag = False
            ############################
            ############################
            elif user_input == 3 :
                x_path = {'junkmail_button_xpath': '//*[@id="folderPaneDroppableContainer"]/div[1]/div[3]/div/div/div[2]/div',
                          'nothing_in_spam_xpath': '//*[@id="EmptyState_MainMessage"]',
                          'select_button_xpath': '//*[@class="XG5Jd TszOG"]',
                          'radio_button_xpath':'//*[@id="540"]/span',
                          'moreoption_button_xpath':'//*[@id="Ribbon-540Dropdown"]/div/ul/li[1]/div/ul/li[2]/button/div',
                          'okay_button_xpath':'/html/body/div[8]/div[2]/div/div[3]/button[1]',
                          're_btn_xpath':'//*[@id="O365_AppName"]'
                }
                notspam(driver,isp,x_path)
                # inner_flag = False
            elif user_input == 4:
                print('Application closed')
                inner_flag = False
                outer_flag = False
                driver.quit()
            else:
                print('please enter correct option')
    elif isp==4:
        outer_flag=False
        print('Application closed')
    else:
    # driver.quit()
        print("please write a given ISP")
                
    # elif inp==2:
    #     outer_flag=False
    # else:
    #     print('please enter correct option')