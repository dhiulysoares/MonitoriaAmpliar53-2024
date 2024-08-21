nome_aluno = []
soma = 0
nota = []
media = []


for cont in range(3):
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

for cont in range(3):
    print("A media do aluno" , nome_aluno[cont], "é ", media[cont])