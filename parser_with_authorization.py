# parser_with_authorization.py
import requests
from bs4 import BeautifulSoup

LOGIN_URL = 'http://158.160.172.156/login/'

if __name__ == '__main__':
    session = requests.session()
    response = session.get(LOGIN_URL)
    response.encoding = 'utf-8'

    soup = BeautifulSoup(response.text, features='lxml')

    csrf_token = soup.find('input', {'name': 'csrfmiddlewaretoken'})['value']
    data = {
        'username': 'test_parser_user',
        'password': 'testpassword',
        'csrfmiddlewaretoken': csrf_token
    }

    response = session.post(LOGIN_URL, data=data)
    response.encoding = 'utf-8'
    print(response.status_code)
    print(response.text)
