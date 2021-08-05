import requests, os, io, docx
from bs4 import BeautifulSoup

url_page = input("Enter a URL: ")
url_page.strip()
page_req = requests.get(url_page, headers={'User-agent': 'Chrome/91.0.4472.114'}) # Enter your Browser Name and Version inside the quotes

beau_soup = BeautifulSoup(page_req.content, 'html.parser')
page_cont = beau_soup.findAll('img') 

name = docx.Document()
name.add_heading('Web Scraped Images', 0)

for _ in page_cont:
    img_name = _.get("src")
    img_var = os.path.split(img_name)
    req_img = requests.get(img_name)
    img_name = io.BytesIO(req_img.content)
    try:
        name.add_picture(img_name)
    except:
        pass

print("Success!")

name.save('imgs.docx')