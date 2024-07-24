"""
3) Faça um algoritmo para receber um número qualquer e informar na tela se é par ou ímpar.

Objetivo: identificar se um numero é par ou impar

Entrada: um numero

Processamento: encontrar o resto da div por 2

Saída: dizer se é par ou impar
"""

numero = int(input("Digite um número: "))

resto = numero % 2

if resto == 0:
    print("O número digitado é par!")
else:
    print("O número digitado é ímpar!")
    