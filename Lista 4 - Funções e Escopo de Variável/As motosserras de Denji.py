#defs

def chainsaw():
  if denji_energy >= 750 and denji_control >= 7 and denji_precision >= 8:
    chainsaw_choice = "Motosserra Suprema"
  elif denji_energy >= 500 and denji_control >= 6 and denji_precision >= 6:
    chainsaw_choice = "Motosserra Avançada"
  else:
    chainsaw_choice = "Motosserra Normal"
  return chainsaw_choice

def battle_message():
  if denji_force > enemy_force:
    print(f"Denji saiu vitorioso nessa batalha contra o {i}")
    battle_result_list.append("Vitoria")
  elif denji_force < enemy_force:
    print(f"Denji não conseguiu força o suficiente para derrotar o {i}")
    battle_result_list.append("Derrota")
  else:
    print(f"Como pode ser possível?? Denji possui a mesma força que o {i}")
    battle_result_list.append("Empate")

#####################
villain_list = ["Makima", "Reze", "Santa Claus"]

chainsaw_list = []
battle_result_list = []
rodada = 1

for i in villain_list:
  denji_energy = int(input())
  denji_control = int(input())
  denji_precision = int(input())
  enemy_force = int(input())
  denji_force = denji_energy + (denji_control*denji_precision)
  
  print(f"### Rodada {rodada} - {i} ###")
  chainsaw_list.append(chainsaw())
  print(f"O Denji ira se transformar na {chainsaw()} para enfrentar o {i}")
  battle_message()
  rodada += 1

print("### Resultado Final ###")
count = 1
index = 0
for i in range(3):
  print(f"Rodada {count}: {chainsaw_list[index]} - {battle_result_list[index]}")
  count += 1
  index += 1

if battle_result_list.count("Vitoria") == 3:
  print("Nenhum dos 3 inimigos foram capazes de derrotar o Denji!")
if battle_result_list.count("Derrota") == 3:
  print("Hoje não foi um dia bom para o Denji, perdeu todas as batalhas")
if battle_result_list.count("Vitoria") == 1 and battle_result_list.count("Derrota") == 1 and battle_result_list.count("Empate") == 1:
  print("Hoje foi um dia equilibrado para o Denji, conseguiu ganhar, perder e empatar")
if battle_result_list.count("Vitoria") == 2:
  print("Denji conseguiu derrotar a maioria de seus inimigos")
if battle_result_list.count("Derrota") == 2:
  print("Dia péssimo para o Denji, perdeu a maioria de suas batalhas")
if battle_result_list.count("Empate") == 2:
  print("Dia duro para o Denji, empatou de mais")