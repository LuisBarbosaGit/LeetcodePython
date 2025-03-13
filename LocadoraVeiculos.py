
def CalculaTotal(dias,distancia):
    if dias >= 3 and dias < 7:
        total = dias * 109.90
        print(f'Valor a ser gasto plano por dia {total}')
    elif dias >= 7 and dias < 15:
        total = dias * 99,90
        print(f'Valor a ser gasto plano por dia {total}')
    elif dias == 15:
        total = dias * 89.90
        print(f'Valor a ser gasto plano por dia {total}')
    else:
        total = dias * 69.90
        print(f'Valor a ser gasto plano por dia {total}')
    if distancia <= 500:
        totald = 0
        totald = distancia * 0.85
        print(f'Valor a ser gasto {totald}')
    elif distancia > 500 and distancia <= 900:
        totald = 0
        totald = distancia * 0.75
        print(f'Valor a ser gasto {totald}')
    elif distancia > 900 and distancia <= 2000:
        totald = 0
        totald = distancia * 0.69
        print(f'Valor a Ser gasto {totald}')
    else:
        totald = 0
        totald = distancia * 0.65
        print(f'Valor a Ser gasto {totald}')

dias = int(input("Bem vindo a Locadora de Veiculos, Informe a quantidade de dias que deseja\n"))
distancia = int(input("Digite a Quantidade de Quilometros que irá Percorrer\n"))
CalculaTotal(dias, distancia)