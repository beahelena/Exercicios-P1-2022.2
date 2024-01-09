N = int(input())
talvez_primo = 0
lista_primos = []

#ver se é primo
def validar_primo(num):
  if num == 1:
    return False
  elif num <= 3:
    return True
  elif num % 2 == 0 or num % 3 == 0:
    return False
  elif num == 5 or num == 7:
    return True
  else:
    i = 5
    while(i * i <= num) : 
        if (num % i == 0 or num % (i + 2) == 0) : 
            return False
        i = i + 6
    return True

#fazer lista com numeros primos entre 1 e N
def lista():
  talvez_primo = N-1
  while talvez_primo != 1:
    if validar_primo(talvez_primo):
      lista_primos.insert(0, talvez_primo)
    talvez_primo -= 1
  return lista_primos

#rodar código
if validar_primo(N):
  print(f'O número {N} é primo.')
else:
  print(f"O número {N} não é primo.")
  if N == 1:
    print(f"Além disso, não temos primos no intervalo de 1 à {N}.")
  else: 
    lista()
    if lista_primos:
      print(f"Entretanto, temos primos no intervalo de 1 à {N}. Estes são:")
      print(*lista_primos, sep = ', ')
print("AGORA ESTOU PRONTO PARA MINHA NOVA VIDA!")