#!/usr/bin/env python

""" INTRO
THIS READS LABARCHIVES SCRIPTS
"""


# REQUIREMENTS
# PYTHON 3.12.3
# MECHANICALSOUP 1.3.0
# YAML 6.0.2
# selenium-4.24.0 


import mechanicalsoup
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#login_url = "https://au-mynotebook.labarchives.com/login"
# CURTIN SPECIFIC SSO
login_url = (
"https://id.curtin.edu.au/am/XUI/?realm=/alpha&spEntityID=https%3A%2F%2Faushib.labarchives.com" +
"%2Fsp%2Fproduction&goto=https%3A%2F%2Fid.curtin.edu.au%3A443%2Fam%2Fsaml2%2Fcontinue%2FmetaAlias%2Falpha%2Fidp%3FsecondVisitUrl" +
"%3D%2Fam%2FSSORedirect%2FmetaAlias%2Falpha%2Fidp%3FReqID%253D_1ea2a489c66df4e7b15bbf2579aaf204&AMAuthCookie=#/"
)
    

def yaml_input(login_yaml):
    """ This will only work if you've set up a login.yaml file in same directory """
    with open(f'{login_yaml}.yaml', 'r', encoding='utf-8') as f:
        log_info = yaml.safe_load(f)
        
    login_id = log_info.get("studentid", {})
    return(login_id)
    

def login_la(login_token, login_url):
    """mechanicalsoup won't do JS. But this is still useful for HTTP request checking."""
    browser = mechanicalsoup.StatefulBrowser()
    
    page = browser.get(login_url)
    type(page.soup)
    print(f"HTTP Status Code after login: {page.status_code}")
    #print(f"{page.soup}")
    
    
    # BELOW DOESN"T REALLY WORK
    #browser.select_form('form[id="floatingLabelInput33"]')
    #browser["email"] = login_token
    
    #response = browser.submit_selected()
    #print("response = ", response)
    #print(f"browser.form.print_summary()")
    
    return()
    
    
def selen_login_la(yaml_login, login_url):  
    
    driver = webdriver.Chrome()
    driver.get(login_url)
    wait = WebDriverWait(driver, 10)
    username_input = wait.until(
        EC.presence_of_element_located((By.ID, "floatingLabelInput33"))
    )


    form = driver.find_element_by_id('floatingLabelInput33')
    username_input.send_keys(login_token)
    
    try:
        # Find the form element, if needed
        form = driver.find_element(By.TAG_NAME, "form")  # Adjust based on actual form tag or selector
        form.submit()
    except:
        # If there's no specific form to submit, you might not need this part
        pass
    
    # Optionally, wait for some result or change to verify successful submission
    # Example: waiting for a new element or URL change
    try:
        success_message = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".success-message"))  # Adjust selector as needed
        )
        print("Form submission successful.")
    except:
        print("Form submission failed or success element not found.")
    
    # Close the browser
    driver.quit()
    
    form.submit()

    return()
    
    
login_token = yaml_input("login")    
#login_la(login_token, login_url)
selen_login_la(login_token, login_url)
