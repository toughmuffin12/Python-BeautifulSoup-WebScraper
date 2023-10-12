import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

#Opens the destination file for the scraped data
scraped_data = open('elca_data.html', 'w')

#Function that sends a get request to the url.
#Then creates a beautiful soup object.
#The for loop looks for all links in the page that start with a current substring. In ELCA's case it is going to start with elca.org. So it will not follow the links to exterior sites.
#If the url does start with that string, the function recursivly calls scrape_site and appends that url to the already visited links.
#Once it finds all the url pages it writes to the opened file elca_data.html.
def scrape_site(url, visited_urls):
    if url in visited_urls:
         return
    
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    base_url = url
    visited_urls.append(url)
    

    for link in soup.find_all('a'):
        suburl = link.get('href')
        absolute_url = urljoin(base_url, suburl)

        if absolute_url.startswith("https://realpython.github"):
            scrape_site(absolute_url, visited_urls)

    scraped_data.write(soup.prettify())

#Visited urls list declaration, initial url although if the website is set up properly it could probably any page in the website, initial function call, closing of elca_data.html
visited_urls = []
elca_url = "https://realpython.github.io/fake-jobs"
scrape_site(elca_url, visited_urls)
scraped_data.close()