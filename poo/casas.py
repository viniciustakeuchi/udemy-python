class Casa:
    def __init__(self, cor, quartos, banheiros):
        self.cor = cor
        self.quartos = quartos
        self.banheiros = banheiros
    
    def mostrar_cor(self):
        print(f'A cor da casa é {self.cor}')
        
    def mostrar_quartos(self):
        print(f'Está casa tem {self.quartos} quartos')
        
    def mostrar_banheiros(self):
        print(f'Está casa tem {self.banheiros} banheiros')
    
    def adicionar_quarto(self):
        self.quartos +=1
        print(f'Esta casa tem {self.quartos} quartos')
    
    def remover_quarto(self):
        self.quartos -=1
        print(f'Está casa tem {self.quartos} quartos')
        
    def pintar_casa(self, nova_cor):
        print(f'A nova cor da casa é: {nova_cor}')
        
        
casa1 = Casa('Amarelo', 4, 3)
casa2 = Casa('Vermelho', 2, 2)

print('\nCasa 1:')
casa1.mostrar_cor()
casa1.mostrar_quartos()
casa1.mostrar_banheiros()
casa1.adicionar_quarto()

print('\nCasa 2:')
casa2.mostrar_cor()
casa2.mostrar_quartos()
casa2.mostrar_banheiros()
casa2.remover_quarto()
casa2.pintar_casa('Vermelho')
    
        