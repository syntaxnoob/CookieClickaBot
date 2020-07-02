#!/bin/python3

def wachtofni(nukoekje, cpsintotaal, watkosthet, duurste, nu):

    # Berekenen hoelang het duurt om de duurste te kopen
    duurstetijd = ((watkosthet[duurste] - nukoekje) / cpsintotaal)

    # Berekenen hoelang het duurt om de bijna duurste eerst te kopen
    # Eest nieuwe cps berekenen

    if (duurste == 0):
        bijnaduurstekoek = (nukoekje - watkosthet[duurste])
        cpsintotaalextra = cpsintotaal + nu[duurste]['cps: ']
    else:
        cpsintotaalextra = cpsintotaal + nu[duurste - 1]['cps: ']
        bijnaduurstekoek = (nukoekje - watkosthet[duurste - 1])

    # Bijna duurste tijd berekenen
    bijnaduurstetijd = (
        (watkosthet[duurste] - bijnaduurstekoek) / cpsintotaalextra)

    # Kopen of wachten
    if(bijnaduurstetijd < duurstetijd):
        print("Ik raad aan om item net niet duur te kopen.")
        tekopen = 1
    elif(bijnaduurstetijd > duurstetijd):
        print("ik raad aan om te wachten tot je de volgende item kan kopen.")
        print("je bespaard", round(bijnaduurstetijd - duurstetijd), "sec.")
        tekopen = 2
    else:
        print("het maakt niet  uit, koop maar zodat je een investering maakt.")
        tekopen = 1

    return tekopen
