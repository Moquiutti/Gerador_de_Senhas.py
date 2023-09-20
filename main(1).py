import random 

letra_maiuscula = chr(random.randint(65, 90))
letra_minuscula = chr(random.randint(97,122))
char_especial = chr(33)
list_num = []

for i in range(5): #até 8 digitos 
  numeros = random.randrange(9)
  list_num.append(numeros)

random.shuffle(list_num)
list_num = str(list_num) [1:-1]
list_num = list_num.replace(',', '')

print(letra_maiuscula, letra_minuscula, list_num, char_especial)
