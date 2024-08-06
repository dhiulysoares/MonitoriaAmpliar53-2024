"""
Objetivo: calcular media de x numeros. E o usuario decide quando finaliza a execução digitando um valor negativo.
Entrada: varios numeros positivos
Processamento: somar esses numeros e dividir pela quantidade deles.
Saída: escrever a média dos numeros
"""

numero = int(input("Digite um numero positivo. Digite um numero negativo caso queira parar:"))
cont = 0
soma = 0

while numero >= 0:
    cont = cont + 1
    soma = soma + numero
    numero = int(input("Digite um numero positivo. Digite um numero negativo caso queira parar:"))

media = soma / cont
print("A media é", media)
