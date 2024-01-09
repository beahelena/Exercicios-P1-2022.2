demons_list = []
#defs
def ascii_sum():
  sum = 0
  for char in demon_name:
    ascii_val = ord(char)
    sum += ascii_val
  return sum

def add(demons_list, index_jail, demon_name, jails):
  if not "0" in demons_list:
    print("CHEIO")
  elif demons_list[index_jail] == "0": #cela vazia
    demons_list[index_jail] = demon_name
  else:
    count = 1
    while count < int(jails) and demons_list[index_jail] != "0":
      index_jail = (index_jail + 1) % int(jails)
      count += 1
    if demons_list[index_jail] == "0":
      demons_list[index_jail] = demon_name

def remove(demon_name, demons_list):
  if demon_name in demons_list:
    index = int(demons_list.index(demon_name))
    demons_list[index] = "0"
  else:
    print("NAO EXISTE")

##primeiro input##
jails, orders = input().split()

##criar lista dos demônios##
for i in range(int(jails)):
  demons_list.append("0")

##segundo input##
for i in range(int(orders)):
  order, demon_name = input().split()
  index_jail = ascii_sum() % int(jails)
  if order == "ADICIONAR":
    add(demons_list, index_jail, demon_name, jails)
  else:
    remove(demon_name, demons_list)
    

## Impressão da lista de demônios ##
final_list = []
for i in demons_list:
  if i != "0":
    final_list.append(i)
print(" ".join(final_list))