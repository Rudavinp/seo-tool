from googlesearch import search
from urllib.request import Request, urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException



USER_AGENT = 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)'
# USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'

query = '"Я люблю айфон"'
q = quote_plus(query)

page = "https://www.google.ru/"
search_yandex = 'https://www.yandex.ru/search/?lr=213&text={}'


def get_page(query, w=True):
    query = '"' + query + '"'
    query = quote_plus(query)
    page = search_yandex.format(query)
    print(1, page)
    request = Request(page)
    request.add_header('User-Agent', USER_AGENT)
    response = urlopen(request)
    html = response.read()
    response.close()

    if w:
        with open('index.html', 'w') as f:
            f.write(html.decode('utf-8'))
    return html

opts = Options()
opts.set_headless()
assert opts.headless


def get_page_with_selenium(query):
    query = '"' + query + '"'
    print('yabdex - 1')
    driver = Firefox(options=opts)

    # driver.wait = WebDriverWait(driver, 2)

    driver.get('https://www.yandex.ru')
    try:

        box = driver.find_element_by_id('text')

        # box = driver.wait.until(EC.presence_of_element_located(
        #     (By.ID, 'text'),
        # ))
        print(12)
        button = driver.find_element_by_class_name('suggest2-form__button')
        # button = driver.wait.until(EC.presence_of_element_located(
        #     (By.CLASS_NAME, 'suggest2-form__button')
        # ))
        box.send_keys(query)
        button.click()
    except TimeoutException:
        print('Box or Button didnt find')
    html = driver.page_source

    driver.close()
    with open('index.html', 'w') as f:
        f.write(html)
    return html

def yandex(query):
    list_snippets = []
    list_links = []

    html = get_page(query)
    # html = get_page_with_selenium(query)
    soup = BeautifulSoup(html, 'html.parser')

    # snippets = soup.findAll('div', class_='serp-item__text')
    # print(soup.prettify())
    not_found = soup.find('div', class_= 'misspell')

    if not_found:
        return []
    blocks = soup.find_all('div', class_='serp-item')
    for b in blocks:

        snip = b.find('div', class_='serp-item__text')
        # snip = b.find('div', class_='extended-text')
        link = b.find('a', class_='serp-item__title-link')
        # link = b.find('a', class_='path path_show-https')

        if snip and query.lower() in snip.text.lower():
            list_snippets.append(snip.text.lower())
        if link:
            list_links.append(link.get('href'))

    for s in list_snippets:
        if query.lower() in s:
            list_snippets[list_snippets.index(s)] = list_snippets[list_snippets.index(s)] + '_yes'
        else:
            list_snippets[list_snippets.index(s)]  = list_snippets[list_snippets.index(s)]  + '_not'

    snippets_links = zip(list_snippets, list_links)
    return list_links

