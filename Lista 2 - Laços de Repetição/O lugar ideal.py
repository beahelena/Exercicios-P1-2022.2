lugares = int(input(""))
melhor_lugar = None
pior_lugar = None
soma_notas = 0
maior_nota = 0
pior_nota = 0
continua = True
empate = False

while lugares > 0:
  nome_lugar = str(input(""))
  lugares -= 1
  while continua:
    nota = float(input(""))
    if nota < 0:
      if maior_nota < soma_notas:
        maior_nota = 0 + soma_notas
        melhor_lugar = nome_lugar
        empate = False
      elif maior_nota == soma_notas:
        melhor_lugar = melhor_lugar + ", " + nome_lugar
        empate = True
      if pior_nota == 0:
        pior_nota = soma_notas
        pior_lugar = nome_lugar
      if pior_nota > 0:
        if soma_notas < pior_nota:
          pior_nota = 0 + soma_notas
          pior_lugar = nome_lugar
      soma_notas = 0
      nome_lugar = None
      break
    soma_notas += nota
else:
  if not empate:
    print(f"{melhor_lugar} ganhou de lavada de {pior_lugar}, com {int(maior_nota)} vs {int(pior_nota)}")
  else:
    print(melhor_lugar)
    print("Tantas opções")