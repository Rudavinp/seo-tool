# import time

# from googlesearch import search
from urllib.request import Request, urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException
from markupsafe import Markup
from flask import render_template
from app import routes


USER_AGENT = 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)'

PAGE = "https://www.yandex.ru/"
SEARCH_YANDEX = 'https://www.yandex.ru/search/?lr=213&text={}'


def get_page(query, w=True):
    """
    This function take param: query -> str
    pars it with quote_plus() for replaces spaces by plus
    and get request to the yandex.ru with user_agent
    If flag w=True html-code of page write to file.
    :param query: str
    :param w: bool write or not page to file (default=True)
    :return: html page
    """
    # TODO yandex.ru often blocks requests from this func.

    query = '"' + query + '"'
    query = quote_plus(query)
    page = SEARCH_YANDEX.format(query)
    request = Request(page)
    request.add_header('User-Agent', USER_AGENT)
    response = urlopen(request)
    html = response.read()
    response.close()

    if w:
        with open('index.html', 'w') as f:
            f.write(html.decode('utf-8'))
    return html




def get_page_with_selenium(query, w=False):
    # COMMENT
    """
    geckodriver&firefox: https://elements.heroku.com/buildpacks/evosystem-jp/heroku-buildpack-firefox
    add RedosToGo on Heroku
    :param query:
    :param w:
    :return:
    """
    yandex_dict = {}

    opts = Options()
    opts.set_headless()
    binary = FirefoxBinary('/app/vendor/firefox/firefox')
    driver = Firefox(options=opts, firefox_binary=binary, executable_path='/app/vendor/geckodriver/geckodriver')
    # driver = Firefox(options=opts, firefox_binary=binary)
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
    # button = driver.find_element_by_class_name('button mini-suggest__button')
    box.send_keys(sent)
    button.click()
    yandex_dict[sent] = driver.page_source

    for sent in query[1:]:
        close = driver.find_element_by_class_name('input__clear')
        close.click()
        box = driver.find_element_by_name('text')
        button = driver.find_element_by_class_name('websearch-button')
        sent = '"' + sent +'"'
        box.send_keys(sent)
        button.click()
        yandex_dict[sent] = driver.page_source

    html = driver.page_source

    driver.close()
    if w:
        with open('index.html', 'w') as f:
            f.write(html)

    return yandex_dict

def yandex(query):
    result_dict = {}


    # html = get_page(query)
    print(43423434234242)
    print(3333, query)
    ya_dict = get_page_with_selenium(query)

    # Dict contain sentences [key] and html page yandex with query
    # this sentences as [item]

    # Parse each html page and check if:
    # - this page is capcha
    # - if sentences not found

    # Then split each page for blocks
    # And check if:
    # - block is advertise -> continue
    # - found snepper text in block and check
    # if sentences in snipper == sentences in query
    # then found link in this block and add to list of links
    # in the end add to result dict sentences[key]: list_links[item]
    # func return this result_dict
    for html in ya_dict:

        list_snippets = []
        list_links = []
        soup = BeautifulSoup(ya_dict[html], 'html.parser')

    # snippets = soup.findAll('div', class_='serp-item__text')
    # print(soup.prettify())

        ya_capcha = soup.find('p', class_='text-wrapper text-wrapper_info')

        if ya_capcha and ya_capcha.text.startswith('Нам очень жаль'):
            # print(222, ya_capcha)
            return 'Ya Capcha'

        not_found = soup.find('div', class_= 'misspell__message')
        # if not_found:
        #     print(10000)

        if not_found and not_found.text.startswith('Точного совпадения не нашлось'):
            print(4)
            result_dict[html] = []
            continue

        blocks = soup.find_all('li', class_='serp-item')
        # blocks = soup.find_all('div', class_='organic')
        # print(99, blocks)

        for b in blocks :
            advertise = b.find('div', class_='label')
            if advertise and advertise.text == 'реклама':
                # print(888, advertise.text)
                print(3)
                continue
            snip = b.find('div', class_='text-container')
            # snip = b.find('div', class_='extended-text')

            if snip and html.lower().strip('"') in snip.text.lower():
                link = b.find('a', class_='link')
                # print(777, link)
                # link = b.find('a', class_='path path_show-https')
                list_snippets.append(snip.text.lower())
                # print(65, snip.text.lower())
                _link = link.get('href')
                    # list_links.append(link.get('href'))
                if not _link:
                    _link = 'Problems with link'
                print(2, list_links)
                list_links.append(_link)
        result_dict[html] = list_links
                # print(66, link.get('href'))
        list_to_template = []



        # if result_dict:
        #     for k, v in result_dict.items():
        #         if result_dict.get(k):
        #             # print(22)
        #             list_to_template.append(Markup('<span style="color: #FF6347">{}</span>'.format(k)))
        #         else:
        #             list_to_template.append(Markup('<span style="color: #00FF00">{}</span>'.format(k)))
        #
        #     text = '.'.join(list_to_template)
        #     text = Markup('<p>{}</p>'.format(text))
        # # print(12, result_dict)
        #     print('olololol')
        #     # routes.like_route(result_dict)
        #     print('kekek')


            # return result_dict



        # return redirect(url_for('index', text=text))


        # ya_dict[html] = list_links



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
    # print(333333, ya_dict)
    print(result_dict)
    return result_dict

