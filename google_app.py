from googlesearch import search
from urllib.request import Request, urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup

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

def yandex(query):
    snippets_links = {}
    list_snippets = []
    list_links = []
    snippets_yes = []
    snippets_not = []

    html = get_page(query)
    soup = BeautifulSoup(html, 'html.parser')

    # snippets = soup.findAll('div', class_='serp-item__text')
    # print(soup.prettify())
    blocks = soup.find_all('div', class_='serp-item')
    print(34, type(blocks))
    for b in blocks:
        print(type(b))
        snip = b.find('div', class_='serp-item__text')
        link = b.find('a', class_='serp-item__title-link')
        if snip and query.lower() in snip.text.lower():
            list_snippets.append(snip.text.lower())
        else:
            list_snippets.append('')
        if link:
            list_links.append(link.get('href'))
        else:
            list_links.append('')



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
    #
    for s in list_snippets:
        if query.lower() in s:
            list_snippets[list_snippets.index(s)] = list_snippets[list_snippets.index(s)] + '_yes'
        else:
            list_snippets[list_snippets.index(s)]  = list_snippets[list_snippets.index(s)]  + '_not'

    snippets_links = zip(list_snippets, list_links)
    # print(tuple(snippets_links))
    return list_links
    # for i in list_snippets:
    #     print(i)
    # print(list_links)

