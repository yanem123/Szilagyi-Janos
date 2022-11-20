def torles(s):
    rosszak = "aáeéiíoóöőuúüűAÁEÉIÍOÓÖŐUÚÜŰ.,:?\"'-"
    jo = ""
    for k in s:
        if k not in rosszak:
            jo += k
    return jo


def hazi():
    file = open("hazi.txt", "r", encoding="utf-8")
    text = file.readlines()
    fulltext = []
    for line in text:
        if line != "\n":
            fulltext.append(line)
    file.close()

    i = 2
    out = open("out.txt", "a")
    while i <= len(fulltext):
        out.write(torles(fulltext[i]))
        i += 3


if __name__ == "__main__":
    hazi()
