n = int(input())

doguinhos_list = []
for i in range(n):
  info = input()
  a= info.split()
  b = a[2].split("/")
  dic = {"name": a[0], "especie": a[1], "birth_date": int(b[1])}
  doguinhos_list.append(dic)

month = int(input())
new_list = []
for doguinhos in doguinhos_list:
  if int(doguinhos["birth_date"]) == month:
    new_list.append(doguinhos)
  else:
    continue

if new_list:
  new_list_sorted = sorted(new_list, key=lambda x: x["name"])
  print("E os donos da festa do mes sao:")
  for i in new_list_sorted:
    print(i["name"], "-", i["especie"])
else:
  print("Sem festa esse mes. :(")