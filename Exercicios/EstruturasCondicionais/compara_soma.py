"""
1) Faça um algoritmo que leia os valores A, B, C e imprima na tela se a soma de A + B é menor
que C.

Objetivo: ler três valores e imprimir se a soma dos dois primeiros é menor que o terceiro

Entrada: os três valores

Processamento: soma de A e B, comparar soma com C 

Saída: resposta da comparação (se a soma é maior ou menor que C)
"""

A = float(input("Digite o primeiro número: "))
B = float(input("Digite o segundo número: "))
C = float(input("Digite o terceiro número: "))

soma = A + B 

if soma < C:
    print("A soma de A e B é menor que C")


