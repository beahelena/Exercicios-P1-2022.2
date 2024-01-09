invencao = input("")

continua = True
custo_total = 0
total_falhas = 0
etapas_realizadas = 0

while continua:
  nome_etapa = input("")
  if nome_etapa == "concluir" or nome_etapa == "desistir":
    continua = False
    print(f"A jornada da construção do(a) {invencao} acaba aqui.")
    continue
  if nome_etapa == "dar um plus":
    custo_extra = int(input(""))
    custo_total += custo_extra
    print(f"Agora o(a) {invencao} ficou ainda mais legal! Pena que precisei gastar R${custo_extra}")
    continue
  custo_etapa = int(input(""))
  tentativas = int(input(""))
  while tentativas > 0:
    tentativas -= 1
    custo_total += custo_etapa
    status_etapa = input("")
    if status_etapa == "correto":
      etapas_realizadas += 1
      print(f"Oba! consegui {nome_etapa}, o que me custou R${custo_etapa}")
      break
    if status_etapa == "incorreto":
      total_falhas += 1
      print(f"Ainda não consegui {nome_etapa} corretamente, e essa tentativa me custou R${custo_etapa}")
  if tentativas == 0 or status_etapa == "correto":
    print(f"ANDAMENTO DO PROJETO: Etapas realizadas - {etapas_realizadas} ; Tentativas falhas - {total_falhas}")

else:
  if nome_etapa == "desistir":
    print(f"Infelizmente, o sonho do(a) {invencao} foi interrompido e levou junto com ele R${custo_total}")
  if nome_etapa == "concluir":
    print(f"Uhuuu, finalmente o(a) {invencao} tá pronto(a)! Esse projeto me custou R${custo_total}")