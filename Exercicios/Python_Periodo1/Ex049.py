#49 - Faça um programa para somar os números pares positivos < 1000 e ao final escrever o resultado.

soma = 0
for i in range(2, 1000, 2): #Zero é nulo, por isso, não entra.
    soma = soma + i

print(soma)