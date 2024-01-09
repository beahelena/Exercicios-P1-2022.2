m = int(input())

aprovados = []
reprovados = []
recuperacao = []
for i in range(m):
  string = input().split(', ')
  media = (float(string[2]) + float(string[3]) + float(string[4]))/3
  dic = {"nome": string[0], "raca": string[1], "nota": "{:.2f}".format(media)}
  if media >= 3:
    aprovados.append(dic)
  elif media < 2:
    reprovados.append(dic)
  else:
    recuperacao.append(dic)

if aprovados:
  print("Estao aprovados e de parabens os seguintes coleguinhas:")
  for i in aprovados:
    print(i["nome"], "-", i["raca"], "- media:", i["nota"])
if reprovados:
  print("Os colegas a seguir nao se comportaram bem e precisam de ajuda profissional (entrar em contato urgente):")
  for i in reprovados:
    print(i["nome"], "-", i["raca"], "- media:", i["nota"])
if recuperacao:
  print("Esses queridos terao uma nova chance e prometem melhorar:")
  for i in recuperacao:
    print(i["nome"], "-", i["raca"], "- media:", i["nota"])