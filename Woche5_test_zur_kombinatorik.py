import math
import numpy as np


def potenz_menge(fullset):
    listrep = list(fullset)
    subsets = []
    for i in range(2 ** len(listrep)):
        subset = []
        for k in range(len(listrep)):
            if i & 1 << k:
                subset.append(listrep[k])
        subsets.append(subset)
    return subsets


def print_potenz_menge(iterable):
    pot = potenz_menge(iterable)

    str = "{"
    for i in range(len(pot)):
        current = pot[i]
        currentStr = "{"
        for j in range(len(current)):
            currentStr += current[j]
            currentStr += ","

        if len(current) == 0:
            currentStr += "}"
        else:
            currentStr = currentStr[:-1] + "}"
        str += currentStr
        str += ","

    str = str[:-1] + "}"

    print(str)


def potenz_menge_anzahl_elemente(elemente):
    return 2 ** elemente


def auf_wie_viele_arten_kann_man_die_Folge_anordnen(folge):
    n = len(folge)

    dic = {}
    for i in range(n):
        key = folge[i]
        if key in dic:
            dic[key] += 1
        else:
            dic[key] = 1

    k = 1
    for x in dic:
        k *= math.factorial(dic[x])
    return math.floor(math.factorial(n) / k)


def computer_program(input_vektor, prozent_der_testlaeufe):
    comb = 1

    for x in input_vektor:
        comb *= len(x)

    return math.ceil(comb * prozent_der_testlaeufe)


def sicherheitskopie1(anzahlKopien, anzahlServer):
    n = anzahlKopien + anzahlServer - 1
    k = anzahlKopien
    return math.floor(math.factorial(n) / (math.factorial(k) * math.factorial(n - k)))


def sicherheitskopie2(anzahlKopien, anzahlServer):
    anzahlKopien -= anzahlServer
    return sicherheitskopie1(anzahlKopien, anzahlServer)


def zahlen_mit_ziffer(stellen):
    alleMöglichenZahlen = 9 * 10**(stellen-1)
    alleMöglichenZahlenOhneEineZiffer = 8 * 9**(stellen-1)

    return alleMöglichenZahlen - alleMöglichenZahlenOhneEineZiffer


# Beispiele:
print_potenz_menge(['{{4}}', 'a', 'd', 's'])
print(potenz_menge_anzahl_elemente(15))
print(auf_wie_viele_arten_kann_man_die_Folge_anordnen([-3,-3,0,1,-3,2]))
print(computer_program(
    [
        np.arange(-2, 3, 1),
        np.arange(-1, 4, 1),
        np.arange(-3, 3, 1),
        np.arange(-2, 4, 1),
        np.arange(-3, 5, 1)
    ], 0.6))
print(sicherheitskopie1(7, 10))
print(sicherheitskopie2(11, 10))
print(zahlen_mit_ziffer(6))
