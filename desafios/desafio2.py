rendimento = int(input('Digite o rendimento da tinta em metros quadrados por litro: '))

altura = int(input('Digite a altura da parede em metros: '))

largura = int(input('Digite a largura da parede em metros: '))

def calcular_tinta():
    area = altura * largura
    tinta_necessaria = area / rendimento
    print(f'Você precisará de {tinta_necessaria:.2f} latas de tinta para pintar a parede.')

calcular_tinta()