lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

posicao = 0
for x in range(15, 7, -1):
    lista[x], lista[posicao] = lista[posicao], lista[x]
    posicao += 1

print(lista)