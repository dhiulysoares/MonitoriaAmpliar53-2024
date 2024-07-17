"""
Escreva um algoritmo que leia o valor da hora-aula, o número de horas-aula dadas no mês, 
e o percentual de desconto do INSS de um professor. 
Calcule e, depois, apresente o salário líquido e o salário bruto.

Objetivo: calcular o salario bruto e liquido de um professor
Entrada: valor da hora-aula, numero de aulas dadas, percentual de desconto INSS
Processamento: calculo do salario 
Saída: salario bruto e salario liquido
"""

#CalculaSalario

valorAula = float(input("Digite o valorAula"))
percentualInss = float(input("Digite o percentualInss"))
numeroAulas = int(input("Digite o numero de aulas"))

salarioBruto = numeroAulas * valorAula
salarioLiquido = salarioBruto - (percentualInss/100 * salarioBruto)

print(salarioBruto, salarioLiquido)