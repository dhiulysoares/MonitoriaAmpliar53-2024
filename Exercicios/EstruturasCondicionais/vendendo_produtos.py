"""
Um vendedor precisa de um algoritmo que calcule o preço total devido por um cliente. 
O algoritmo deve receber o código de um produto e a quantidade comprada e calcular o preço total, 
usando a tabela abaixo. Mostre uma mensagem no caso de código inválido.

Código 	Preço unitário
'ABCD' 	R$ 5,30
'XYPK' 	R$ 6,00
'KLMP' 	R$ 3,20
'QRST' 	R$ 2,50

objetivo: calcular preços dos produtos
entrada: codigo do produto, quantidade
processamento: calcular o preço total em cada caso
saída: retornar o preço devido
"""

codigo_produto = input("Digite o código do produto: \n"
                       "[ABCD] R$ 5,30\n"
                       "[XYPK] R$ 6,00\n"
                       "[KLMP] R$ 3,20\n"
                       "[QRST] R$ 2,50\n")

quantidade = int(input("Digite a quantidade: "))

match codigo_produto:
    case "ABCD":
        preco = quantidade * 5.3
        print("Valor devido: ", preco)
    case "XYPK":
        preco = quantidade * 6.0
        print("Valor devido: ", preco)
    case "KLMP":
        preco = quantidade * 3.2
        print("Valor devido: ", preco)
    case "QRST":
        preco = quantidade * 2.5
        print("Valor devido: ", preco)
    case _:
        print("invalido")