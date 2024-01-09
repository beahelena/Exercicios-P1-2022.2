selecao1 = input("")
selecao2 = input("")

aposta = int(input(""))

prob = float(input(""))
if (prob >= 0.5) :
    print("Pedro, você está proibido de apostar nos favoritos, só em zebra, lembra?")
    
resultado = str(input(""))

valor = int(aposta*(1+(0.5-prob)**2*100))

if (prob < 0.5):
    if resultado == "Ganhou":
        if 0.4 < prob < 0.5:
            print(f"Não foi um palpite tão arriscado, todos sabiam que {selecao1} não estava muito atrás de {selecao2}")
        elif 0.3 < prob <= 0.4:
            print(f"Eu pensava que {selecao2} iria ganhar, mas nunca duvidei que a {selecao1} pudesse ganhar essa partida")
        elif 0.2 < prob <= 0.3:
            print(f"Uau! que jogo foi esse?? {selecao1} surpreendeu a todos nós…")
        elif 0.1 < prob <=0.2:
            print(f"Essa é a copa das zebras?? O impossível aconteceu hoje nessa partida, como que {selecao1} ganhou de {selecao2}, alguém me explica?")
        elif prob <= 1:
            print(f"PEDROOOOO, você tá rico!! ninguém, absolutamente ninguém apostou na {selecao1}, somente você!")
        print(f"Parabéns, você apostou R${aposta} e recebeu R${valor} nessa aposta")
    elif resultado == "Perdeu":
        print("Pedro, infelizmente você está no fundo do poço, se endividou completamente e não temos o que fazer…")
        print(f"Você poderia ter ganhado R${valor}, mas perdeu R${aposta}")