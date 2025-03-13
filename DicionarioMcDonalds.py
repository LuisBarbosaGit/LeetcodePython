from typing import Match

Lanches = {
    '1': 'McChiken',
    'Valor1': 29.99,
    '2': 'McFeliz',
    'Valor2': 34.90,
    '3': 'BigMac',
    'Valor3': 45.90,
    '4': 'McSalada',
    'Valor4': 20,
    '5': 'McCheddar',
    'Valor5': 50}
Sobremesas = {
    '1': 'McFlury',
     'Valor1':   15,
    '2':'Casquinha',
     'Valor2':   5,
    '3':'Cascao',
     'Valor3':   8,
    '4':'McNutella',
     'Valor':   12,
    '5': 'McCake',
     'Valor4':   14
}
escolhas = []
total = 0
while True:
    Escolha = int(input('Bem vindo Ao Sistema do MC Donalds!!!\nDigite:\n"1" Adicionar Lanches\n"2" Adicionar Sobremesas\n"3" Cupom\n"0" Sair\n'))
    match Escolha:
        case 1:
            lanches = Lanches.values()
            print(list(lanches))
            EscLanche = input('Escreva 1-2-3-4 com base em qual Lanche Deseja\n')
            escolhas.append(Lanches[EscLanche])
            print(f'Você escolheu {Lanches[EscLanche]}, item adicionado com sucesso\n')
            match EscLanche:
                case '1':
                    total = total + Lanches['Valor1']
                case '2':
                    total = total + Lanches['Valor2']
                case '3':
                    total = total + Lanches['Valor3']
                case '4':
                    total = total + Lanches['Valor4']
                case '5':
                    total = total + Lanches['Valor5']
        case 2:
            sobremesas = Sobremesas.values()
            print(list(sobremesas))
            EscSobre =  input('Escreva 1-2-3-4 com base em qual Sobremesa Deseja\n')
            escolhas.append(Sobremesas[EscSobre])
            print(f'Você escolheu {Sobremesas[EscSobre]}, item adicionado com sucesso')
            match EscSobre:
                case '1':
                    total = total + Sobremesas['Valor1']
                case '2':
                    total = total + Sobremesas['Valor2']
                case '3':
                    total = total + Sobremesas['Valor3']
                case '4':
                    total = total + Sobremesas['Valor4']
                case '5':
                    total = total + Sobremesas['Valor5']
        case 3:
            cupom = int(input('Informe qual é seu cupom\n1-ABC5F\n2-WER2A\n3-BNM9R\n4-QDG8X'))
            match cupom:
                case 1:
                    print('Desconto 5%')
                    total =- (total * 0.05)
                case 2:
                    print('Desconto 8%')
                    total =- (total * 0.08)
                case 3:
                    print('Desconto 10%')
                    total =- (total * 0.1)
                case 4:
                    print('Desconto 18%')
                    total =- (total * 0.18)
        case 0:
            break

print('Obrigado pela Preferencia, aqui está sua conta:\n')
print(f'Itens Escolhidos:{escolhas}\n Total Conta {total}')

