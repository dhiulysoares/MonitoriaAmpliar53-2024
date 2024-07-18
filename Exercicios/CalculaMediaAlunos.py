"""
Faça um algoritmo que leia as 3 notas de um aluno e calcule a média final deste aluno. 
Considerar que a média é ponderada e que o peso das notas é: 2,3 e 5, respectivamente. 

Objetivo: calcular média ponderada de alunos
Entrada: tres notas
processamento: n1*2 + n2*3 + n3*5 / 10
saida: media final
"""

nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))
peso1 = 2
peso2 = 3
peso3 = 5

mediaFinal = ((nota1*peso1) + (nota2*peso2) + (nota3*peso3)) / (peso1+peso2+peso3)

print("A média final do aluno é: ", mediaFinal)
