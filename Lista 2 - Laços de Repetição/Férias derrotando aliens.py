frase = input("")

frase_final_1 = "O relógio descarregou!"
frase_final_2 = "Por hoje já deu"
contador = 0

while ((frase != frase_final_1) and (frase!=frase_final_2)):
  frase = input("")
  contador += 1
else:
  if frase == frase_final_1:
    print(f"Corra Ben! Você já derrotou {contador} aliens")
  else:
    print(f"Muito Ben Ben! hehe você derrotou {contador} aliens hoje")