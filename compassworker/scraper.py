import requests
from bs4 import BeautifulSoup


class CompassCard(object):
    _url_frontpage = 'https://compasscard.511sd.com'
    _url_login = 'https://compasscard.511sd.com/webtix/welcome/welcome.do'

    def __init__(self, card_number, password):
        self._card_number = card_number
        self._password = password
        self._login_get_balance()

    def _login_get_balance(self):
        post_payload = {
            'cardNum':self._card_number,
            'pass':self._password,
            'cardOps':'Display',
        }
        response = requests.post(self._url_login, post_payload)
        soup = BeautifulSoup(response.text, 'html5lib')
        balance_update_date, balance = [x.get_text() for x in soup.find('table', class_='results_table', id=False).find_all("td")]
        self._balance = float(balance.replace('$',''))
        self._balance_update_date = balance_update_date

    @property
    def card_number(self):
        return self._card_number

    @property
    def balance(self):
        return self._balance
