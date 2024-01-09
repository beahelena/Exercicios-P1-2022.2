n = int(input())
soma_pares = 0
soma_impares = 0
prod = 1
mensagem_final = []

alfabeto = [] #lista das letras
for i in range(ord('a'), ord('z')+1):
  alfabeto.append(chr(i))

for i in range(n):
  quebra_de_linha = input()
  palavra_decodificadora = input()
  quebra_de_linha = input()
  palavra_codificada = input()
  lista_decodificada = palavra_codificada.split() #transformar palavra codificada em lista
  
  if palavra_decodificadora == "Portal":
    palavra_descoberta = ''
    letra = None
    for char in lista_decodificada:
      if char in alfabeto:
        if char == "z":
          letra = "a"
          palavra_descoberta = palavra_descoberta+letra
        else:
          letra = alfabeto[(alfabeto.index(char)+1)] #descobrir a próxima letra do alfabeto
          palavra_descoberta = palavra_descoberta+letra
    if palavra_descoberta != '':
      mensagem_final.append(palavra_descoberta)
  
  if palavra_decodificadora == "Experimento": #somar os números pares da lista
    for char in lista_decodificada:
      if char.isdigit():
        if int(char)%2 == 0:
          soma_pares += int(char)
    if soma_pares != 0:
      mensagem_final.append(str(soma_pares))
  
  if palavra_decodificadora == "Schembulock": #multiplicação de todos os números
    for char in lista_decodificada:
      if char.isdigit():
        prod *= int(char)
    if prod != 1:
      mensagem_final.append(str(prod))
  
  if palavra_decodificadora == "Realidade": #somar os números ímpares
    for char in lista_decodificada:
      if char.isdigit():
        if int(char)%2 != 0:
          soma_impares += int(char)
    mensagem_final.append(str(soma_impares))

if mensagem_final: #se a lista da mensagem não estiver vazia
  print("Consegui! A mensagem decodificada de Bill Cipher é: " + ' '.join(mensagem_final))
else:
  print("Esse formato de mensagem nem Bill Cipher entenderia!")