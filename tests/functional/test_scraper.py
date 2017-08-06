from unittest import TestCase

from compassworker.scraper import CompassCard
from tests import test_config


class FakeResponse(object):
    def __init__(self, text):
        self.text = text


class MockRequests(object):
    #TODO inject test_config.compass_cards data into MockRequests instance

    @staticmethod
    def post(url, post_payload_dict):
        for card in test_config.compass_cards:
            if card.number == post_payload_dict['cardNum']:
                return FakeResponse(card.balance_page_html)
        return FakeResponse("crap")


class TestCompassCard(TestCase):
    @classmethod
    def setUpClass(cls):
        CompassCard.Requests = MockRequests
        pass

    def test_balance01(self):
        card_config = test_config.compass_cards[0]
        cc = CompassCard(card_config.number, card_config.password )
        self.assertEqual(cc.balance, 12.50)

    def test_balance02(self):
        card_config = test_config.compass_cards[1]
        cc = CompassCard(card_config.number, card_config.password)
        self.assertEqual(cc.balance, 8.00)
