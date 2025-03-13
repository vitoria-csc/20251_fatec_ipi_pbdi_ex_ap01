import calculadora

def menu():
    num = int(input('Selecione a opção desejada (1. SOMAR / 2. SUBTRAIR / 3. MULTIPLICAR / 4. DIVIDIR / 0. SAIR.): '))
    a = float(input('Qual é o primeiro número desejado? '))
    b = float(input('Qual é o segundo número desejado? '))
    if num == 1:
        return calculadora.somar(a,b)