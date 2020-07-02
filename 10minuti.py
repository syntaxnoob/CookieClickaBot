#!/bin/python3

import math
from ishetvoordelig import hoeveelkosthet, nieuwekostberekenen
from loopmetfunctie import wachtofni

factorr = 1.15
menscps = 5
simulatieduur = 60 * 10  # 1 minuut * aantal minuten
cpsnu = 0
koekjesnu = 0

currentitems = {0: {'aantal': 0}, 1: {'aantal': 0}, 2: {'aantal': 0},
                3: {'aantal': 0}, 4: {'aantal': 0}, 5: {'aantal': 0},
                6: {'aantal': 0}, 7: {'aantal': 0}, 8: {'aantal': 0},
                9: {'aantal': 0}, 10: {'aantal': 0}}

items = {0: {'naam': "cursor", 'cps: ': 0.1, 'beginwaarde: ': 15},
         1: {'naam': "oma", 'cps: ': 1, 'beginwaarde: ': 100},
         2: {'naam': "farm", 'cps: ': 8, 'beginwaarde: ': 1100},
         3: {'naam': "mine", 'cps: ': 47, 'beginwaarde: ': 12000},
         4: {'naam': "factory", 'cps: ': 260, 'beginwaarde: ': 130000},
         5: {'naam': "bank", 'cps: ': 1400, 'beginwaarde: ': 1400000},
         6: {'naam': "tempel", 'cps: ': 7800, 'beginwaarde: ': 20000000},
         7: {'naam': "wizard tower",
             'cps: ': 44000, 'beginwaarde: ': 330000000},
         8: {'naam': "shipment", 'cps: ': 260000, 'beginwaarde: ': 5100000000},
         9: {'naam': "lab", 'cps: ': 1600000, 'beginwaarde: ': 75000000000},
         10: {'naam': "portal", 'cps: ': 10000000,
              'beginwaarde: ': 1000000000000}}

for i in range(1, simulatieduur):
    currentprijs = []
    # Hoeveel koekjes op dit moment
    tussencps = 0
    albetaald = 0
    for j in currentitems:
        tussencps = tussencps + (currentitems[j]['aantal']*items[j]['cps: '])
    if 0.01*tussencps > menscps:
        cpsnu = tussencps
    else:
        cpsnu = tussencps + menscps
    # print("koekjes per seconden NU", cpsnu)
    # Het CPS is gekend
    for k in currentitems:
        albetaald = albetaald + math.ceil(hoeveelkosthet(
            items[k]['beginwaarde: '],
            currentitems[k]['aantal']))
    # Het aantal koekjes op dit moment is gekend

    koekjesnu = round(koekjesnu + cpsnu)

    # print("aantal koekjes NU", koekjesnu)

    # Nu moet het programma uitmaken of dat het beter is om iets te kopen dan
    # om te wachten, wat de beste keuze voor dit moment is.

    # Target kiezen
    j = 0
    while True:
        if currentitems[j]['aantal'] == 0:
            if currentitems[j+1]['aantal'] == 0:
                duurste = j
                break
            else:
                j = j+1
                pass
        else:
            j = j+1
            pass
    # print("ik heb", duurste, "in het oog.")
    # De target is nu gekozen, nu uitmaken of hij beter koop of wacht.
    for j in items:
        tussen = nieuwekostberekenen(items[j]['beginwaarde: '],
                                     currentitems[j]['aantal'])
        currentprijs.append(math.ceil(tussen))

    tekopen = wachtofni(koekjesnu, cpsnu, currentprijs, duurste, items)

    # Koop het bijna duurste items
    if tekopen == 1:
        # print("we gaan het net niet duurste kopen, update in current items.")
        if (duurste == 0):
            if(koekjesnu > currentprijs[duurste]):
                currentitems[duurste]['aantal'] += 1
                print("net de net niet dure gekocht", items[duurste]['naam'],
                      "op", i, "seconden voor",
                      currentprijs[duurste], "koekjes.")
                print("ik had", items[duurste]['naam'], "op het oog")
                print("aantal koekjes nu", koekjesnu, "cps nu", cpsnu)
                print("ik heb nu", koekjesnu-currentprijs[duurste], ".\n")
                koekjesnu = koekjesnu - currentprijs[duurste]

            else:
                # print("niet genoeg geld")
                pass
        else:
            if(koekjesnu > currentprijs[duurste-1]):

                currentitems[duurste-1]['aantal'] += 1
                print("net de Nduurste", items[duurste-1]['naam'],
                      "op", i, "seconden voor",
                      currentprijs[duurste], "koekjes.")
                print("ik had", items[duurste]['naam'], "op het oog")
                print("aantal koekjes nu", koekjesnu, "cps nu", cpsnu)
                print("ik heb nu", koekjesnu-currentprijs[duurste-1], ".\n")
                koekjesnu = koekjesnu - currentprijs[duurste-1]
            else:
                # print("niet genoeg geld")
                pass
    # Koop het duurste items
    else:
        # print("we wachten op het duurste item")
        wekopenduur = 88
    if (wekopenduur == 88):
        if(koekjesnu > currentprijs[duurste]):
            currentitems[duurste]['aantal'] += 1
            print("net de HEEL DURE gekocht", items[duurste]['naam'],
                  "op", i, "seconden voor", currentprijs[duurste], "koekjes.")
            print("ik had", items[duurste]['naam'], "op het oog")
            print("aantal koekjes nu", koekjesnu, "cps nu", cpsnu)
            print("ik heb nu", koekjesnu-currentprijs[duurste], ".\n")
            koekjesnu = koekjesnu - currentprijs[duurste]
        else:
            # print("we hebben nog niet genoeg koekjes.")
            pass
        wekopenduur = 0
print(currentitems)
