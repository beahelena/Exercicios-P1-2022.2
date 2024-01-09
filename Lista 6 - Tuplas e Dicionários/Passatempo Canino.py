def vaquinha(energia_atual, adicional, energia_gasta, energia_inicial):
    energia_antes = energia_atual
    energia_atual = max(0, energia_atual - int(adicional))
    energia_gasta += min(energia_antes - energia_atual, 100)
    print("Brinquedo da vaquinha! Vou chacoalhar")
    return energia_atual, energia_gasta

def chupeta(energia_atual, adicional, energia_gasta, energia_inicial):
    energia = energia_atual - 5
    energia_antes = energia_atual
    energia_atual =  max(0, energia, min(int(adicional), energia_atual))
    energia_gasta += energia_antes - energia_atual
    print("Minha pipeta! Vou morder")
    return energia_atual, energia_gasta

def ze_gotinha(energia_atual, adicional, energia_gasta, energia_inicial):
    energia_antes = energia_atual
    energia_atual = max(0, energia_atual // max(int(adicional), 1))
    energia_gasta += energia_antes - energia_atual
    print("Meu preferido! Faz barulho e mordo")
    return energia_atual, energia_gasta

def bolinha(energia_atual, adicional, energia_gasta, energia_inicial):
    energia_antes = energia_atual
    energia_atual = max(0, energia_atual - int(adicional) // 4)
    energia_gasta += energia_antes - energia_atual
    print("ZOOOOOOOOOOOOOOOOOM")
    return energia_atual, energia_gasta

def osso(energia_atual, adicional, energia_gasta, energia_inicial):
    energia_atual = min(energia_atual + int(adicional) * 2, energia_inicial)
    energia_gasta = energia_gasta
    print("Pausa para roer")
    return energia_atual, energia_gasta

def comida(energia_atual, adicional, energia_gasta, energia_inicial):
    letras = len(adicional)
    energia_antes = energia_atual
    sinal = 1 - 2 * (letras % 2)
    energia_atual = max(0, min(energia_atual + sinal * letras, energia_inicial))
    energia_gasta += max(energia_antes - energia_atual, 0)
    print(f"Uhh, {adicional} deve ser comestível")
    return energia_atual, energia_gasta

opcoes = {
    "Vaquinha": vaquinha,
    "Chupeta": chupeta,
    "Zé Gotinha": ze_gotinha,
    "Bolinha": bolinha,
    "Osso": osso,
    "Comida": comida,
}

energia_inicial = int(input())
energia_atual = energia_inicial
energia_gasta = 0

while energia_atual > 0 and energia_gasta < 100:
  entrada = input().split(": ")
  objeto, adicional = entrada[0], entrada[1]
  energia_atual, energia_gasta = opcoes[objeto](energia_atual, adicional, energia_gasta, energia_inicial)

n = min(10, max(energia_gasta, 10)//10)
qtd = 'a' * n

energia_gasta = min(energia_gasta, 100)
print(f"Mamãe chegou! Gastei {energia_gasta} pontos da minha energia e estou c{qtd}nsada, mas vou correr para seus braços!")
