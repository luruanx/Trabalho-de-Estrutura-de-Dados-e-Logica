#Função para escolher o serviço
def escolha_servico():
    while True:
        print("\nEntre com o tipo de serviço desejado")
        print("DIG - Digitalização")
        print("ICO - Impressão Colorida")
        print("IPB - Impressão Preto e Branco")
        print("FOT - Fotocópia")
        servico = input("Digite o código do serviço desejado: ").strip().lower()

        if servico == 'dig':
            return ('Digitalização', 1.10)
        elif servico == 'ico':
            return ('Impressão Colorida', 1.00)
        elif servico == 'ipb':
            return ('Impressão Preto e Branco', 0.40)
        elif servico == 'fot':
            return ('Fotocópia', 0.20)
        else:
            print("Opção de serviço inválida. Tente novamente.")

#Função para solicitar o número de páginas
def num_pagina():
    while True:
        try:
            paginas = int(input("\nDigite o número de páginas: "))
            if paginas >= 20000:
                print("Não aceitamos tantas páginas de uma vez.")
                print("Por favor, digite o número de páginas novamente.")
                continue
            elif paginas >= 2000:
                return (paginas, paginas * 0.75)  #25% de desconto
            elif paginas >= 200:
                return (paginas, paginas * 0.80)  #20% de desconto
            elif paginas >= 20:
                return (paginas, paginas * 0.85)  #15% de desconto
            else:
                return (paginas, paginas)  #Sem desconto
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")

#Função para escolher serviço extra
def servico_extra():
    while True:
        print("\nDeseja adicionar encadernação?")
        print("1 - Encadernação Simples (R$15.00)")
        print("2 - Encadernação Capa Dura (R$40.00)")
        print("0 - Não desejo mais nada")
        adicional = input("Digite a opção desejada: ").strip()

        if adicional == "1":
            return ('Encadernação Simples', 15.00)
        elif adicional == "2":
            return ('Encadernação Capa Dura', 40.00)
        elif adicional == "0":
            return ('Sem adicional', 0.00)
        else:
            print("Opção de adicional inválida. Tente novamente.")

#Código principal
print("Bem-vindo a Copiadora do Ruan Richard")

#Chamada das funções
nome_servico, valor_servico = escolha_servico()
qtd_paginas, qtd_com_desconto = num_pagina()
nome_extra, valor_extra = servico_extra()

#Cálculo total
subtotal = valor_servico * qtd_com_desconto
total = subtotal + valor_extra

#Exibe resultado
print(f"\nTotal: R${total:.2f}")
print("Serviços Relizados:")
print(f"{nome_servico}: R${valor_servico:.2f} * Páginas: {int(qtd_com_desconto)} + ({nome_extra}: R${valor_extra:.2f})")
