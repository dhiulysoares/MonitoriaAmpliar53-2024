"""
4. Crie um algoritmo que, dado o nível de alerta de risco, imprima se ele for GRAVE. O
nível de alerta é um número que varia de 0 a 10. O nível é considerado GRAVE quando
ele é superior a 9.

Objetivo: tendo o nivel de alerta, dizer o que ele significa

Entrada: nivel de alerta

Processamento: comparar se é maior que 9

Saída: escrever se é GRAVE.
"""

nivel_de_alerta = int(input("Digite o nível de alerta: "))

if nivel_de_alerta < 0 or nivel_de_alerta > 10:
    print("Valor incorreto.")
    exit()

if nivel_de_alerta > 9:
    print("GRAVE!")
else:
    print("Seguro.")


print("GRAVE!") if nivel_de_alerta > 9 else print("Seguro.") #operador ternario