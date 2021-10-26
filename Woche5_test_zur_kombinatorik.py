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



# Beispiele:
print_potenz_menge(['1', '10', 'a', 't'])
print(potenz_menge_anzahl_elemente(22))

print(auf_wie_viele_arten_kann_man_die_Folge_anordnen([-2, 3, 2, 3, 0, 0]))
