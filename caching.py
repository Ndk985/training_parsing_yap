import requests_cache

MAIN_DOC_URL = 'https://docs.python.org/3/'

if __name__ == '__main__':
    session = requests_cache.CachedSession()
    response = session.get(MAIN_DOC_URL)
    # Печать списка закешированных веб-страниц.
    print(session.cache.urls())
