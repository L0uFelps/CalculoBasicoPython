cont = int(0)
s = int(0)
while (cont <= 10):
    print("Digite o ", cont, "º valor : ")
    n = int(input())
    s = s + n
    cont = cont + 1

print("A soma de todos os valores é: {}".format(s))
