from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = int(input("Enter count: "))
position = int(input("Enter position: "))
print("Retrieving: ", url)

while count > 0:
	html = urlopen(url, context=ctx).read()
	soup = BeautifulSoup(html, "html.parser")
	tags = soup.find_all('a')
	url = tags[(position-1)].get('href')
	count = count - 1
	print("Retrieving: ", url)
