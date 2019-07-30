import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import requests
import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# To scrape all the pages
for i in range(1,30):
    url = 'https://www.amazon.co.uk/R-S-Hydration-Electrolyte-Tablets-Blackcurrant/product-reviews/B00NGTCKWS/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews&pageNumber=' + str(i)

# Instance created for the Chrome driver
driver = webdriver.Chrome(executable_path = "/Users/stephanie/Downloads/chromedriver")
# A new Chrome window will open up

# Directing the page to ORS Amazon reviews page
driver.get(url)
time.sleep(2)

# Scrolling pause time and cycle time
SCROLL_PAUSE_TIME = 1
CYCLES = 1

html = driver.find_element_by_tag_name('html')
html.send_keys(Keys.PAGE_DOWN)
html.send_keys(Keys.PAGE_DOWN)
time.sleep(SCROLL_PAUSE_TIME * 2)

# For loop to run until cycles have been ran
for i in range(CYCLES):
    html.send_keys(Keys.END)
    time.sleep(SCROLL_PAUSE_TIME)

# Collect data
user_elems = driver.find_elements_by_class_name("a-profile-name")
all_users = [elem.text for elem in user_elems]
print(all_users)

date_elems = driver.find_elements_by_class_name("review-date")
all_dates = [elem.text for elem in date_elems]
#print(all_dates)

title_elems = driver.find_elements_by_class_name("review-title-content")
all_titles = [elem.text for elem in title_elems]
#print(all_titles)

flavor_elems = driver.find_elements_by_class_name("a-size-mini")
all_flavors = [elem.text for elem in flavor_elems]
#print(all_flavors)

text_elems = driver.find_elements_by_class_name("review-text-content")
all_texts = [elem.text for elem in text_elems]
#print(all_texts)

# Export data collected as csv file
write_file = "amazon_reviews.csv"
with open(write_file, "w") as output:
    for line in all_users:
        output.write(line + '\n')

# Clean up and close browser once task is completed
driver.close()
note = "hi"
