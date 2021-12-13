lista = []
indices = []

for a in range(40):
    num = int(input("Insira um número inteiro: "))
    lista.append(num)

for x in range(10):
    if lista[x] < 0:
        indices.append(lista[x])

for y in indices:
    lista.remove(y)

print(lista)