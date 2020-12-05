from requests import get, HTTPError, ConnectionError
from urllib.error import URLError
from bs4 import BeautifulSoup
import re, sys

"""
>>> b = re.sub( r'^\d\.\s', "", a)
>>> b1 = re.sub( r'^\d*\.\s', "", a1)
"""
url = r'https://www.emmasdiary.co.uk/pregnancy-and-birth/unique-baby-names/our-top-300-baby-girl-names'

try:
    r = get(url)
except HTTPError as h:
    print("URL not found.")
    print(sys.exc_info()[0])
except ConnectionError as c:
    print("Connection Error")
    print(sys.exc_info()[0])
except URLError as u:
    print("URL error")
    print(sys.exc_info()[0])

soup = BeautifulSoup(r.content, 'lxml')

listNames = soup.findAll('h3') # finds all h3 tags from the babyNames site.
new_list = [x.get_text() for x in listNames][7:-3]
newer_list = [re.sub( r"^\s*\d*\.\s","",x) for x in new_list]

list_of_names = newer_list[50:100]

print(list_of_names)