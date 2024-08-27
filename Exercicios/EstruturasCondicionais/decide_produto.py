"""2. Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
sabendo que a decisão é sempre pelo mais barato. 

entrada: 3 preços
processamento: verificar qual é mais barato
saída: printar o mais barato"""

precos = []

for i in range(3):
    preco = float(input(f"Digite o preço do produto {i + 1}: R$ "))
    precos.append(preco)
 
indice_mais_barato = precos.index(min(precos))
 
print(f"O produto {indice_mais_barato + 1} é o mais barato e custa R$ {precos[indice_mais_barato]:.2f}.")



"""
Solução proposta em sala por Alex Gonçalves:
for i in range(3):
    preco = float(input(f"Digite o preço do produto {i + 1}: R$ "))
    precos.append(preco)
 
indice_mais_barato = precos.index(min(precos))
 
print(f"O produto {indice_mais_barato + 1} é o mais barato e custa R$ {precos[indice_mais_barato]:.2f}.")
"""