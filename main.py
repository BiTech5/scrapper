import requests as re
from bs4 import BeautifulSoup
url=r"https://techbehemoths.com/companies/kathmandu"
r=re.get(url)
print(r)

soup=BeautifulSoup(r.text,'lxml')
# print(soup)
boxes=soup.find_all('div',class_="co-list__itm")
# print(len(boxes))
company_name=soup.find_all('p',class_="co-box__name font-medium")
for i in company_name:
    a_tag=i.find('a')
    if a_tag:
        print(i.text)