# # dynamic_parsing.py
# from bs4 import BeautifulSoup
# from requests_html import HTMLSession
# import os
# os.environ["PYPPETEER_SKIP_CHROMIUM_DOWNLOAD"] = "1"


# if __name__ == '__main__':
#     session = HTMLSession()
#     response = session.get('https://httpbin.org/')
#     response.html.render(sleep=3)
#     soup = BeautifulSoup(response.html.html, 'lxml')
#     swagger = soup.find(id='swagger-ui')
#     print(swagger.prettify())


from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright   # <-- новый импорт

if __name__ == '__main__':
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://httpbin.org/")
        page.wait_for_timeout(3000)              # sleep 3 секунды
        html = page.content()
        browser.close()

    soup = BeautifulSoup(html, "lxml")
    swagger = soup.find(id="swagger-ui")
    print(swagger.prettify() if swagger else "Элемент #swagger-ui не найден")