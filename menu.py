import calculadora

def menu():
    num = int(input('Selecione a opção desejada (1. SOMAR / 2. SUBTRAIR / 3. MULTIPLICAR / 4. DIVIDIR / 0. SAIR.): '))
    if num == 0:
        print("Saindo...")
        return
    a = float(input('Qual é o primeiro número desejado? '))
    b = float(input('Qual é o segundo número desejado? '))
    if num == 1:
        return calculadora.somar(a,b)
    if num == 2:
        return calculadora.subtrair(a,b)
    if num == 3:
        return calculadora.multiplicar(a,b)
    if num == 4:
        return calculadora.dividir(a,b)