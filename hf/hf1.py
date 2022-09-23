# coding : utf-8

# 1. feladat
def PythonProf():

    sentence = input("Adjon meg egy mondatot: ")

    frequency = {}
    for letter in sentence:
        if letter not in frequency:
            frequency[letter] = 1
        else:
            frequency[letter]=frequency[letter]+1

    print("Betűk gyakorisága: "+str(frequency))
    print("Fordítva: "+sentence[::-1])

    print("Listába rendezve szavanként: "+str(sentence.split(' ')))

# 2. feladat

def Nemtom():

    number = input("Adjon meg egy számot: ")
    unit = input("Adjon meg egy mértékegységet: ")

    if unit == "cm":
        print(str(float(number)/2.54)+" inches")
    elif unit == "inch":
        print(str(float(number)*2.54)+" centimeters")
    else:
        print("Not correct unit!")

if __name__=="__main__":
    PythonProf()
    Nemtom()