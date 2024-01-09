class Sonic:
  def __init__(self):
    self.aneis = 0
    self.esmeraldas = 0
    self.escudo = False
    self.super_sonic = False
    self.morreu = False
  
  def coletar_aneis(self, qtd_aneis):
    self.aneis += qtd_aneis
    return self.aneis
  
  def escudo(self):
    self.escudo = True
  
  def dano(self):
    if self.aneis == 0 and self.escudo == False:
      self.morreu = True
    elif self.aneis != 0 and self.escudo == False:
      self.aneis = 0
    elif self.escudo == True:
      self.escudo = False
  
  def coletar_esmeraldas(self):
    if self.esmeraldas == 7:
      print('Sonic ja possui todas as esmeraldas!!!')
    else:
      self.esmeraldas += 1
      if sonic.esmeraldas < 7:
        valor = 7 - sonic.esmeraldas
        print(f'Sonic ainda precisa encontrar mais {valor} esmeraldas!!!')
      else:
        print('Sonic acabou de encontrar a esmeralda que faltava!!!')
  
sonic = Sonic()
while not sonic.morreu and not sonic.super_sonic:
  comando = input()
  
  if comando == "aneis":
    qtd_aneis = int(input())
    sonic.coletar_aneis(qtd_aneis)
    print(f'Sonic esta agora com {sonic.aneis} aneis! Gotta go fast!!!')
  
  elif comando == "escudo":
    if sonic.escudo == 'True':
      print('Sonic ja esta equipado com uma protecao extra!!!')
    else:
      sonic.escudo = True
      print("Sonic esta agora com uma camada a mais de protecao!!! Let's go!!!")
  
  elif comando == "dano":
    sonic.dano()
    print('Maldito robo do Eggman!!! Este sera seu fim, bigodudo!!!')
  
  elif comando == "esmeralda":
    sonic.coletar_esmeraldas()
  
  if sonic.esmeraldas == 7 and sonic.aneis >= 50:
    sonic.super_sonic = True

if sonic.super_sonic:
  print('Com o poder das esmeraldas do caos, Super Sonic conseguiu deter os planos malignos do Dr. Robotinik!!!')
if sonic.morreu == True:
  print('Infelizmente, nosso heroi nao conseguiu correr o bastante para derrotar seu nemesis...')