#!/usr/bin/env python

# INTRO
# THIS READS LABARCHIVES SCRIPTS



# REQUIREMENTS
# PYTHON 3.12.3
# MECHANICALSOUP 1.3.0


import mechanicalsoup
import yaml

browser = mechanicalsoup.StatefulBrowser()
login_url = "https://au-mynotebook.labarchives.com/login"
#page = browser.get(login_url)
page = browser.open(login_url)
#print(f"HTTP Status Code after login: {page.status_code}")