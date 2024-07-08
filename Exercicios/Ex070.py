'''Exercicio 70: O cardápio de uma lanchonete é o seguinte:

i .Especificação Código Preço

ii .Cachorro Quente 100 R$ 1,20

iii. Bauru Simples 101 R$ 1,30

iv. Bauru com ovo 102 R$ 1,50

v. Hambúrguer 103 R$ 1,20

vi. Cheeseburguer 104 R$ 1,30

vii. Refrigerante 105 R$ 1,00

Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado.
'''

valor_total = valor_item = codigo = quantidade =  0

perg = input('Deseja fazer um pedido? [S/N]')
while (perg != 'n' and perg != 'N') :
  codigo = int(input('Digite o código do pedido: '))
  if codigo >= 100 and codigo <= 105:
    quantidade = int(input('Digite a quantidade: '))
    if codigo == 100 or codigo == 103:
      preco = 1.20
    elif codigo == 101 or codigo == 104:
      preco = 1.30
    elif codigo == 102:
      preco = 1.50
    else:
      preco = 1.00

    valor_item = preco * quantidade
    valor_total += valor_item
    print('Codigo: {}, Quantidade: {}, Valor do Item: {}' .format(codigo, quantidade, valor_item))
    print('Valor total: ', valor_total)
    print()
    perg = input('Deseja fazer outro pedido? [S/N]')
  else:
    print('Código inválido.')

print()
print('Valor da fatura: R$', valor_total)