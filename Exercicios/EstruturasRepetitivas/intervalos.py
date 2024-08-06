"""Objetivo: receber 10 numeros e identificar quantos estão entre [10,20] e quantos estão fora.
Entrada: 10 numeros
Processamento: contar quantos estão dentro do intervalo e contar quantos estão fora do intervalo
Saída: exibir o resultado da contagem"""

dentroIntervalo = 0
foraIntervalo = 0

for cont in range(10):
    numero = int(input("Digite um numero"))
    if numero > 10 and numero < 20:
        dentroIntervalo = dentroIntervalo + 1
    else:
        foraIntervalo = foraIntervalo + 1

print("Quantidade de numeros dentro do intervalo [10, 20]: ", dentroIntervalo)
print("Quantidade de numeros fora do intervalo [10, 20]: ", foraIntervalo)
