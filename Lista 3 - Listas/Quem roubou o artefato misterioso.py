suspeitos = []
acabou = False

while not acabou:
  entrada = input("")
  if entrada == "novo suspeito - altissima periculosidade":
    nome_suspeito = input("")
    suspeitos.insert(0, nome_suspeito)
  if entrada == "novo suspeito - pouco perigoso":
    nome_suspeito = input("")
    suspeitos.append(nome_suspeito)
  if entrada == "livre de suspeita, pode remover":
    nome_inocente = input("")
    suspeitos.remove(nome_inocente)
  if entrada == "sujeito mais perigoso do que pensavamos":
    index_suspeito = int(input(""))
    index_novo = int(input(""))
    suspeitos[index_suspeito], suspeitos[index_novo] = suspeitos[index_novo], suspeitos[index_suspeito]
  if entrada == "que estranho, esses dois meliantes… troque-os de lugar":
    suspeito_1 = input("")
    suspeito_2 = input("")
    index_1 = int(suspeitos.index(suspeito_1))
    index_2 = int(suspeitos.index(suspeito_2))
    suspeitos.remove(suspeito_1)
    suspeitos.remove(suspeito_2)
    suspeitos.insert(index_2, suspeito_1)
    suspeitos.insert(index_1, suspeito_2)
  if entrada == "essa posicao nao esta de acordo, ele nao e tao perigoso assim":
    nome_suspeito = input("")
    suspeitos.remove(nome_suspeito)
    suspeitos.append(nome_suspeito)
  if entrada == "como a lista esta ficando?":
    print(' '.join(suspeitos))
  if entrada == "ja temos nossa lista de suspeitos":
    acabou = True

if acabou:
  print("O resultado final ficou assim:")
  print(' '.join(suspeitos))