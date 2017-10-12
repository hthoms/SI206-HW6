from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()

soup = BeautifulSoup(html, "html.parser")

tags = soup('span')
total, count = 0, 0

for tag in tags:
    total += int(tag.contents[0])
    count += 1

#You are to find all the <span> tags in the file and pull out the numbers from the tag and sum the numbers.
print("Count ", count)
print("Sum ", total)