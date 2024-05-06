
#
# webscraping: exercise 1
#


# 1) get the HTML
import requests
page = requests.get("https://www.europarl.europa.eu/meps/en/full-list/all")

# 2) parse the HTML
from bs4 import BeautifulSoup
soup = BeautifulSoup(page.text, "html.parser")

with open("tmp.html", "w", encoding="utf-8") as f:
  f.write(soup.prettify())

# 3) select the elements you want
all_elems = soup.select("a.erpl_member-list-item-content")

# Let's display the content of the first element
first_person = all_elems[0]
print(first_person.get_text().strip())

# Let's get only the person name
first_person.select(".erpl_title-h4")[0].get_text()

# Let's find out the URL (remember it's an 'a' tag, ie a link)
first_person.get_attribute_list("href")[0]

# Create two lists of the same length:
# - name: contains only the name of the MEP
# - url: contains the URL of the personal MEP page
# 

name = []
url = []
for i in range(len(all_elems)):
  current_person = all_elems[i]
  name.append(current_person
              .select(".erpl_title-h4")[0]
              .get_text())
  url.append(current_person.get_attribute_list("href")[0])


#
# Exercise 2: The age of each MEP
#

# Loop through all the URLs to get the date of birth of the MEP, if provided
# NOTA: add a pause between two requests (don't flood the server!)

# To add a pause: use time.sleep(number_seconds)
import time
time.sleep(.5)


