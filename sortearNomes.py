import random
nome1 = input("Digite o nome de 4 alunos: ")
nome2= input()
nome3 = input()
nome4 = input()
nomes = [nome1, nome2, nome3, nome4]
print('O escolhido no sorteio foi: {}'.format(random.choice([nome1, nome2, nome3, nome4])))

print("E a ordem em que vão se apresentar será")
random.shuffle(nomes)
print(nomes)