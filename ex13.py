lista1 = []
lista2 = []
intersecao = []


for a in range(10):
    valor1 = int(input("Vetor 1: "))
    lista1.append(valor1)
uniao = lista1

print()
for b in range(10):
    valor2 = int(input("Vetor 2: "))
    lista2.append(valor2)

for i in range(len(lista2)):
    uniao.append(lista2[i])

for x in range(10):
    for y in range(10):
        if lista1[x] == lista2[y]:
            intersecao.append(lista1[x])

print(f"Vetor da união das listas: {uniao}")
print(f"Vetor da intersecção das listas: {intersecao}")
