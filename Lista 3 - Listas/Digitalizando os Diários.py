n = int(input(""))
diario_1 = []
diario_2 = []
diario_3 = []

for i in range(n):
  entrada_1 = input()
  conteudo, numero_diario = entrada_1.split(", ")
  numero_diario_inteiro = int(numero_diario)
  if numero_diario_inteiro == 1:
    diario_1.append(conteudo)
  elif numero_diario_inteiro == 2:
    diario_2.append(conteudo)
  elif numero_diario_inteiro == 3:
    diario_3.append(conteudo)

m = int(input(""))

for i in range(m):
  conteudo_buscado = input()
  if conteudo_buscado in diario_1:
    print(f"Informacoes sobre {conteudo_buscado} estao no Diario 1")
  elif conteudo_buscado in diario_2:
    print(f"Informacoes sobre {conteudo_buscado} estao no Diario 2")
  elif conteudo_buscado in diario_3:
    print(f"Informacoes sobre {conteudo_buscado} estao no Diario 3")
  else:
    print(f"Nenhum dos diarios possui informacoes sobre {conteudo_buscado}")