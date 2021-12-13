class Candidatos:
    def __init__(self, inscricao, nota):
        self.inscricao = inscricao
        self.nota = nota

listaCandidatos = []
for x in range(10):
    inscricao = int(input("Número da inscrição: "))
    nota = float(input("Nota: "))
    listaCandidatos.append(Candidatos(inscricao, nota))

listaCandidatos.sort(key = lambda candidato: candidato.nota, reverse = True) #,reverse=True -> Ordena de maneira decrescente

for y in range(len(listaCandidatos)):
    candidato = listaCandidatos[y]
    print(f"Número da inscrição: {candidato.inscricao} - Nota: {candidato.nota}")