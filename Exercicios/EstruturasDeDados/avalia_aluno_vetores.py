# O professor precisa ler 4 notas de 10 alunos e no final receber uma lista com a média de todos cada um deles.

nome_aluno = []
media = []


for cont in range(10):
    nome = input("Digite o nome do aluno: ")
    nome_aluno.append(nome) ## nome_aluno[cont] = input("Digite o nome do aluno: ")
    soma = 0
    nota = []
    for cont in range(4):
        nota_prova = float(input("Digite a nota: "))
        nota.append(nota_prova)
        soma = soma + nota[cont]
    media_calculada = soma / 4
    media.append(media_calculada)

for cont in range(10):
    print("A media do aluno" , nome_aluno[cont], "é ", media[cont])


print(nome_aluno, "e", media) # [ana, carol, pedro, adao, jose] e [9, 7,5, 8, 6, 5]