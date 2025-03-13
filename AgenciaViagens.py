
def relatorio(valor,pensao):
    print(f'Valor a Vista, Desconto de 12%\n {valor - (valor * 0.125)}')
    print(f'Até 12 Vezes, Valor sem Juros')
    print(f'De 13 até 24, Acrescimo de 0.3 ao mês \nEx: 15 Vezes\nValor a Ser Pago {15 * 0.3 * valor}')
    print(f'De 25 até 36, Acrescimo de 0.5 ao mês \nEx: 26 Vezes\nValor a Ser pago {26 * 0.5 * valor}')
    if pensao == 'Sim':
        print(f'Valor a Ser gasto com pensao {valor + 300}')


valor = float(input('Digite o Valor que deseja disponibilzar para a Viagem\n'))
pensao = input('Deseja adicionar Pensão ?\n (sim/não)\n')
relatorio(valor,pensao)
