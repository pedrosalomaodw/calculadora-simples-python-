import colorama as cl 

cl.init()

print('-'*30)
print('CALCULADORA SIMPLES')
print('-'*30)

op = ''
resultado = 0
nu = 0
n2 = 0

while True:

    nu = int(input('escolha um número: '))
    n2 = int(input('escolha outro número: '))
    op = (input)('escolha um operador: ')


    if op == '+':
            resultado = nu + n2
    elif op == '-':
            resultado = nu - n2
    elif op == '*':
            resultado = nu * n2
    elif op == '/':
            resultado = nu / n2
    else:
        print(cl.Fore.RED + 'ERRO NO CÁLCULO!!')
    
    print(str(nu) + '' + str(op) + '' + str(n2) + '=' + str(resultado))

print(cl.Style.RESET_ALL) 

  

