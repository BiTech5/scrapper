import requests as re
from bs4 import BeautifulSoup
url=r"https://techbehemoths.com/companies/kathmandu"
r=re.get(url)
print(r)

soup=BeautifulSoup(r.text,'lxml')
# print(soup)
boxes=soup.find_all('div',class_="co-list__itm")
# print(len(boxes))
p_tag=soup.find_all('p',class_="co-box__name font-medium")
def data(att):
    att=str(att)
    url="https://techbehemoths.com"+att

    r=re.get(url)
    soup=BeautifulSoup(r.text,'lxml')
    company_name=soup.find('h1',class_="co-box__name font-medium larger")
    print(company_name.text)
for i in p_tag:
    a_tag=i.find('a')
    if a_tag:
        href=a_tag['href']
        data(href)
        
