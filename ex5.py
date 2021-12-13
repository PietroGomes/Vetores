class Aluno:
    def __init__(self, matricula, primeiraNota, segundaNota, media, situacao):
        self.matricula = matricula
        self.primeiraNota = primeiraNota
        self.segundaNota = segundaNota
        self.media = media
        self.situacao = situacao

listaAlunos = []
situacao = ""
aprovados = 0
reprovados = 0
notaTotal = 0

for x in range(10):
    matricula = int(input("Matrícula: "))
    primeiraNota = float(input("Primeira nota: ").replace(",", "."))
    segundaNota = float(input("Segunda nota: ").replace(",", "."))
    media = (primeiraNota + segundaNota)/2
    notaTotal += media
    if media >= 7:
        situacao = "Aprovado"
        aprovados += 1
    else:
        situacao = "Reprovado"
        reprovados += 1
    
    listaAlunos.append(Aluno(matricula, primeiraNota, segundaNota, media, situacao))

listaAlunos.sort(key = lambda aluno: aluno.media, reverse = True)

print()
for y in range(len(listaAlunos)):
    aluno = listaAlunos[y]
    print(f"Aluno: {aluno.matricula} ----- 1º Prova: {aluno.primeiraNota} ----- 2ª Prova: {aluno.segundaNota} ----- Média: {aluno.media} ----- Situação: {aluno.situacao}")

print(f"\nMédia da classe: {notaTotal/10 :.2f}")
print(f"Quantidade de aprovados: {aprovados}")
print(f"Quantidade de reprovados: {reprovados}")
