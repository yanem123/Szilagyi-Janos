class Team:
    def __init__(self, nev, projekt, szerepkor):
        self._nev = nev
        self._projekt = projekt
        self._szerepkor = szerepkor

        print("-- Developer létrehozva --")

    def __str__(self):
        return self._nev + " a " + self._projekt + "-en dolgozik " + self._szerepkor + " szerepkörben."

    @property
    def nev(self):
        return self._nev

    @property
    def projekt(self):
        return self._projekt

    @property
    def szerepkor(self):
        return self._szerepkor


def peldanyositas():
    lista = [["Ricsi", "SolArch", "Frontend"], ["Angéla", "ZerTeng", "Tesztelő"], ["Peti", "KefERP", "Backend"],
             ["Éva", "KefERP", "Frontend"]]
    emberek = []

    for i in range(len(lista)):
        emberek.append(Team(lista[i][0], lista[i][1], lista[i][2]))
        print(emberek[i])

    return emberek


def partnerek():
    projektek = {}
    projekt = []
    for item in kollegak:
        if item.projekt in projektek:
            projektek[item.projekt] += 1
        else:
            projektek[item.projekt] = 1

    for item in projektek:
        if projektek[item] > 1:
            projekt.append(item)
    # he több együtt dolgozó csapat lenne
    for item in projekt:
        tarsak = []
        for nber in kollegak:
            if nber.projekt == item:
                tarsak.append(nber.nev)
        print(", ".join(tarsak) + " együtt dolgoznak")


if __name__ == "__main__":
    kollegak = peldanyositas()
    partnerek()
