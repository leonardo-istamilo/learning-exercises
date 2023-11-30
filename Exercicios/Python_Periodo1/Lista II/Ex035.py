""" Exercicio 35 - Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;

Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário; """


a = float(input('Digite o valor de a:'))
if a != 0:
    b = float(input('Digite o valor de b:'))
    c = float(input('Digite o valor de c:'))
    
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = ((-b + delta**(1/2))/2*a)
        x2 = ((-b - delta**(1/2))/2*a)

        if delta == 0:
            print('A equação possui duas raizes reais e iguais (x1 = x2): ', x1)

        elif delta > 0:
            print("A equação possui duas raizes reais e distintas x1 = {} e x2 = {}".format(x1, x2))
    else:
        print('A equação não possui raizes reais.')
else:
    print('Não é do segundo grau.')
