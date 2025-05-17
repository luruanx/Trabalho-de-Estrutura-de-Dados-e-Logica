# SISTEMA DE EMPLACAMENTO DE VEÍCULOS - BRASIL

# Classe Nodo
class Nodo:
    def __init__(self, sigla, nomeEstado):
        self.sigla = sigla
        self.nomeEstado = nomeEstado
        self.proximo = None

# Classe TabelaHash
class TabelaHash:
    def __init__(self):
        self.tabela = [None] * 10  # Tabela hash com 10 posições

    def funcao_hash(self, sigla):
        if sigla == "DF":
            return 7
        else:
            char1_ascii = ord(sigla[0])
            char2_ascii = ord(sigla[1])
            return (char1_ascii + char2_ascii) % 10

    def inserir_no_inicio(self, sigla, nomeEstado):
        indice = self.funcao_hash(sigla)
        novo_nodo = Nodo(sigla, nomeEstado)
        novo_nodo.proximo = self.tabela[indice]
        self.tabela[indice] = novo_nodo

    def imprimir_tabela_hash(self):
        for i in range(10):
            print(f"Posição {i}: ", end="")
            atual = self.tabela[i]
            while atual:
                print(f"{atual.sigla} ", end="")
                atual = atual.proximo
            print()

# Lista de estados brasileiros e o DF
estados = [
    ("AC", "Acre"), ("AL", "Alagoas"), ("AP", "Amapá"), ("AM", "Amazonas"),
    ("BA", "Bahia"), ("CE", "Ceará"), ("ES", "Espírito Santo"), ("GO", "Goiás"),
    ("MA", "Maranhão"), ("MT", "Mato Grosso"), ("MS", "Mato Grosso do Sul"),
    ("MG", "Minas Gerais"), ("PA", "Pará"), ("PB", "Paraíba"), ("PR", "Paraná"),
    ("PE", "Pernambuco"), ("PI", "Piauí"), ("RJ", "Rio de Janeiro"),
    ("RN", "Rio Grande do Norte"), ("RS", "Rio Grande do Sul"), ("RO", "Rondônia"),
    ("RR", "Roraima"), ("SC", "Santa Catarina"), ("SP", "São Paulo"),
    ("SE", "Sergipe"), ("TO", "Tocantins"), ("DF", "Distrito Federal")
]

# Estado fictício (Meu Nome)
estado_ficticio = ("LR", "Luan Richard")

# Criando a tabela hash
tabela_hash = TabelaHash()

# Saída da tabela hash
print("Tabela hash antes de inserir qualquer informação:")
tabela_hash.imprimir_tabela_hash()

# Inserindo estados e o DF
for sigla, nome in estados:
    tabela_hash.inserir_no_inicio(sigla, nome)

# Saída da tabela hash após com a inclusão
print("\nTabela hash após inserir os 26 estados e o Distrito Federal:")
tabela_hash.imprimir_tabela_hash()

# Inserindo o estado fictício
tabela_hash.inserir_no_inicio(estado_ficticio[0], estado_ficticio[1])

# Saída da tabela hash após inclusão do estado fictício
print("\nTabela hash após inserir os 26 estados, Distrito Federal e o estado fictício:")
tabela_hash.imprimir_tabela_hash()