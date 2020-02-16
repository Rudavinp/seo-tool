from googlesearch import search
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

opts = Options()
opts.set_headless()
assert opts.headless  # без графического интерфейса.

browser = Firefox(options=opts)
browser.get('https://duckduckgo.com')

query = 'i like iphone'

my_res = []

# for i in search(query, num=1,
#                 ):
#     my_res.append(i)
#
# print(my_res)