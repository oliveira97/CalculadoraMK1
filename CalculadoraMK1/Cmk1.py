# Calculadora simples com python, versão: MK 1.0.0 !!!
print('-=-'*20)
print('Seja bem vindo(a) ao meu projeto de calculadora simples :)')
print('-=-'*20)
nome = input('Qual é seu nome? ')
print('Seja bem vindo(a) a minha calculadora {} :)'.format(nome))

escolha = input('Digite: \n "1" para adição, \n "2" multiplicação, \n "3" subtração,'
    ' \n "4" divisão ou \n "5" sair do programa: \n')
if escolha == '1':
    a1 = float(input('Digite o primeiro número da adição: '))
    a2 = float(input('Digite o segundo numero por favor: '))
    s = a1 + a2
    print('A soma entre {:.2f} e {:.2f} é igual a {:.2f}'.format(a1, a2, s))
if escolha == '2':
    m1 = float(input('Digite o primeiro número da multiplicação: '))
    m2 = float(input('Agora o segundo número por favor: '))
    mp = m1 * m2
    print('A multiplicação entre {:.2f} e {:.2f} é igual a {:.2f}'.format(m1, m2, mp))
if escolha == '3':
    s1 = float(input('Digite primeiro o maior número da subtração: '))
    s2 = float(input('Agora o menor número por favor: '))
    su = s1 - s2
    print('A subtração de {:.2f} e {:.2f} tem o resultado de {:.2f}'.format(s1, s2, su))
if escolha == '4':
    d1 = float(input('digite o valor do dividendo: '))
    d2 = float(input('Agora o divisor: '))
    dv = d1 / d2
    print('O valor da divisão de {} pelo {} será de {}'.format(d1, d2, dv))
if escolha >= '5' :
    print('Você esta saindo do programa, até a proxima!')
print('Muito obrigado por usar a minha calculadora \U0001f60d !!! ')
