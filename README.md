# 💡 Trabalho de Lógica de Programação - Ciência da Computação

Este repositório contém os quatro exercícios desenvolvidos para o trabalho de **Lógica de Programação** do curso de **Ciência da Computação**. Cada exercício representa a aplicação de conceitos fundamentais de lógica e controle de fluxo com Python, simulando sistemas do mundo real.

---

## 🛒 Exercício 1 - Sistema de Vendas

Simula uma loja simples, onde o usuário informa o valor unitário e a quantidade de um produto. O sistema então:

- Calcula o valor total da compra.
- Aplica descontos com base no valor total:
  - Sem desconto: abaixo de R$2.500
  - 4% de desconto: entre R$2.500 e R$6.000
  - 7% de desconto: entre R$6.000 e R$10.000
  - 11% de desconto: acima de R$10.000
- Exibe o valor total com e sem desconto.

✅ **Tópicos abordados**: entrada de dados, estruturas condicionais, operações matemáticas.

---

## 🍨 Exercício 2 - Loja de Gelatos

Um sistema interativo de pedidos de gelados (Cupuaçu ou Açaí) com três tamanhos disponíveis:

| Sabor   | Pequeno (P) | Médio (M) | Grande (G) |
|---------|-------------|-----------|------------|
| CP (Cupuaçu) | R$ 9.00 | R$ 14.00 | R$ 18.00 |
| AC (Açaí)    | R$ 11.00 | R$ 16.00 | R$ 20.00 |

- Permite múltiplos pedidos em sequência.
- Calcula e exibe o valor total a pagar.

✅ **Tópicos abordados**: loops, condicionais aninhadas, validação de entrada, somatório.

---

## 🖨️ Exercício 3 - Sistema de Copiadora

Sistema que simula serviços de uma copiadora, com três etapas:

1. **Escolha do serviço**: Digitalização, Impressão Colorida, PB ou Fotocópia.
2. **Número de páginas**: aplica desconto progressivo dependendo da quantidade.
3. **Serviço adicional**: opção de encadernação (simples ou capa dura).

- Calcula o valor total com desconto e adicional.
- Exibe um resumo dos serviços realizados.

✅ **Tópicos abordados**: funções, múltiplos retornos, validação, lógica de negócios.

---

## 📚 Exercício 4 - Sistema de Livraria

CRUD básico de uma livraria, com as seguintes funcionalidades:

- 📖 **Cadastrar livro** (com ID automático, nome, autor e editora)
- 🔍 **Consultar livros**:
  - Todos os livros
  - Por ID
  - Por Autor
- 🗑️ **Remover livro** por ID
- ❌ **Encerrar o sistema**

✅ **Tópicos abordados**: listas de dicionários, laços, funções, menu interativo, tratamento de exceções.

---

## 🚀 Como executar

Certifique-se de ter o **Python 3** instalado. Em seguida, execute cada exercício separadamente via terminal:

```bash
python exe01-sistema-vendas.py
python exe02-vendas-gelato.py
python exe03-sistema-copiadora.py
python exe03-sistema-livraria.py
