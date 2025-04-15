resp = "s"
while resp == "s":
    a1 = float(input("Digite sua primeira nota: "))
while a1 >10 or a1 < 0:
    a1 = float(input("Digite sua primeira nota: "))

    a2 = float(input("Digite sua segunda nota: "))
    while a2 >10 or a2 < 0:
        a2 = float(input("Digite sua segunda nota: "))
    media = (a1+a2)/2
    print(media)
    resp=input("Deseja fazer o cálculo novamente? (s/n)")

