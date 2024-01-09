nome_jogador = input("")

posicao = None

if nome_jogador == "Alisson":
  posicao = "goleiro"
elif nome_jogador == "Ederson":
  posicao = "goleiro"
elif nome_jogador == "Weverton":
  posicao = "goleiro"
elif nome_jogador == "Marquinhos":
  posicao = "zagueiro"
elif nome_jogador == "Thiago Silva":
  posicao = "zagueiro"
elif nome_jogador == "Éder Militão":
  posicao = "zagueiro"
elif nome_jogador == "Bremer":
  posicao = "zagueiro"
elif nome_jogador == "Daniel Alves":
  posicao = "lateral"
elif nome_jogador == "Danilo":
  posicao = "lateral"
elif nome_jogador == "Alex Sandro":
  posicao = "lateral"
elif nome_jogador == "Alex Telles":
  posicao = "lateral"
elif nome_jogador == "Casemiro":
  posicao = "meia"
elif nome_jogador == "Fabinho":
  posicao = "meia"
elif nome_jogador == "Fred":
  posicao = "meia"
elif nome_jogador == "Bruno Guimarães":
  posicao = "meia"
elif nome_jogador == "Lucas Paquetá":
  posicao = "meia"
elif nome_jogador == "Everton Ribeiro":
  posicao = "meia"
elif nome_jogador == "Neymar":
  posicao = "atacante"
elif nome_jogador == "Raphinha":
  posicao = "atacante"
elif nome_jogador == "Vini Jr.":
  posicao = "atacante"
elif nome_jogador == "Antony":
  posicao = "atacante"
elif nome_jogador == "Richarlison":
  posicao = "atacante"
elif nome_jogador == "Rodrygo":
  posicao = "atacante"
elif nome_jogador == "Pedro":
  posicao = "atacante"
elif nome_jogador == "Gabriel Jesus":
  posicao = "atacante"
elif nome_jogador == "Gabriel Martinelli":
  posicao = "atacante"

if posicao != None:
  print(f"{nome_jogador} foi convocado e jogará como {posicao}!")

else:
  print(f"{nome_jogador} não foi convocado, mas quem sabe na próxima?")