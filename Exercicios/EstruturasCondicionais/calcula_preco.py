"""
11) Elabore um algoritmo que calcule o que deve ser pago por um produto, considerando o preço
normal deetiqueta e a escolha da condição de pagamento. Utilize os códigos da tabela a seguir
para ler qual acondição de pagamento escolhida e efetuar o cálculo adequado.
Código Condição de pagamento
1 À vista em dinheiro ou cheque, recebe 10% de desconto
2 À vista no cartão de crédito, recebe 15% de desconto
3 Em duas vezes, preço normal de etiqueta sem juros
4 Em duas vezes, preço normal de etiqueta mais juros de 10%

Objetivo: montar uma estrutura que calcule o preço do produto de acordo com o código informado
Entrada: codigo da operação, preço de etiqueta
processamento: de acordo com o código, calcular o desconto ou o juros
saída: valor final
"""

preco_produto = float(input("Digite o preço do produto: "))
codigo_operacao = int(input("Digite a opção desejada: \n"
                            "[1] À vista em dinheiro ou cheque, recebe 10% de desconto\n" 
                            "[2] À vista no cartão de crédito, recebe 15% de desconto\n"
                            "[3] Em duas vezes no boleto, preço normal de etiqueta sem juros\n"
                            "[4] Em duas vezes no cartão, preço normal de etiqueta mais juros de 10%: "))

match codigo_operacao:
    case 1:
        print("O preço a pagar será: ", preco_produto - 0.1*preco_produto)
    case 2:
        print("O preço a pagar será: ", preco_produto - 0.15*preco_produto)
    case 3:
        print("O preço a pagar será: ", preco_produto)
    case 4:
        print("O preço a pagar será: ", preco_produto + 0.1*preco_produto)
