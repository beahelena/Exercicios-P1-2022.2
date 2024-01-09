chatgpt_answer = ''
def compressed_message(phrase):
  if len(phrase) == 0:
    return ""
  else:
    letter = phrase[0]
    letter_count = 1
    while letter_count < len(phrase) and letter == phrase[letter_count]:
      letter_count += 1
    return str(letter_count)+letter+compressed_message(phrase[letter_count:])

def translation(chatgpt_answer):
  if len(chatgpt_answer) == 0:
    return ""
  else:
    num = int(chatgpt_answer[0])
    letter = chatgpt_answer[1]
    return letter * num + translation(chatgpt_answer[2:])

def num_sum(cm):
  soma = 0
  list_compressed = list(cm)
  for i in list_compressed:
    if i.isdigit():
      soma += int(i)
  return soma

while True:
  soma = 0
  a = input()
  if a == "Vou pedir ajuda pro meu amigo ChatGPT":
    over = False
    while not over:
      phrase = input()
      if phrase == "Não tô entendendo nada":
        over = True
      else:
        print(f"usuário:{compressed_message(phrase)}")
        cm = compressed_message(phrase)
        chatgpt_answer = ''
        if 0 < num_sum(cm) <= 5:
          chatgpt_answer = "1t3a1 1f1a1c3i1n1h1o1 1n3e"
        elif 6 < num_sum(cm) <= 20:
          chatgpt_answer = "1c2o2m2p2r3e1 1u3m1 1t2e1c1l1a1d1o1 1n4o1v1o"
        elif 21 < num_sum(cm) <= 30:
          chatgpt_answer = "1s6o1 1n1a1 1v1i1d2a1 1m4a1n1s3a"
        elif 31 < num_sum(cm) <= 40:
          chatgpt_answer = "1v5a1 1e2s1t4u3d3a3r1 1r1a1p3a3z"
        else:
          chatgpt_answer = "3e1s1t5u1d1a1 1n2a1o1 1p1r3a1 1t2u1 1v4e1r"
        print(f"ChatGPT:{chatgpt_answer}")
  elif a == "Qual era a tradução?":
    if chatgpt_answer:
      print(f"Descobri! É: {translation(chatgpt_answer)}, tá de brincadeira né?")
    else:
      print("Não tem nada pra traduzir")
  else:
    break