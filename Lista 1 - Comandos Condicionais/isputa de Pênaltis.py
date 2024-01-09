time1 = input("")
time2 = input("")

gols1 = 0
gols2 = 0
chances_time1 = 5
chances_time2 = 5
acabou = False

entrada1 = input("")
if entrada1 == "Gol":
    gols1 += 1
chances_time1 -= 1

entrada2 = input("")
if entrada2 == "Gol":
    gols2 += 1
chances_time2 -= 1

entrada3 = input("")
if entrada3 == "Gol":
    gols1 += 1
chances_time1 -= 1

entrada4 = input("")
if entrada4 == "Gol":
    gols2 += 1
chances_time2 -= 1

entrada5 = input("")
if entrada5 == "Gol":
    gols1 += 1
chances_time1 -= 1


entrada6 = input("")
if entrada6 == "Gol":
    gols2 += 1
chances_time2 -= 1
if ((chances_time1 + gols1 >= gols2) and (chances_time2 + gols2 >= gols1)) == False:
    acabou = True
    if gols1 > gols2:
        print(
            f"{time1} vence a disputa de pênaltis por {gols1} a {gols2} e avança de fase!")
    if gols2 > gols1:
        print(
            f"{time2} vence a disputa de pênaltis por {gols2} a {gols1} e avança de fase!")

if not acabou:
    entrada7 = input("")
    if entrada7 == "Gol":
        gols1 += 1
    chances_time1 -= 1
    if ((chances_time1 + gols1 >= gols2) and (chances_time2 + gols2 >= gols1)) == False:
        acabou = True
        if gols1 > gols2:
            print(
                f"{time1} vence a disputa de pênaltis por {gols1} a {gols2} e avança de fase!")
        else:
            print(
                f"{time2} vence a disputa de pênaltis por {gols2} a {gols1} e avança de fase!")

if not acabou:
    entrada8 = input("")
    if entrada8 == "Gol":
        gols2 += 1
    chances_time2 -= 1
    if ((chances_time1 + gols1 >= gols2) and (chances_time2 + gols2 >= gols1)) == False:
        acabou = True
        if gols1 > gols2:
            print(
                f"{time1} vence a disputa de pênaltis por {gols1} a {gols2} e avança de fase!")
        if gols2 > gols1:
            print(
                f"{time2} vence a disputa de pênaltis por {gols2} a {gols1} e avança de fase!")

if not acabou:
    entrada9 = input("")
    if entrada9 == "Gol":
        gols1 += 1
    chances_time1 -= 1
    if ((chances_time1 + gols1 >= gols2) and (chances_time2 + gols2 >= gols1)) == False:
        acabou = True
        if gols1 > gols2:
            print(
                f"{time1} vence a disputa de pênaltis por {gols1} a {gols2} e avança de fase!")
        if gols2 > gols1:
            print(
                f"{time2} vence a disputa de pênaltis por {gols2} a {gols1} e avança de fase!")

if not acabou:
    entrada10 = input("")
    if entrada10 == "Gol":
        gols2 += 1
    if gols1 > gols2:
        print(
            f"{time1} vence a disputa de pênaltis por {gols1} a {gols2} e avança de fase!")
    elif gols2 > gols1:
        print(
            f"{time2} vence a disputa de pênaltis por {gols2} a {gols1} e avança de fase!")
    elif gols1 == gols2:
        print(
            f"Ambas as seleções terminaram com {gols1} gols, mas o desempate vai ficar para outro dia.")
