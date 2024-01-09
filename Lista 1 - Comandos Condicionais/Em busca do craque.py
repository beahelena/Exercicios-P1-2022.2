nome1 = input("")
grande_area1 = int(input(""))
finalizacoes1 = int(input(""))
gols1 = int(input(""))

nome2 = input("")
grande_area2 = int(input(""))
finalizacoes2 = int(input(""))
gols2 = int(input(""))

nome3 = input("")
grande_area3 = int(input(""))
finalizacoes3 = int(input(""))
gols3 = int(input(""))

aproveitamento1 = (gols1/finalizacoes1)*100
aproveitamento2 = (gols2/finalizacoes2)*100
aproveitamento3 = (gols3/finalizacoes3)*100
melhor_jogador = ""
grande_area_jogador_escolhido = 0

if grande_area1 == grande_area2 > grande_area3:
  print("Tite está mais indeciso do que nunca!")
if grande_area1 == grande_area3 > grande_area2:
  print("Tite está mais indeciso do que nunca!")
if grande_area2 == grande_area3 > grande_area1:
  print("Tite está mais indeciso do que nunca!")
if grande_area2 == grande_area3 == grande_area1:
  print("Tite está mais indeciso do que nunca!")

if grande_area1 > grande_area2 > grande_area3:
  print(nome1)
  print(nome2)
  print(nome3)
  melhor_jogador = nome1
  grande_area_jogador_escolhido = grande_area1

if grande_area1 > grande_area3 > grande_area2:
  print(nome1)
  print(nome3)
  print(nome2)
  melhor_jogador = nome1
  grande_area_jogador_escolhido = grande_area1

if grande_area2 > grande_area1 > grande_area3:
  print(nome2)
  print(nome1)
  print(nome3)
  melhor_jogador = nome2
  grande_area_jogador_escolhido = grande_area2

if grande_area2 > grande_area3 > grande_area1:
  print(nome2)
  print(nome3)
  print(nome1)
  melhor_jogador = nome2
  grande_area_jogador_escolhido = grande_area2

if grande_area3 > grande_area2 > grande_area1:
  print(nome3)
  print(nome2)
  print(nome1)
  melhor_jogador = nome3
  grande_area_jogador_escolhido = grande_area3

if grande_area3 > grande_area1 > grande_area2:
  print(nome3)
  print(nome1)
  print(nome2)
  melhor_jogador = nome3
  grande_area_jogador_escolhido = grande_area3

if grande_area1 == grande_area2 > grande_area3:
  if aproveitamento1 > aproveitamento2:
    print(nome1)
    print(nome2)
    print(nome3)
    melhor_jogador = nome1
  grande_area_jogador_escolhido = grande_area1
  if aproveitamento1 < aproveitamento2:
    print(nome2)
    print(nome1)
    print(nome3)
    melhor_jogador = nome2
    grande_area_jogador_escolhido = grande_area2

if grande_area1 == grande_area3 > grande_area2:
  if aproveitamento1 > aproveitamento3:
    print(nome1)
    print(nome3)
    print(nome2)
    melhor_jogador = nome1
    grande_area_jogador_escolhido = grande_area1
  if aproveitamento1 < aproveitamento3:
    print(nome3)
    print(nome1)
    print(nome2)
    melhor_jogador = nome3
    grande_area_jogador_escolhido = grande_area3

if grande_area2 == grande_area3 > grande_area1:
  if aproveitamento2 > aproveitamento3:
    print(nome2)
    print(nome3)
    print(nome1)
    melhor_jogador = nome2
    grande_area_jogador_escolhido = grande_area2
  if aproveitamento2 < aproveitamento3:
    print(nome3)
    print(nome2)
    print(nome1)
    melhor_jogador = nome3
    grande_area_jogador_escolhido = grande_area3

if grande_area3 > grande_area1 == grande_area2:
  if aproveitamento1 > aproveitamento2:
    print(nome3)
    print(nome1)
    print(nome2)
    melhor_jogador = nome3
    grande_area_jogador_escolhido = grande_area3
  if aproveitamento1 < aproveitamento2:
    print(nome3)
    print(nome2)
    print(nome1)
    melhor_jogador = nome3
    grande_area_jogador_escolhido = grande_area3

if grande_area2 > grande_area1 == grande_area3:
  if aproveitamento1 > aproveitamento3:
    print(nome2)
    print(nome1)
    print(nome3)
    melhor_jogador = nome2
    grande_area_jogador_escolhido = grande_area2
  if aproveitamento1 < aproveitamento3:
    print(nome2)
    print(nome3)
    print(nome1)
    melhor_jogador = nome2
    grande_area_jogador_escolhido = grande_area2

if grande_area1 > grande_area2 == grande_area3:
  if aproveitamento2 > aproveitamento3:
    print(nome1)
    print(nome2)
    print(nome3)
    melhor_jogador = nome1
    grande_area_jogador_escolhido = grande_area1
  if aproveitamento2 < aproveitamento3:
    print(nome1)
    print(nome3)
    print(nome2)
    melhor_jogador = nome1
    grande_area_jogador_escolhido = grande_area1

if grande_area2 == grande_area3 == grande_area1:
  if aproveitamento1 > aproveitamento2 > aproveitamento3:
    print(nome1)
    print(nome2)
    print(nome3)
    melhor_jogador = nome1
    grande_area_jogador_escolhido = grande_area1
  if aproveitamento1 > aproveitamento3 > aproveitamento2:
    print(nome1)
    print(nome3)
    print(nome2)
    melhor_jogador = nome1
    grande_area_jogador_escolhido = grande_area1
  if aproveitamento2 > aproveitamento1 > aproveitamento3:
    print(nome2)
    print(nome1)
    print(nome3)
    melhor_jogador = nome2
    grande_area_jogador_escolhido = grande_area2
  if aproveitamento2 > aproveitamento3 > aproveitamento1:
    print(nome2)
    print(nome3)
    print(nome1)
    melhor_jogador = nome2
    grande_area_jogador_escolhido = grande_area2
  if aproveitamento3 > aproveitamento1 > aproveitamento2:
    print(nome3)
    print(nome1)
    print(nome2)
    melhor_jogador = nome3
    grande_area_jogador_escolhido = grande_area3
  if aproveitamento3 > aproveitamento2 > aproveitamento1:
    print(nome3)
    print(nome2)
    print(nome1)
    melhor_jogador = nome3
    grande_area_jogador_escolhido = grande_area3

print("Finalmente o técnico da seleção brasileira liberou a escalação completa do time! O ponta-direita escolhido foi…")
if grande_area_jogador_escolhido <= 10:
  print(f"{melhor_jogador}?! Sei não hein Galvão…")
else:
  print(f"{melhor_jogador}! Dessa vez o hexa vem pra casa!!")