listaCodigos = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
listaPrecos = [10000, 9000, 850, 200, 100, 5000, 4000, 900, 870, 1000]

for x in range(10):
    for y in range(10):
        if listaPrecos[y] > listaPrecos[x]:
            auxPrecos = listaPrecos[x]
            listaPrecos[x] = listaPrecos[y]
            listaPrecos[y] = auxPrecos

            auxCodigos = listaCodigos[x]
            listaCodigos[x] = listaCodigos[y]
            listaCodigos[y] = auxCodigos

for i in range(10):
    if (listaCodigos[i] % 2 == 0) and (listaPrecos[i] > 1000):
        print(f"Código: {listaCodigos[i]} --- Preço: {listaPrecos[i]:.2f} --- Novo preço: {(listaPrecos[i]*1.2):.2f}")

    elif listaCodigos[i] % 2 == 0:
        print(f"Código: {listaCodigos[i]} --- Preço: {listaPrecos[i]:.2f} --- Novo preço: {(listaPrecos[i]*1.15):.2f}")
    
    elif listaPrecos[i] > 1000:
        print(f"Código: {listaCodigos[i]} --- Preço: {listaPrecos[i]:.2f} --- Novo preço: {(listaPrecos[i]*1.1):.2f}")
    
    else:
        print(f"Código: {listaCodigos[i]} --- Preço: {listaPrecos[i]:.2f} --- Novo preço: XXXX.XX")