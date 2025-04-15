pin = 123
tentativas = 0
msg = "senha bloqueada"
while tentativas < 3:
    senha = int(input("digite sua senha: "))
    if senha == pin:
        msg ="senha correta"
        break
    tentativas += 1
print(msg)
