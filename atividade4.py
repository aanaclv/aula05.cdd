alunos = int(input("Digite o número de alunos: "))
# inicia no aluno 1
n = 1
# var para guardar a qt de alunos
soma = 0
# enquanto n for menor que a qt de alunos do input repete a pergunta das notas
while n <= alunos:
    nota = float(input(f"Digite a {n} nota: "))
 #quebra o laço de repetição
    n += 1
#soma as notas e guarda na var
    soma += nota

media = soma/alunos
print(media)