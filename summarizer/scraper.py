def scraper(url):
    import requests
    from bs4 import BeautifulSoup
    # URL = 'https://www.hostgator.com/blog/how-make-website-mobile-friendly/'
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')
    contents = soup.find_all('p')
    para = ""
    for content in contents:
        if None in content:
            continue
        para += content.text
        # print(content.text)
    return para