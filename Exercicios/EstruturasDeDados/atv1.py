idade = []
altura = []

for cont in range(5):
    idade_digitada = input(f"Digite a idade do aluno {cont+1}: ")
    idade.append(idade_digitada)
    altura_digitada = float(input("Digite a altura do aluno, em metros: "))
    altura.append(round(altura_digitada,2))

for cont in range(5):
    print("O aluno ", cont+1, "tem ", idade[cont], "anos, e ", altura[-cont-1], "cm de altura.")

# lista[1]
# lista[-1], lista[-1-1] = lista[-2], lista[-2-1] = lista[-3]