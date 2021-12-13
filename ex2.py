lista = []
for x in range(10):
    valor = float(input(f"Valor {x+1}: "))
    lista.append(valor)

lista.sort(reverse=True)
print(lista)