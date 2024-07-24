"""
Escreva um algoritmo que leia o valor da hora-aula, o número de horas-aula dadas no mês, 
e o percentual de desconto do INSS de um professor. 
Calcule e, depois, apresente o salário líquido e o salário bruto.

Objetivo: calcular o salario bruto e liquido de um professor
Entrada: valor da hora-aula, numero de aulas dadas, percentual de desconto INSS
Processamento: calculo do salario 
Saída: salario bruto e salario liquido
"""

valorAula = float(input("Digite o valor da aula"))
numeroAulas = int(input("Digite a quantidade de aulas dadas")) # 14 <> "14"
percentualInss = float(input("Digite o percentual de desconto do INSS"))

salarioBruto = valorAula * numeroAulas
salarioLiquido = salarioBruto - (percentualInss/100 * salarioBruto)

print("O salario bruto é:", salarioBruto)
print("O salario liquido é:", salarioLiquido)
