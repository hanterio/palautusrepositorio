class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=5, kasvatuskoko=5):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")
        self.kapasiteetti = kapasiteetti

        if not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            raise Exception("Väärä kasvatuskoko")
        self.kasvatuskoko = kasvatuskoko

        self.joukko = self._luo_lista(self.kapasiteetti)

        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        return n in self.joukko
    
    def lisaa(self, n):
        if not self.kuuluu(n):
            self.joukko[self.alkioiden_lkm] = n
            self.alkioiden_lkm += 1
            self.tarkista_koko()

    def tarkista_koko(self):
        if self.alkioiden_lkm == len(self.joukko):
            self.pidenna_listaa()

    def pidenna_listaa(self):    
        self.joukko += self._luo_lista(self.kasvatuskoko)

    def poista(self, n):
        if n in self.joukko:
            self.joukko.remove(n)
            self.joukko.append(0)
            self.alkioiden_lkm -= 1

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        siisti_joukko = self._luo_lista(self.alkioiden_lkm)

        for i in range(0, self.alkioiden_lkm):
            siisti_joukko[i] = self.joukko[i]

        return siisti_joukko

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        joukko = a.to_int_list() + b.to_int_list()

        for i in range(0, len(joukko)):
            x.lisaa(joukko[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_joukko = a.to_int_list()
        b_joukko = b.to_int_list()

        for i in range(0, len(a_joukko)):
            if a_joukko[i] in b_joukko:
                y.lisaa(a_joukko[i])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_joukko = a.to_int_list()
        b_joukko = b.to_int_list()

        for i in range(0, len(a_joukko)):
            z.lisaa(a_joukko[i])

        for i in range(0, len(b_joukko)):
            z.poista(b_joukko[i])

        return z

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos += str(self.joukko[i]) + ", "
            tuotos += str(self.joukko[self.alkioiden_lkm - 1]) + "}"
            return tuotos
