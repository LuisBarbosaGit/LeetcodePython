import time

def ImprimeRelatorio(escolha, quantia):
    opcao = ['Az Investimentos', 'Crypto invest', 'Bitcoin XP']
    rent = [0.5, 0.8, 1.2,1.1, 1.5, 1.9,2.1, 2.8, 3.9]
    quantia = quantia * rent[escolha - 1]
    if escolha >= 1 and escolha <= 3:
        Tipo = opcao[0]
    elif escolha >= 4 and escolha <= 6:
        Tipo = opcao[1]
    else:
        Tipo = opcao[2]
    print(f'Com Base na sua Escolha, a Melhor Sugestão de Investimentos Para você é a {Tipo} \nRentabilidade: {rent[escolha - 1]} \nRetorno Total: {quantia} ')


def SugereInvestimento(quantia, risco, tempo):
    match risco:
        case 'Baixo':
            match tempo:
                case 24:
                    ImprimeRelatorio(1, quantia)
                case 60:
                    ImprimeRelatorio(2, quantia)
                case 120:
                    ImprimeRelatorio(3, quantia)
        case 'Media':
            match tempo:
                case 24:
                    ImprimeRelatorio(4, quantia)
                case 60:
                    ImprimeRelatorio(5, quantia)
                case 120:
                    ImprimeRelatorio(6, quantia)
        case 'Alto':
            match tempo:
                case 24:
                    ImprimeRelatorio(7, quantia)
                case 60:
                    ImprimeRelatorio(8, quantia)
                case 120:
                    ImprimeRelatorio(9, quantia)

print('Bem vindo ao sistema de sugestão de investimentos')
quantia = float(input('Digite a Quantia que deseja Investir \n'))
risco = input('Digite a CLassificação de Risco \n 1-"Baixo" \n 2-"Media" \n 3-"Alto" \n ')
tempo = int(input('Digite o Tempo que deseja Investir \n 24 \n 60 \n 120 \n'))
print('Aguarde, processando Informações.........')
time.sleep(2)
SugereInvestimento(quantia, risco, tempo)
