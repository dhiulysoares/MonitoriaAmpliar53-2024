"""
Receber a idade do usuário e a informação se ele tem cartão. Caso ele seja maior de idade e tenha cartão, 
poderá realizar a compra, caso contrário não. E vamos exibir essa mensagem na tela.


Objetivo: validar a idade e se o usuario possui cartão
Entrada: idade, possui cartão?
Processamento: verificar se é maior de idade e a resposta obtida sobre ter cartão
Saída: Mensagem permitindo a compra ou rejeitando
"""

idade = int(input("Digite a sua idade: "))
if idade < 0:
    idade = int(input("Idade inválida. Digite novamente"))
    if idade < 0:
        exit()

possui_cartao = input("Digite S para sim e N para não: ")

if idade >= 18:
    if possui_cartao == "S":
        print("Você pode realizar a compra.")
    else:
        print("Você não pode realizar a compra sem o cartão.")
else:
    print("Você é menor de idade e não pode realizar a compra.")
