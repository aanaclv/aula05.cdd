# ler 2 valores
valor1 = int(input("Insira um valor: "))
valor2 = int(input("Insira o segundo valor: "))
# enquanto o valor2 seja 0: digite novamente
while valor2 == 0:
    valor2 = int(input("Digite novamente"))
    
divisao = valor1/valor2
print(divisao)

