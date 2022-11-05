def Szorzotabla():
    elrendezes = "{0:>4}{1:>4}{2:>4}{3:>4}{4:>4}{5:>4}{6:>4}{7:>4}{8:>4}{9:>4}{10:>4}{11:>4}{12:>4}"

    print(elrendezes.format("\t", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"))
    print("   :------------------------------------------------")
    for i in range(1, 13):
        print(elrendezes.format(str(i)+":", i*1, i*2, i*3, i*4, i*5, i*6, i*7, i*8, i*9, i*10, i*11, i*12))


def Hosszumaganhangzotlan(s):
    jodolog = ""
    rossz = "áéíóőúű"
    for i in s.lower():
        if i not in rossz:
            jodolog += i
        elif i == "á":
            jodolog += "a"
        elif i == "é":
            jodolog += "e"
        elif i == "í":
            jodolog += "i"
        elif i == "ó":
            jodolog += "o"
        elif i == "ő":
            jodolog += "ő"
        elif i == "ú":
            jodolog += "u"
        elif i == "ű":
            jodolog += "ü"
    return jodolog.lower()


def Palindrom(szoveg):
    aze = False
    majdnem = Hosszumaganhangzotlan(szoveg)
    meno = ""
    for i in majdnem:
        if i != " ":
            meno += i
    vissza = Hosszumaganhangzotlan(meno[::-1])
    for i in range(len(vissza)):
        if meno[i] == vissza[i]:
            aze = True
        elif meno[i:i+2] == vissza[i:i+2:-1]:
            aze = True
        elif meno[i:i+3] == vissza[i:i+3:-1]:
            aze = True
    if aze:
        print("Palindrom")
    else:
        print("Nem palindrom")


if __name__ == "__main__":
    Szorzotabla()
    szoveg = "apa"
    Palindrom(szoveg)
