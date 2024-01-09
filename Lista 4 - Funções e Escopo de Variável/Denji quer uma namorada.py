lista_pretendentes = []
perigosas = 0
probabilidade_pretendentes = []

#defs
def nomes(nome):
  if len(nome)>7:
    letter_list = list(nome)
    inicial = letter_list[0]+letter_list[1]
    print(f"Er {inicial}.. errr... nao consigo lembrar, melhor deixar para la")
    return False
  elif nome == "Makima":
    print("Woof Woof")
  return True

def probabilidade_def():
  global perigosas
  if probabilidade <= 50 or nome == "Makima":
    print(f"Beleza {nome}!! Essa é uma boa pretendente!")
    if nome != "Makima":
      lista_pretendentes.append(nome)
      probabilidade_pretendentes.append(probabilidade)
  else:
    perigosas += 1
    print(f"{nome}, mais uma que so quer o coraçao do chainsaw man, quando que alguem vai querer o meu coraçao!?!?")

while True:
  nome = input()
  if nome == "cabo":
    break
  else:
    if not nomes(nome):
      continue
    probabilidade = int(input())
    probabilidade_def()
  
if len(lista_pretendentes) > perigosas:
  print("Epa ai sim! E hoje pochita!!")
else:
  print("Desculpa pochita acho que nao vai ser hoje que voce vai poder ver meus sonhos")
if perigosas == 0:
  for i,j in zip(lista_pretendentes, probabilidade_pretendentes):
    print(f"nome: {i} - chances de morrer: {j}%")