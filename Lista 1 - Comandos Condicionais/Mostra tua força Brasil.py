favoritismobr = int(input(""))
NomeOponente1 = input("")
FavoritismoOponente1 = int(input(""))
GolsBR1 = int(input(""))
GolsOPO1 = int(input(""))

perdeu = False
if GolsBR1 > GolsOPO1:
  print("Quem é que segura o Brasil???")
  if GolsBR1 - GolsOPO1 == 1:
    favoritismobr = favoritismobr + 10
  if GolsBR1 - GolsOPO1 == 2:
    favoritismobr = favoritismobr + 20
  if GolsBR1 - GolsOPO1 >= 3:
    favoritismobr = favoritismobr + 30
elif GolsBR1 < GolsOPO1:
  print(f"Infelizmente essa seleção dx {NomeOponente1} era muito forte para o Brasil.")
  perdeu = True
elif GolsBR1 == GolsOPO1:
  if favoritismobr > FavoritismoOponente1:
    print("No sufoco, o Brasil conseguiu ganhar!!!")
  else:
    perdeu = True
    print("Foi no detalhe! Mas infelizmente o Brasil esta eliminado da copa...")

if not perdeu:
  NomeOponente2 = input("")
  FavoritismoOponente2 = int(input(""))
  GolsBR2 = int(input(""))
  GolsOPO2 = int(input(""))
  if GolsBR2 > GolsOPO2:
    print("Quem é que segura o Brasil???")
    if GolsBR2 - GolsOPO2 == 1:
      favoritismobr = favoritismobr + 10
    if GolsBR2 - GolsOPO2 == 2:
      favoritismobr = favoritismobr + 20
    if GolsBR2 - GolsOPO2 >= 3:
      favoritismobr = favoritismobr + 30
  elif GolsBR2 < GolsOPO2:
    print(f"Infelizmente essa seleção dx {NomeOponente2} era muito forte para o Brasil.")
    perdeu = True
  elif GolsBR2 == GolsOPO2:
    if favoritismobr > FavoritismoOponente2:
      print("No sufoco, o Brasil conseguiu ganhar!!!")
    else:
      perdeu = True
      print("Foi no detalhe! Mas infelizmente o Brasil esta eliminado da copa...")

if not perdeu:
  NomeOponente3 = input("")
  FavoritismoOponente3 = int(input(""))
  GolsBR3 = int(input(""))
  GolsOPO3 = int(input(""))
  if GolsBR3 > GolsOPO3:
    print("Quem é que segura o Brasil???")
    if GolsBR3 - GolsOPO3 == 1:
      favoritismobr = favoritismobr + 10
    if GolsBR3 - GolsOPO3 == 2:
      favoritismobr = favoritismobr + 20
    if GolsBR3 - GolsOPO3 >= 3:
      favoritismobr = favoritismobr + 30
  elif GolsBR3 < GolsOPO3:
    print(f"Infelizmente essa seleção dx {NomeOponente3} era muito forte para o Brasil.")
    perdeu = True
  elif GolsBR3 == GolsOPO3:
    if favoritismobr > FavoritismoOponente3:
      print("No sufoco, o Brasil conseguiu ganhar!!!")
    else:
      print("Foi no detalhe! Mas infelizmente o Brasil esta eliminado da copa...")
      perdeu = True

if not perdeu:
  NomeOponente4 = input("")
  FavoritismoOponente4 = int(input(""))
  if favoritismobr > FavoritismoOponente4:
    print("O BRASIL VAI SER HEXAAAAAAAA")
  else:
    print(f"O nosso Brasil foi vice, não conseguindo bater a seleção dx {NomeOponente4} na simulação")