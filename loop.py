#!/bin/python3

from ishetvoordelig import koekjesberekenen
import math
nukoekje = 180

wathebik = {}
watkosthet = []
cpsintotaal = 0
koopbaar = {}

# for i in range(17):
#     wathebik[i] = {}
#     print(i)
#     hoeveelheid = int(input('hoeveelheid van boven'))
#     cps = input('cps van boven')
#     beginkost = [15, 100, 1100, 12000, 130000, 1400000, 20000000]
#     wathebik[i]['hoeveelheid: '] = hoeveelheid
#     wathebik[i]['cps: '] = cps
#     wathebik[i]['beginwaarde: '] = beginkost[i]
# print(wathebik)

# gegeven data

nu = {0: {'hoeveelheid: ': 0, 'cps: ': 0.1, 'beginwaarde: ': 15},
      1: {'hoeveelheid: ': 6, 'cps: ': 1, 'beginwaarde: ': 100},
      2: {'hoeveelheid: ': 0, 'cps: ': 8, 'beginwaarde: ': 1100},
      3: {'hoeveelheid: ': 0, 'cps: ': 47, 'beginwaarde: ': 12000},
      4: {'hoeveelheid: ': 0, 'cps: ': 260, 'beginwaarde: ': 130000},
      5: {'hoeveelheid: ': 0, 'cps: ': 1400, 'beginwaarde: ': 1400000},
      6: {'hoeveelheid: ': 0, 'cps: ': 7800, 'beginwaarde: ': 20000000},
      7: {'hoeveelheid: ': 0, 'cps: ': 44000, 'beginwaarde: ': 330000000},
      8: {'hoeveelheid: ': 0, 'cps: ': 260000, 'beginwaarde: ': 5100000000},
      9: {'hoeveelheid: ': 0, 'cps: ': 1600000, 'beginwaarde: ': 75000000000},
      10: {'hoeveelheid: ': 0, 'cps: ': 9999999, 'beginwaarde: ': 1000000000000}
      }

# Bereken de kost van volgende aankoop
print("prijzen berekenen...")
for i in nu:
    nieuwekost = koekjesberekenen(nu[i]['beginwaarde: '],
                                  nu[i]['hoeveelheid: '])
    watkosthet.append(math.ceil(nieuwekost))

# cps berekenen
print("cps berekenen(eventuele powerups moeten hier nog komen)...")
for j in nu:
    cpsintotaal = (cpsintotaal + (nu[j]['hoeveelheid: ']) * (nu[j]['cps: ']))

# Welke producten kan ik kopen?
for k in nu:
    koopbaar[k] = {}
    if (watkosthet[k] < nukoekje):
        koopbaar[k]["koopbaar: "] = 'True'
    else:
        koopbaar[k]["koopbaar: "] = 'False'


# Het duurste en betaalbare item vinden
i = 0
while True:
    if (nu[i]['hoeveelheid: '] == 0):
        if(nu[i + 1]['hoeveelheid: '] == 0):
            duurste = i
            break
        else:
            i = i + 1
            pass

    else:
        i = i + 1
        pass

# Berekenen hoelang het duurt om de duurste te kopen
duurstetijd = ((watkosthet[duurste] - nukoekje) / cpsintotaal)

# Berekenen hoelang het duurt om de bijna duurste eerst te kopen
# Eest nieuwe cps berekenen
cpsintotaalextra = cpsintotaal + nu[duurste - 1]['cps: ']

# Bijna duurste tijd berekenen
bijnaduurstekoek = (nukoekje - watkosthet[duurste - 1])
bijnaduurstetijd = (
    (watkosthet[duurste] - bijnaduurstekoek) / cpsintotaalextra)

print(bijnaduurstetijd, duurstetijd)

# Kopen of wachten
if(bijnaduurstetijd < duurstetijd):
    print("Ik raad aan om item", nu[duurste - 1], "te kopen.")
if(bijnaduurstetijd > duurstetijd):
    print("\nik raad aan om te wachten tot je de volgende item kan kopen.")
    print("je bespaard", round(bijnaduurstetijd - duurstetijd), "seconden.")
