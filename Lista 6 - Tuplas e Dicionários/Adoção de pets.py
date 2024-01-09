animals = input()

animals_list = animals.split(" e ")

animais_catalogo = ("gato", "cachorro", "peixe", "hamster")

needs = {'gato': ['bola de lã', 'caixa de areia', 'ração', 'ratinho de brinquedo'],
  'cachorro': ['coleira', 'ração', 'ursinho de pelúcia'],
  'peixe': ['aquário', 'filtro', 'ração'],
  'hamster': ['ração', 'roda para hamster', 'serragem']
}

enemies = {'gato': ['cachorro', 'peixe', 'hamster'],
  'cachorro': ['gato'],
  'hamster': ['gato', 'cachorro'],
  'peixe': ['gato']
}

puppies = input()
valid_puppies = False
if puppies == "sim":
  valid_puppies = True

###main###
exist = True

for i in animals_list:
  if i not in animais_catalogo:
    exist = False
    print(f'Sérgio, o animal {i} não estava nas suas potenciais escolhas, logo ele não pode ser analisado.')

if exist:
  if valid_puppies:
    print("Como os animais são recém nascidos, eles podem ser adotados juntos!")
    print("Segue aqui as necessidades dos animais:")
    for i in animals_list:
      print(f'As necessidades do(a) {i} são:')
      for j in needs[f'{i}']:
        print(f'- {j};')
    print('Dito isso, vamos adotá-los!!!')
  else:
    not_enemies = True
    for animal in animals_list:
      aux = animals_list.copy()
      aux.remove(animal)
      for i in aux:
        if i in enemies[f'{animal}']:
          not_enemies = False
          print(f'Sérgio, o(a) {animal} tem o(a) {i} como inimigo. Não é possível adotá-los juntos, a não ser que sejam recém nascidos')
    if not_enemies:
      print('Segue aqui as necessidades dos animais:')
      for animal in animals_list:
        print(f'As necessidades do(a) {animal} são:')
        for i in needs[f'{animal}']:
          print(f'- {i};')
      print('Dito isso, vamos adotá-los!!!')