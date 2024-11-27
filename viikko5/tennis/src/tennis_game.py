class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.pisteet_p1 = 0
        self.pisteet_p2 = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.pisteet_p1 = self.pisteet_p1 + 1
        else:
            self.pisteet_p2 = self.pisteet_p2 + 1

    def tasan(self, pisteet):
        tasan_tilanteet = {0: "Love-All", 1: "Fifteen-All", 2: "Thirty-All"}
        if pisteet in tasan_tilanteet:
            return tasan_tilanteet[pisteet]
        else:
            return "Deuce"
    
    def etu_tai_voitto(self, pisteiden_ero):
        if abs(pisteiden_ero) == 1:
            tilanne = "Advantage"
        else:
            tilanne = "Win for"
            
        if pisteiden_ero < 0:
            pelaaja = self.player2_name
        else:
            pelaaja = self.player1_name
        return f"{tilanne} {pelaaja}"

    def tilanne(self, pisteet1, pisteet2):
        tilanteet = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}
        score = f"{tilanteet[pisteet1]}-{tilanteet[pisteet2]}"
        return score

    def get_score(self):
        if self.pisteet_p1 == self.pisteet_p2:
            score = self.tasan(self.pisteet_p1)
        elif self.pisteet_p1 >= 4 or self.pisteet_p2 >= 4:
            pisteiden_ero = self.pisteet_p1 - self.pisteet_p2
            score = self.etu_tai_voitto(pisteiden_ero)
        else:
            score = self.tilanne(self.pisteet_p1, self.pisteet_p2)

        return score
