n = int(input())
mensagem_final = ''

for i in range(n):
  msg_cod = input()
  msg_cod = msg_cod.replace("-"," ")
  lista_msg_cod = msg_cod.split()
  index_seq_fib = lista_msg_cod[0]
  index_numero1 = lista_msg_cod[1]
  index_numero2 = lista_msg_cod[2]
  
  #sequencia de fibonacci
  fibonacci_lista = [0, 1]
  for i in range(int(index_seq_fib)-1):
    num_fibonacci = fibonacci_lista[-1] + fibonacci_lista[-2]
    fibonacci_lista.append(num_fibonacci)
  
  #tranformar numero de fibonacci em lista
  lista_strings = list(str(fibonacci_lista[-1]))
  numero_ascii = int(lista_strings[int(index_numero1)]+lista_strings[int(index_numero2)])
  letra = chr(numero_ascii)
  mensagem_final += letra
print(mensagem_final)