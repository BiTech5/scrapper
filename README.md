# TechBehemoths Kathmandu Scraper

This project is a Python web scraper that collects company details from [TechBehemoths](https://techbehemoths.com/), specifically targeting companies listed in Kathmandu.  
The scraper gathers information such as:

- Company Name  
- Company Website  
- Company Number  
- Location  

All the collected data is exported into an Excel file (`company.xlsx`).

---

## How it Works

1. The script loops through multiple pages of Kathmandu company listings.  
2. For each company, it visits the detail page and extracts:  
   - Company name  
   - Website (if available)  
   - Contact number (if available)  
   - Location  
3. The data is stored in a structured dictionary.  
4. Finally, everything is combined into a Pandas DataFrame and saved as an Excel file.

---

## Installation & Setup

1. Clone this repository or copy the code.  
2. Make sure you have Python installed (>=3.8 recommended).  
3. Install the required dependencies:

```bash
pip install requests beautifulsoup4 lxml pandas openpyxl
```

4. Run the script:

```bash
python scraper.py
```
## Output
After running, you will get an Excel file named:
```bash
company.xlsx
```

## Notes

Some companies may not have a website or contact number listed; in that case, the scraper adds placeholder text such as "Website is not mentioned" or "Number is not mentioned".

The script currently scrapes 3 pages of companies in Kathmandu. You can change this number inside the main() function.

This scraper is for educational purposes only. Please respect the website’s terms of service before using it at scale.


