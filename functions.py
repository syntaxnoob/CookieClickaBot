#!/bin/python3

def nieuwekostberekenen(beginwaarde, hoeveelheid):
    factorr = 1.15
    tussen = beginwaarde
    nieuwefactor = factorr
    if (hoeveelheid == 0):
        nieuwekost = beginwaarde
    else:
        for i in range(hoeveelheid):
            nieuwefactor = factorr
            for j in range(i):
                nieuwefactor = nieuwefactor * factorr
            tussen = tussen + (beginwaarde*(nieuwefactor))
        nieuwekost = (beginwaarde*nieuwefactor)
    return nieuwekost


def hoeveelkosthet(beginwaarde, hoeveelheid):
    factorr = 1.15
    nieuwefactor = factorr
    totaleprijs = 0
    if hoeveelheid == 0:
        totaleprijs = 0

    elif hoeveelheid == 1:
        totaleprijs = beginwaarde
    else:
        for i in range(hoeveelheid):

            for j in range(i):
                nieuwefactor = nieuwefactor * factorr
        totaleprijs = totaleprijs + (beginwaarde*nieuwefactor)
    return totaleprijs
