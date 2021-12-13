listaQuantidade = []
listaCliente___ = []

for x in range(50):
    codigoCliente = int(input("Código do cliente: "))
    quantFilmes = int(input("Quantidade de filmes retirados: "))

    listaQuantidade.append(quantFilmes)
    listaCliente___.append(codigoCliente)

    
for i in range(50):
    for j in range(50):
        if listaQuantidade[j]>listaQuantidade[i]:
            aux = listaQuantidade[i]
            listaQuantidade[i] = listaQuantidade[j]
            listaQuantidade[j] = aux

            auxCliente = listaCliente___[i]
            listaCliente___[i] = listaCliente___[j]
            listaCliente___[j] = auxCliente

print()
for x in range(49, 39, -1):
    print(f"Cliente : {listaCliente___[x]} ----- Quantidade de filmes: {listaQuantidade[x]}")