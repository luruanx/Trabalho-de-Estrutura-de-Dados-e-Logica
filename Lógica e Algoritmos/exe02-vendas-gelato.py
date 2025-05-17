print("Bem-vindo à Loja de Gelados do Ruan Richard")

print("--------------------------------Cardápio-------------------------------------")
print("-----------------------------------------------------------------------------")
print("----|     Tamanho     |       Cupuaçu (CP)      |       Açaí  (AC)      |----")
print("----|        P        |        R$ 9.00          |       R$ 11.00        |----")
print("----|        M        |        R$ 14.00         |       R$ 16.00        |----")
print("----|        G        |        R$ 18.00         |       R$ 20.00        |----")
print("-----------------------------------------------------------------------------")

#Carrinho
total = 0

#Loop principal
while True:
    #Solicita o sabor
    sabor = input("\nDigite o sabor desejado (CP para Cupuaçu ou AC para Açaí): ").upper()

    #Verifica se o sabor é válido
    if sabor != "CP" and sabor != "AC":
        print("Sabor inválido. Tente novamente")
        continue  #Volta ao início do loop

    #Solicita o tamanho
    tamanho = input("Digite o tamanho desejado (P/M/G): ").upper()

    #Verifica se o tamanho é válido
    if tamanho != "P" and tamanho != "M" and tamanho != "G":
        print("Tamanho inválido. Tente novamente")
        continue  #Volta ao início do loop

    #Verifica os preços
    preco = 0
    if sabor == "CP":
        if tamanho == "P":
            preco = 9.00
        elif tamanho == "M":
            preco = 14.00
        else:
            preco = 18.00
    elif sabor == "AC":
        if tamanho == "P":
            preco = 11.00
        elif tamanho == "M":
            preco = 16.00
        else:
            preco = 20.00

    #Exibe o valor do pedido
    print(f"Você pediu um {sabor} de tamanho {tamanho}: R$ {preco:.2f}")

    #Valor do pedido
    total += preco

    #Pergunta se deseja algo mais
    print()
    mais = input("Deseja pedir mais alguma coisa? (S/N): ").upper()
    if mais == "S":
        continue  #Volta ao início do loop para novo pedido
    else:
        break  #Encerra

#Exibe o total do pedido
print(f"\nO total a ser pago é: R$ {total:.2f}")
