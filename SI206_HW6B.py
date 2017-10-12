from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = input("Enter count: ")
position = input("Enter position: ")

html = urlopen(url, context=ctx).read()

soup = BeautifulSoup(html, "html.parser")

tags = soup("a")
hrefs = []
#loop count number of times
while count > 0:

	for tag in tags:
		hrefs.append(tag.get('href', None))

print(hrefs)