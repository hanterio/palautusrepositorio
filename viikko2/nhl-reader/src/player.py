class Player:
    def __init__(self, dict):
        self.name = dict["name"]
        self.maa = dict["nationality"]
        self.joukkue = dict["team"]
        self.maalit = dict["goals"]
        self.syotot = dict["assists"]
        self.pisteet = self.maalit + self.syotot
    def __str__(self):
        return f"{self.name:20} {self.joukkue}  {self.maalit:3} + {self.syotot:3} = {self.pisteet:3}" 
