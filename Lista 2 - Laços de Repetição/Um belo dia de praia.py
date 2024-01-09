protetor_solar = False
acabou = False
clima = "ensolarado"
carteira = 0

while not acabou:
  entrada = input("")
  if entrada == "separar dinheiro":
    dinheiro = float(input(""))
    carteira += dinheiro
  if entrada == "passar protetor":
    protetor_solar = True
  if entrada == "choveu":
    clima = "chuvoso"
  if entrada == "parou de chover":
    clima = "ensolarado"
  if entrada == "ir para a praia":
    acabou = True
else:
  if clima == "chuvoso":
    print("Hoje não vai dar pra ir, chuvinha barrou")
  elif clima == "ensolarado":
    print("Hoje tem sol e mar!")
    if protetor_solar == False and carteira < 10:
      print("Você não chegou muito bem, chame um médico!")
    if protetor_solar == False and carteira >= 10:
      print("O novo camarão do CIn foi criado")
    if protetor_solar == True and carteira < 10:
      print("Só faltou uma aguinha de coco...")
    if protetor_solar == True and carteira >= 10:
      print("Aí sim! Hoje rendeu!")