import requests as re
from bs4 import BeautifulSoup

def data(att):
    att=str(att)
    url="https://techbehemoths.com"+att

    r=re.get(url)
    soup=BeautifulSoup(r.text,'lxml')
    company_name=soup.find('h1',class_="co-box__name font-medium larger")
    company_website=soup.find('a',class_="btn relative btn-outlined btn-black btn-special")
    company_website=company_website.find('span','val ellipsis')
    company_nbr=soup.find('a',class_='btn btn-outlined btn-black btn-special relative')
    if company_nbr:
        company_nbr=company_nbr.find('span','val ellipsis')
        nbr=company_nbr.text
    else:
       nbr=''
    location=soup.find('span',"co-box__loc-itm")
    all_data={
        'Name':company_name.text if company_name else '',
        "Company Website":company_website.text if company_website else '',
        'Company Number':nbr,
        'Location':location.text if location else ''
    }
    return all_data

def pagination(url):
    r=re.get(url)
    soup=BeautifulSoup(r.text,'lxml')
    p_tag=soup.find_all('p',class_="co-box__name font-medium")
    for i in p_tag:
        a_tag=i.find('a')
        if a_tag:
            href=a_tag['href']
            print(data(href))
i=0
while i!=3:
    i+=1
    nbr=str(i)
    url="https://techbehemoths.com/companies/kathmandu?page="+nbr
    pagination(url)
    print('Page',i,'Finished')

