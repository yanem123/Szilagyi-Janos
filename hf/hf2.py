#coding: utf-8

#Háromszög számolás....
def triCalc():

    print("Adja meg a háromszög oldalát cm-ben:")

    aSide = int(input("a oldal (cm): "))
    bSide = int(input("b oldal (cm): "))
    cSide = int(input("c oldal (cm): "))

    possible = False

    if aSide + bSide >= cSide and aSide + cSide >= bSide and bSide + cSide >= aSide:
        possible = True

    if possible:
        print("A(z) {}, {} és {} oldalú háromszög szerkeszthető.".format(aSide, bSide, cSide))
    else:
        print("A(z) {}, {} és {} oldalú háromszög NEM szerkeszthető".format(aSide, bSide, cSide))

if __name__=="__main__":
    triCalc()