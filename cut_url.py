# Modules
from sys import argv
import requests
import mechanicalsoup

# Check if was url have protocol https
try:
    if "https://" not in argv[1]: 
        exit("\nYour url not have 'https' !")
except IndexError:
    exit("\nUse: python3 cut_link.py 'https://url'\n")

# Create a short link
try:
    browser = mechanicalsoup.StatefulBrowser()
    browser.open("https://cutt.us")
    Input = browser.page.find("form")
    Input.select("input")[0]['value']=argv[1]
    cut_url = browser.submit(Input,browser.url).soup.select('a')[6]['href']
    print(f"\nurl     : {argv[1]}\ncut url : {cut_url}")
except (requests.exceptions.ConnectionError): # if was you offline
    exit(f"\nurl     : {argv[1]}\ncut url : You are offline!")
except KeyboardInterrupt:
    exit("\nExit...")
