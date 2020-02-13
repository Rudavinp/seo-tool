from googlesearch import search
from urllib.request import Request, urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup

USER_AGENT = 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)'

query = '"Я люблю айфон"'
q = quote_plus(query)

page = "https://www.google.ru/"
search_yandex = 'https://www.yandex.ru/search/?lr=213&text={}'

def get_page(query, w=True):
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

def yandex(query):
    list_snippets = []
    snippets_yes = []
    snippets_not = []

    html = get_page(query)
    soup = BeautifulSoup(html, 'html.parser')
    snippets = soup.findAll('div', class_='serp-item__text')
    links = soup.find_all('a')
    links_ = soup.find_all('a', class_='serp-item__title-link')
    print(22, links_)
    for _ in links_:
        print(55, _.get('href'))
    # for l in links:
    #     print(33, l.get('class'))
    #     print(44, l.get('href'))
    list_links = [l.text.lower() for l in links]
    for s in snippets:
        list_snippets.append(s.text.lower())

    for s in list_snippets:
        if query.lower() in s:
            list_snippets[list_snippets.index(s)] = list_snippets[list_snippets.index(s)] + '_yes'
        else:
            list_snippets[list_snippets.index(s)]  = list_snippets[list_snippets.index(s)]  + '_not'
    for i in list_snippets:
        print(i)
    # print(list_links)

