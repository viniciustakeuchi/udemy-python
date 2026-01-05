class Carro:
    # iniciando o construtor
    def __init__(self, cor, ano):
        self.cor = cor
        self.ano = ano
        self.ligado = False
        self.seta = None
    # método para mostrar infos do carro
    def informacoes(self):
        print(f'A cor do carro é {self.cor}')
        print(f'O ano do carro é {self.ano}')

    # método para ligar o carro
    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print('O carro foi ligado!')
        else:
            print('O carro já estava ligado!')
            
    #método para desligar o carro
    def desligar(self):
        # se for verdadeiro, ou seja, se o carro estiver ligado
        if self.ligado:
            # faça:
            self.ligado = False
            print('O carro foi desligado!')
        else:
            print('O carro já estava desligado!')
            
    def ligar_seta(self, direcao):
        if not self.ligado:
            print('Ligue o carro primeiro :)')
            return
        self.seta = direcao
        print(f'Seta ligada para a {self.seta}')
        
carro1 = Carro('Prata', 2010)
carro1.informacoes()
carro1.ligar()
carro1.desligar()
carro1.ligar_seta('esquerda')


        
    
    
    
    
    
    