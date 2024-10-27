import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_etsii_joukkueen_pelaajat_oikein(self):
        joukkue = self.stats.team("DET")
        print(joukkue)
        self.assertEqual(str(joukkue[0]), "Yzerman DET 42 + 56 = 98")

    def test_etsii_pelaajan_oikein_jos_ei_ole(self):
        pelaaja = self.stats.search("Kiprusoff")
        self.assertEqual(pelaaja, None)

    def test_etsii_pelaajan_oikein_jos_on(self):
        pelaaja = self.stats.search("Yzerman")
        self.assertEqual(str(pelaaja), "Yzerman DET 42 + 56 = 98")

    def test_lajittele_pelaajat_oikein(self):
        lajittelu = self.stats.top(1)
        self.assertEqual(str(lajittelu[0]), "Gretzky EDM 35 + 89 = 124")

    def test_lajittele_pelaajat_oikein_pisteet(self):
        lajittelu = self.stats.top(1, SortBy.POINTS)
        self.assertEqual(str(lajittelu[0]), "Gretzky EDM 35 + 89 = 124")

    def test_lajittele_pelaajat_oikein_maalit(self):
        lajittelu = self.stats.top(1, SortBy.GOALS)
        self.assertEqual(str(lajittelu[0]), "Lemieux PIT 45 + 54 = 99")

    def test_lajittele_pelaajat_oikein_syotot(self):
        lajittelu = self.stats.top(1, SortBy.ASSISTS)
        self.assertEqual(str(lajittelu[0]), "Gretzky EDM 35 + 89 = 124")