import random

#Evinger Bónó
jatekos = "Játékos:"
gep = "Gép: "

print("""
Kártyajáték: (Black Jack)
    A gép ellen játszik 1 játékos. Kap kettő lapot, 16 tól megállhat, alatta újat kell húzzon. Ha megállt,
    akkor a gép megmutatja a lapjait. Az nyer, aki kevesebb lapból közelebb van a 21-hez. Aki túllépte az
    veszít! 
""")

#Csiszér Alex Dominik
def lapKivalasztas(lapok):
    lap = ""
    randomLap = random.randint(1, 11)
    if randomLap == 10:
        random10 = random.randint(1, 3)
        if random10 == 1:
            lap = lapok[9]
        elif random10 == 2:
            lap = lapok[10]
        elif random10 == 3:
            lap = lapok[11]
    elif randomLap == 11:
        lap = lapok[12]
    else:
        lap = lapok[randomLap]

    return lap

def lapErtek(lap):
    if lap == "K":
        lap = 10
    elif lap == "J":
        lap = 10
    elif lap == "Q":
        lap = 10
    elif lap == "A":
        # Még nincs kész 11 vagy 1 értéke legyen
        lap = 11
    else:
        lap = int(lap)

    if lap < 10 and lap > 0:
        ertek = lap
    elif lap == 10:
        ertek = 10
    elif lap == 11:
        ertek = 11

    return ertek

def gepKiiras():
    print(f"{gep}", end="")
    for i in range(len(gepLapokErtek)):
        print(f"X ", end="")
    print()
def jatekosKiiras():
    print(f"{jatekos} ", end="")  # Kiíratás rész
    for i in jatekosLapok:
        print(i, end=" ")
    print()

def huzas():
    #Csiszér Alex Dominik, Evinger Bónó

    # Játékos
    jatekosLapja = lapKivalasztas(lapokLista)

    jatekosLapokErtek.append(lapErtek(jatekosLapja))
    jatekosLapok.append(jatekosLapja)
    jatekosKiiras()

    # Gép
    gepLapjai = lapKivalasztas(lapokLista)

    if sum(gepLapokErtek) < 16:
        gepLapokErtek.append(lapErtek(gepLapjai))
        gepLapok.append(gepLapjai)
        gepKiiras()
    elif sum(gepLapokErtek) > 13 and sum(gepLapokErtek) < 22:
        szazalek = random.randint(1,10)
        if szazalek == 3:
            gepLapokErtek.append(lapErtek(gepLapjai))
            gepLapok.append(gepLapjai)
        gepKiiras()

    print()

#Lap generálása (Még nincs elmentve)
lapokLista = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "J", "K", "Q", "A"]
lap = lapKivalasztas(lapokLista)

#Lapok elmentve
jatekosLapokErtek = []
jatekosLapok = []

gepLapokErtek = []
gepLapok = []

allitas = True

while True: #még nincs kész a feltétel !!! Újra lehessen játszani
    #Furkó Norbert
    if sum(jatekosLapokErtek) > 15 and sum(jatekosLapokErtek) < 21 and allitas:
        #Hibás adatnál kérje be újra
        valasz = input("Szeretnél új lapot húzni (igen/nem)?: ")
        if valasz == "igen":
            huzas()
        else:
            allitas = False
    elif sum(jatekosLapokErtek) < 15:
        huzas()
    else:
        #Vége eldöntése: Mikor ki nyert és mikor ki vesztett
        #Csiszér Alex Dominik, Evinger Bónó Furkó Norbert
        print()
        if sum(jatekosLapokErtek) > sum(gepLapokErtek) and sum(jatekosLapokErtek) < 22:
            print("Játékos nyert!")
        elif sum(gepLapokErtek) < 22:
            print("Gép nyert!")
        else:
            print("Senki se nyert!")
        print("\nAz állás: ")

        #Játékos vége
        print(f"{jatekos} ", end="")  # Kiíratás rész
        for i in jatekosLapok:
            print(i, end=" ")
        print(f" (Értéke: {sum(jatekosLapokErtek)})")  # Kiíratás rész

        #Gép vége
        print(f"{gep}", end="")
        for i in gepLapokErtek:
            print(f"{i} ", end="")
        print(f"(Értéke: {sum(gepLapokErtek)})")

        break