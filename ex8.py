listaLogica = []
listaProg = []
listaIntersecao = []

for x in range(15):
    logica = int(input("Digite a matrícula para a disciplina de Lógica: "))
    listaLogica.append(logica)

for x in range(20):
    programacao = int(input("Digite a matrícula para a disciplina de Linguagem de Programação: "))
    listaProg.append(programacao)


for x in range(15):
    for y in range(20):
        if listaLogica[x] == listaProg[y]:
            listaIntersecao.append(listaLogica[x])

listaIntersecao.sort()

print()
if listaIntersecao == []:
    print("Não há alunos matriculados nas duas disciplinas")
else:
    for i in listaIntersecao:
        print(f"{i}", end = " ")
