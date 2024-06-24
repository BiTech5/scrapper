import requests as re
from bs4 import BeautifulSoup
url=r"https://techbehemoths.com/companies/kathmandu"
r=re.get(url)
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
    company_website=soup.find('a',class_="btn relative btn-outlined btn-black btn-special")
    company_website=company_website.find('span','val ellipsis')
    company_nbr=soup.find('a',class_='btn btn-outlined btn-black btn-special relative')
    company_nbr=company_nbr.find('span','val ellipsis')
    location=soup.find('span',"co-box__loc-itm")
    all_data={
        'Name':company_name.text,
        "Company Website":company_website.text,
        'Company Number':company_nbr.text,
        'Location':location.text
    }
    return all_data

for i in p_tag:
    a_tag=i.find('a')
    if a_tag:
        href=a_tag['href']
        print(data(href))