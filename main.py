import requests as re
from bs4 import BeautifulSoup
import pandas as pd

def data(att):
    att = str(att)
    url = "https://techbehemoths.com" + att

    r = re.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    
    company_name = soup.find('h1', class_="co-box__name font-medium larger")
    company_website = soup.find('a', class_="btn relative btn-outlined btn-black btn-special")
    company_nbr = soup.find('a', class_='btn btn-outlined btn-black btn-special relative')
    location = soup.find('span', class_="co-box__loc-itm")

    company_name_text = company_name.text.strip() if company_name else 'Company  name is not given'
    company_website_text = company_website.find('span', class_='val ellipsis').text.strip() if company_website else 'Website is not mentioned'
    company_nbr_text = company_nbr.find('span', class_='val ellipsis').text.strip() if company_nbr else 'Number is not mentioned'
    location_text = location.text if location else 'Location not mentioned'

    all_data = {
        'Name': company_name_text,
        "Company Website": company_website_text,
        'Company Number': company_nbr_text,
        'Location': location_text
    }
    return all_data

def pagination(url):
    r = re.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    p_tags = soup.find_all('p', class_="co-box__name font-medium")
    
    page_data = []
    for p_tag in p_tags:
        a_tag = p_tag.find('a')
        if a_tag:
            href = a_tag['href']
            company_data = data(href)
            page_data.append(company_data)
            
    
    return page_data

def main():
    all_data = []
    for i in range(3):
        nbr = str(i + 1)
        url = "https://techbehemoths.com/companies/kathmandu?page=" + nbr
        page_data = pagination(url)
        all_data.extend(page_data)
        
    df = pd.DataFrame(all_data)
    df.to_excel('company.xlsx')

if __name__ == "__main__":
    main()
