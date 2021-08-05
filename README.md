# Web-Scraper
This project helps to scrape the internet, download the images from the specified URL and save the scraped images in a Word document.

This project helps to scrape the internet, download the images from the specified URL and save the scraped images in a Word document.

Web Scraping is the process of automatically collecting specific data from the internet. It is used to process and collect large data and store it in a manageable format. In this packet, we look at one of the methods to scrape images from the Internet. 

This packet is implemented in Python and uses BeautifulSoup, Requests, and Python-Docx libraries. BeautifulSoup is a python library that is used to parse the Web Page and find the specific HTML tag. Requests is a Python library used to get a URL and access its contents. The Python-Docx library is used to manipulate a document with a .docx extension (Word Document) 

As a pre-requisite, you need to know basic HTML tags, their meanings, and usage. 

 

Installing the required Libraries:

The required libraries do not come preinstalled in Python3 and have to installed using the pip command. 

pip install bs4
pip install requests
pip install python-docx 
 

Post Installation Instructions:

After downloading the packet, copy the code into your Code Editor. Once copied, change the below code:

page_req = requests.get(url_page, headers={'User-agent': 'Chrome/91.0.4472.114'})
Headers prevent the browser from thinking that the request is sent from a robot and help to process the request. In place of Chrome/91.0.4472.114, type the name of your browser and its version. In the case of Chrome, click on the 3 dots on the top right corner and click on Help and choose About Google Chrome. The browser version can be found there. 

Once the required changes are made, run the program and scrape images from the Web. 
