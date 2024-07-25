
"""
somar dois numeros e retornar se a soma é maior que zero, igual a zero, ou menor que zero.

Objetivo: realizar a soma e comparar com zero
entrada: dois numeros
processamento: realizar a soma e comparar com zero
saída: exibir o resultado
"""

numero1, numero2 = input("Digite dois numeros: ").split()

soma = int(numero1) + int(numero2)

if soma > 0:
    print("Maior que zero")
elif soma == 0:
    print("Igual a zero")
else:
    print("Menor que zero")

"1689" "16" "-9"