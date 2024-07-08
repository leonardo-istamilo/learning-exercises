'''
Exercicio 35 - Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;

Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
'''

a = float(input('Digite o valor de a:'))
if a != 0:
    b = float(input('Digite o valor de b:'))
    c = float(input('Digite o valor de c:'))
    delta = b**2 - 4*a*c
    x1 = (-b + pow(delta, 1/2))/2*a
    x2 = (-b - (delta**(1/2)))/2*a
    print()
    if delta < 0:
        print('A equação não possui raizes reais.')
    elif delta == 0:
        print('A equação possui apenas uma raiz real.')
        print('x1 = x2 = ', x1)
    else:
        print('A equação possui duas raizes reais e distintas:')
        print('x1 = {}, x2 = {}' .format(x1, x2))
else:
    print('Não é do segundo grau.')
