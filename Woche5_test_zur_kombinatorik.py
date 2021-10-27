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
    return math.factorial(n) / k


def computer_program(input_vektor, prozent_der_testlaeufe):
    comb = 1

    for x in input_vektor:
        comb *= len(x)

    return math.ceil(comb * prozent_der_testlaeufe)


def sicherheitskopie1(anzahlKopien, anzahlServer):
    n = anzahlKopien + anzahlServer - 1
    k = anzahlKopien
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))


def sicherheitskopie2(anzahlKopien, anzahlServer):
    anzahlKopien -= anzahlServer
    return sicherheitskopie1(anzahlKopien, anzahlServer)


def zahlen_mit_ziffer(stellen):
    return 10 ** stellen - 9 ** stellen


# Beispiele:
print_potenz_menge(['1', '10', 'a', 't'])
print(potenz_menge_anzahl_elemente(22))
print(auf_wie_viele_arten_kann_man_die_Folge_anordnen([-2, 3, 2, 3, 0, 0]))
print(computer_program([np.arange(-1, 3, 1), np.arange(-3, 5, 1), np.arange(-2, 6, 1), np.arange(0, 3, 1)], 0.8))
print(sicherheitskopie1(10, 10))
print(sicherheitskopie2(11, 10))
print(zahlen_mit_ziffer(7))
