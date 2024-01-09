binario = int(input(""))
n = len(str(binario))
decimal = 0
i = 0

while n >= 0:
  resto = binario % 10
  decimal = decimal + (resto * (2**i))
  n -= 1
  i += 1
  binario = binario // 10

tentativas = 3

while tentativas > 0:
  tentativas -= 1
  palpite = int(input(""))
  if palpite == decimal:
    print("Parabéns!! Você acertou!")
    if palpite == 1:
      print("Férias inesquecíveis estão te esperando!")
      print("Seu destino será Porto de Galinhas (BRA).")
      print("Prepare-se para viver dias incríveis desfrutando das riquezas naturais da nossa região!")
      break
    elif palpite == 2:
      print("Férias inesquecíveis estão te esperando!")
      print("Seu destino será Fernando de Noronha (BRA).")
      print("Belíssimas praias estão por vir.")
      print("Não esqueça o protetor solar.")
      break
    elif palpite == 3:
      print("Férias inesquecíveis estão te esperando!")
      print("Seu destino será Gramado (BRA).")
      print("Aproveite passeios e paisagens espetaculares no sul do país!")
      break
    elif palpite == 4:
      print("Férias inesquecíveis estão te esperando!")
      print("Seu destino será Berlim (ALE).")
      print("Desfrute de muita cultura e de experiências incríveis!")
      print("Prepare os casacos de frio!")
      break
    elif palpite == 5:
      print("Férias inesquecíveis estão te esperando!")
      print("Seu destino será Tóquio (JPN).")
      print("Viva uma experiência inesquecível explorando um país do outro lado do mundo.")
      print("Prepare-se para muitas horas de voo!")
      break
    else:
      print("Mas, infelizmente, hoje não é o seu dia de sorte.")
      print("Apesar de ter dado a resposta correta, seu bilhete não oferece nenhum prêmio.")
      print("Sinta-se à vontade para conhecer nossos pacotes e outras promoções imperdíveis com um de nossos vendedores!")
      break
  if palpite != decimal and tentativas > 0:
    print(f"Resposta incorreta. Mas não desista! Você ainda tem {tentativas} chance(s).")
  if palpite != decimal and tentativas == 0:
    if decimal == 1 or decimal == 2 or decimal == 3 or decimal == 4 or decimal == 5:
      print("Infelizmente mais uma resposta incorreta.")
      print("Agradecemos sua participação!")
      print("Seu bilhete era premiado. Que pena!")
      break
    if decimal != 1 or decimal != 2 or decimal != 3 or decimal != 4 or decimal != 5:
      print("Infelizmente mais uma resposta incorreta.")
      print("Agradecemos sua participação!")
      print("Pelo menos seu bilhete não era premiado.")
      print("Sinta-se à vontade para conhecer nossos pacotes e outras promoções imperdíveis com um de nossos vendedores!")