print("Bem-vindo à Loja do Ruan Richard")

#Valor do Produto
valor_unitario = float(input("Qual o valor do produto? R$ "))

#Quantidade do Produto
quantidade = int(input("Qual a quantidade do produto? "))

#Cálculo do valor total sem desconto
valor_total = valor_unitario * quantidade

#Verifica valor e define desconto
if valor_total < 2500:
    desconto = 0
    percentual = 0
elif valor_total >= 2500 and valor_total < 6000:
    desconto = valor_total * 0.04
    percentual = 4
elif valor_total >= 6000 and valor_total < 10000:
    desconto = valor_total * 0.07
    percentual = 7
else:
    desconto = valor_total * 0.11
    percentual = 11

#Cálculo do valor com desconto
valor_com_desconto = valor_total - desconto

#Saída dos resultados
print(f"\nValor total sem desconto: R$ {valor_total:,.2f}")
print(f"Desconto de {percentual}% aplicado: R$ {desconto:,.2f}")
print(f"Valor total com desconto: R$ {valor_com_desconto:,.2f}")
