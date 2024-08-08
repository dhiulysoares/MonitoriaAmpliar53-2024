"""
4. Em uma instituição de ensino, a aprovação de um aluno em uma disciplina ocorre
quando a média das notas é maior ou igual a 7. Para auxiliar o professor em suas
atividades, elabore um algoritmo para: ler a quantidade de provas da disciplina, o
código de aluno e as notas do aluno. Calcule a média final de cada aluno e informe
o número de alunos aprovados e reprovados. O algoritmo deve ser executado até
que seja informado um código de aluno igual a 0.

Objetivo: calcular media de varios alunos, para determinado numero de provas e exibir a quantidade de aprovados
e reprovados.
Entrada: quantidade de provas, codigo do aluno, nota do aluno
Processamento: calcular a media e verificar se cada aluno foi aprovado ou reprovado com base na media 7, pedir um novo aluno enquanto
o codigo do aluno nao for 0.
Saída: quantidade de aprovados e a quantidade de reprovados.
"""

qtd_provas = int(input("Digite a quantidade de provas da disciplina: "))
codigo_aluno = input("Digite o código do aluno. Digite 0 para parar:")

soma = 0
qtd_aprovados = 0
qtd_reprovados = 0

while codigo_aluno != "0":
    for cont in range(qtd_provas):
        nota = float(input("Digite a nota: "))
        soma = soma + nota
    media_aluno = soma / qtd_provas    
    if media_aluno >= 7:
        qtd_aprovados = qtd_aprovados + 1
    else:
        qtd_reprovados = qtd_reprovados + 1
    codigo_aluno = input("Digite o código do aluno. Digite 0 para parar:")

print("A quantidade de aprovados é de: ", qtd_aprovados)
print("A quantidade de reprovados é de: ", qtd_reprovados)

