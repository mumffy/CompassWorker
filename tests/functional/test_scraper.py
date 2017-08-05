from unittest import TestCase

from compassworker.scraper import CompassCard
from tests import test_config


class TestCompassCard(TestCase):
    def test_balance(self):
        card_config = test_config.compass_cards[0]
        cc = CompassCard(card_config.number, card_config.password )
        self.assertEqual(cc.balance, 12.50)
