class NadadoresCrawl:
    def __init__(self, numNadador, tempo):
        self.numNadador = numNadador
        self.tempo = tempo

class NadadoresPeito:
    def __init__(self, numNadador, tempo):
        self.numNadador = numNadador
        self.tempo = tempo

class NadadoresCostas:
    def __init__(self, numNadador, tempo):
        self.numNadador = numNadador
        self.tempo = tempo

class NadadoresBorboleta:
    def __init__(self, numNadador, tempo):
        self.numNadador = numNadador
        self.tempo = tempo

listaCrawl = []
listaPeito = []
listaCostas = []
listaBorboleta = []

for x in range(40):
    numNadador = int(input("Inscrição do competidor: "))
    modalidade = int(input("Modalidade do nadador: "))
    tempo = float(input("Tempo na competição: "))

    if modalidade == 1:
        listaCrawl.append(NadadoresCrawl(numNadador, tempo))
    elif modalidade == 2:
        listaPeito.append(NadadoresPeito(numNadador, tempo))
    elif modalidade == 3:
        listaCostas.append(NadadoresCostas(numNadador, tempo))
    elif modalidade == 4:
        listaBorboleta.append(NadadoresBorboleta(numNadador, tempo))

listaCrawl.sort(key = lambda nadador: nadador.tempo)
listaPeito.sort(key = lambda nadador: nadador.tempo)
listaCostas.sort(key = lambda nadador: nadador.tempo)
listaBorboleta.sort(key = lambda nadador: nadador.tempo)

print("\nModalidade Crawl")
for x in range(len(listaCrawl)):
    crawl = listaCrawl[x]
    print(f"Competidor: {crawl.numNadador} ----- Tempo: {crawl.tempo}")

print("\nModalidade Peito")
for y in range(len(listaPeito)):
    peito = listaPeito[y]
    print(f"Competidor: {peito.numNadador} ----- Tempo: {peito.tempo}")

print("\nModalidade Costas")
for z in range(len(listaCostas)):
    costas = listaCostas[z]
    print(f"Competidor: {costas.numNadador} ----- Tempo: {costas.tempo}")

print("\nModalidade Borboleta")
for i in range(len(listaBorboleta)):
    borboleta = listaBorboleta[i]
    print(f"Competidor: {borboleta.numNadador} ----- Tempo: {borboleta.tempo}")

primeiroCrawl = listaCrawl[0]
primeiroPeito = listaPeito[0]
primeiroCostas = listaCostas[0]
primeiroBorboleta = listaBorboleta[0]
print(f"\nPrimeiro colocado - modalidade Crawl | Competidor: {primeiroCrawl.numNadador} ----- Tempo: {primeiroCrawl.tempo}\n")
print(f"Primeiro colocado - modalidade Peito | Competidor: {primeiroPeito.numNadador} ----- Tempo: {primeiroPeito.tempo}\n")
print(f"Primeiro colocado - modalidade Costas | Competidor: {primeiroCostas.numNadador} ----- Tempo: {primeiroCostas.tempo}\n")
print(f"Primeiro colocado - modalidade Borboleta | Competidor: {primeiroBorboleta.numNadador} ----- Tempo: {primeiroBorboleta.tempo}")