inimigo = input()
aliado = input()
clima = input()

#receber mensagens
lista_mensagens = []
Cansado = False
while not Cansado:
  mensagem = input()
  if mensagem == "Cansado":
    Cansado = True
    break
  lista_mensagens.append(list(map(int, mensagem.split())))

#caso o clima seja diferentes dos inputs
if clima not in ["Ensolarado", "Nublado", "ChuvosoNormal", "ChuvosoComRaio"]:
  print("Infelizmente esse clima não está bom. Não conseguimos decifrar a mensagem, o que será do mundo agora??")
  print(f"Tenho certeza que conseguiremos na próxima {aliado}")

#decodificar as mensagens
else:
  if clima == "Ensolarado":
    for i in range (len(lista_mensagens)):
        for j in range (len(lista_mensagens[i])-1, 0, -1):
            for k in range (j):
                if lista_mensagens[i][k] > lista_mensagens[i][k+1]:
                  lista_mensagens[i][k], lista_mensagens[i][k+1] = lista_mensagens[i][k+1], lista_mensagens[i][k]
    print(f"Caramba! Finalmente organizamos a mensagem secreta do {inimigo} com esse clima Ensolarado! Vamos nessa {aliado}!")
  
  
  if clima == "Nublado": #ordenar os números do maior para o menor
    for i in range (len(lista_mensagens)):
        for j in range (len(lista_mensagens[i])-1, 0, -1):
            for k in range (j):
                if lista_mensagens[i][k] < lista_mensagens[i][k+1]:
                  lista_mensagens[i][k], lista_mensagens[i][k+1] = lista_mensagens[i][k+1], lista_mensagens[i][k]
    print(f"Ufa! Mesmo com o clima Nublado ainda desvendamos a mensagem do {inimigo}! Vamos nessa {aliado}!")
  
  if clima == "ChuvosoNormal": #comparar itens e substituir quando o primeiro for menor
    for i in range(len(lista_mensagens)-1):
      for j in range(len(lista_mensagens[i])):
        if lista_mensagens[i][j] < lista_mensagens[i+1][j]:
          lista_mensagens[i][j], lista_mensagens[i+1][j] = lista_mensagens[i+1][j], lista_mensagens[i][j]
    print(f"Nem mesmo a chuva vai nos parar de salvar o mundo! Desvendamos a mensagem do {inimigo}! Vamos nessa {aliado}!")
  
  if clima == "ChuvosoComRaio": #comparar itens e substituir quando o primeiro for maior
    for i in range(len(lista_mensagens)-1):
      for j in range(len(lista_mensagens[i])):
        if lista_mensagens[i][j] > lista_mensagens[i+1][j]:
          lista_mensagens[i][j], lista_mensagens[i+1][j] = lista_mensagens[i+1][j], lista_mensagens[i][j]
    print(f"Eitaa! Até mesmo essa chuva com trovoadas não nos parou. Estamos indo até você, {inimigo}! Vamos nessa {aliado}!")
  
  quantidade = int(len(lista_mensagens)) #quantidade de mensagens
  print(f"Agora decodificamos as {quantidade} mensagens do {inimigo} e sabemos seus {quantidade} lugares de ataque.")
  print("Os lugares sao:")
  for i in range (quantidade):
    print(f"{i+1} lugar:")
    print(f"Coordenadas: {lista_mensagens[i][0]}° {lista_mensagens[i][1]}' {lista_mensagens[i][2]}''")
    print(f"Horario: {lista_mensagens[i][3]}h {lista_mensagens[i][4]}m {lista_mensagens[i][5]}s")
    print(f"Data: {lista_mensagens[i][6]}/{lista_mensagens[i][7]}/{lista_mensagens[i][8]}")
  print(f"Vamos rapido {aliado}!!")