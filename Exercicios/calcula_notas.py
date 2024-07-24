"""
10. Considerando o sistema de notas da Universidade, construa um algoritmo que, dadas as notas
 de um aluno pelo usuário, calcule a média e imprima se o aluno foi aprovado ou
reprovado

Objetivo: calcular média e dizer se o aluno foi aprovado

Entrada: atividade1, atividade2, atividade3, mapa, prova

processamento: calcular a nota final: atv1 + atv2 + atv3 + mapa = 10 
                                        prova = 10
                                        media = bloco1 + prova / 2 > 6 (aprovado)

saida: dizer se foi aprovado ou reprovado
"""

atividade1 = float(input("Digite a nota atividade1: "))
atividade2 = float(input("Digite a nota atividade2: "))
atividade3 = float(input("Digite a nota atividade3: "))
mapa = float(input("Digite a nota mapa: "))
prova = float(input("Digite a nota prova: "))

bloco1 = atividade1 + atividade2 + atividade3 + mapa
media = (bloco1 + prova) / 2

if media >= 6:
    print("APROVADO! sua media foi: ", media)
else:
    print("Reprovado... Tente novamente. sua media foi: ", media)
