class Aluno:
    def __init__(self, matricula, idade):
        self.matricula = matricula
        self.idade = idade

listaAluno = []
for x in range(15):
    matricula = int(input("Número da matrícula: "))
    idade = int(input("Idade: "))
    listaAluno.append(Aluno(matricula, idade))

listaAluno.sort(key = lambda aluno: aluno.idade) #,reverse=True -> Ordena de maneira decrescente

for x in range(len(listaAluno)):
    aluno = listaAluno[x]
    print(f"Matrícula: {aluno.matricula} - Idade: {aluno.idade}")
