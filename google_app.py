import time

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
    print(response.code)
    response.close()

    if w:
        with open('index.html', 'w') as f:
            f.write(html.decode('utf-8'))
    return html

opts = Options()
# opts.set_headless()
# assert opts.headless


def get_page_with_selenium(query):
    yandex_dict = {}
    # query = '"' + query + '"'
    print('yabdex - 1')
    # print(3, query)
    driver = Firefox(options=opts)

    driver.wait = WebDriverWait(driver, 5)

    driver.get('https://www.yandex.ru')
    # try:
    # #
    # #     # box = driver.find_element_by_id('text')
    # #
    #     box = driver.wait.until(EC.presence_of_element_located(
    #         (By.ID, 'text'),
    #     ))
    # #     print(12)
    # #     button = driver.find_element_by_class_name('suggest2-form__button')
    #     button = driver.wait.until(EC.presence_of_element_located(
    #         (By.CLASS_NAME, 'suggest2-form__button')
    #     ))
    #     box.send_keys(query)
    #     button.click()
    # except TimeoutException:
    #     print('Box or Button didnt find')
    sent = '"' + query[0] +'"'
    box = driver.find_element_by_name('text')
    button = driver.find_element_by_class_name('suggest2-form__button')
    box.send_keys(sent)
    button.click()
    yandex_dict[sent] = driver.page_source

    for sent in query[1:]:
        time
        close = driver.find_element_by_class_name('input__clear')
        close.click()
        box = driver.find_element_by_name('text')
        button = driver.find_element_by_class_name('websearch-button')
        sent = '"' + sent +'"'
        box.send_keys(sent)
        button.click()
        yandex_dict[sent] = driver.page_source

    print(len(yandex_dict))

    html = driver.page_source

    driver.close()
    with open('index.html', 'w') as f:
        f.write(html)
    return yandex_dict

def yandex(query):


    # html = get_page(query)
    ya_dict = get_page_with_selenium(query)

    for html in ya_dict:
        list_snippets = []
        list_links = []
        soup = BeautifulSoup(ya_dict[html], 'html.parser')

    # snippets = soup.findAll('div', class_='serp-item__text')
    # print(soup.prettify())

        ya_capcha = soup.find('p', class_='text-wrapper text-wrapper_info')
        if ya_capcha and ya_capcha.text.startswith('Нам очень жаль'):
            print(222, ya_capcha)
            return 'Ya Capcha'

        not_found = soup.find('div', class_= 'misspell')

        if not_found and not_found.text.startswith('Точного совпадения не нашлось'):
            print(99999)
            ya_dict[html] = []
            continue
        # blocks = soup.find_all('div', class_='serp-item')
        blocks = soup.find_all('div', class_='organic')
        # print(99, blocks)

        for b in blocks :
            advertise = b.find('div', class_='label')
            if advertise and advertise.text == 'реклама':
                print(888, advertise.text)
                continue
            snip = b.find('div', class_='text-container')
            # snip = b.find('div', class_='extended-text')
            link = b.find('a', class_='link')
            # print(777, link)
            # link = b.find('a', class_='path path_show-https')
            print(44, html.lower().strip('"'))
            if snip:
                print(44, html.lower().strip('"'))
                print(45, snip.text.lower())
            if snip and html.lower().strip('"') in snip.text.lower():
                list_snippets.append(snip.text.lower())
                print(65, snip.text.lower())
                if link:
                    list_links.append(link.get('href'))
                # print(66, link.get('href'))

        ya_dict[html] = list_links



    # links = soup.find_all('a')
    # print(33, links)
    # links_ = soup.find_all('a', class_='serp-item__title-link')
    # print(len(snippets))
    # print(len(links_))
    # for _ in links_:
    #     print(55, _.get('href'))
    # for l in links:
    #     print(33, l.get('class'))
    #     print(44, l.get('href'))
    # list_links = [l.text.lower() for l in links if ]
    # for s in snippets:
    #     list_snippets.append(s.text.lower())
    # #
    #     for s in list_snippets:
    #         if query.lower() in s:
    #             list_snippets[list_snippets.index(s)] = list_snippets[list_snippets.index(s)] + '_yes'
    #         else:
    #             list_snippets[list_snippets.index(s)]  = list_snippets[list_snippets.index(s)]  + '_not'
    #
    #     snippets_links = zip(list_snippets, list_links)
    print(type(ya_dict))
    return ya_dict

