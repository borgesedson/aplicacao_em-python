lista_numeros = [2, 3, 4, 53, 78, 9, 56]
soma = 0

try:
    for i in lista_numeros:
        soma += i
    print(f'A soma dos elementos é: {soma}')
except Exception as e:
    print(f'Ocorreu um erro: {e}')
