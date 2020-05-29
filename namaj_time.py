from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = "https://www.islamicfinder.org/world/bangladesh/1185241/dhaka-prayer-times/"
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html,"html.parser")

#print(type(html))
# for line in html:
#     cl=re.findall('pt-card-header',line)
#     print(cl)
names  = soup('span', class_ = 'prayername')
times  = soup('span', class_ = 'prayertime')
prayer_name_lst = list()
prayer_time_lst = list()
#print("===========================================================")

#making prayername list
for name in names:
    #print("abc::",i.contents[0])
    prayer_name_lst.append(name.contents[0])
#print(prayer_name_lst)

#making prayertime list
for time in times:
    #print("abc::",i.contents[0])
    prayer_time_lst.append(time.contents[0])
print(prayer_name_lst)
print(prayer_time_lst)


for i in range(len(prayer_name_lst)):
    print(prayer_name_lst[i],prayer_time_lst[i])
