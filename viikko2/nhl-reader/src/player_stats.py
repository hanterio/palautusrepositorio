from player import Player
from player_reader import PlayerReader

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader.get_players()

    def top_scorers_by_nationality(self, maa):
        lajiteltu = sorted(self.reader, key=lambda player: player.pisteet, reverse=True)

        maittain = []
        for player in lajiteltu:
            if player.maa == maa:
                maittain.append(player)
        return maittain