listaNumeros =  []
listaPositivo = []
listaNegativo = []

for x in range(8):
    numero = int(input("Digite um número: "))
    listaNumeros.append(numero)

for x in range(8):
    if listaNumeros[x] > 0:
        listaPositivo.append(listaNumeros[x])
    else:
        listaNegativo.append(listaNumeros[x])

listaPositivo.sort()
listaNegativo.sort()

print("\nNúmeros positivos: ", end = "")
for num in listaPositivo:
    print(num, end = " ")

print()
print("Números negativos: ", end = "")
for num in listaNegativo:
    print(num, end = " ")
