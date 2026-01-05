class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def apresentar(self):
        print(f'Olá, meu nome é {self.nome} e tenho {self.idade} anos de idade')
        
class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo):
        super().__init__(nome, idade) # Puxar as infos da classe pai: Pessoa. Usa a função embutida super() quando você quer adicionar um novo parâmetro
        self.cargo = cargo
    
    def trabalhar(self):
        print(f'{self.nome} está trabalhando como {self.cargo}')

class Cliente(Pessoa):
    def __init__(self, nome, idade, saldo):
        super().__init__(nome, idade) # Puxar as infos da classe pai: Pessoa. Usa a função embutida super() quando você quer adicionar um novo parâmetro
        self.saldo = saldo
    
    def comprar(self, valor_compra):
        if valor_compra <= self.saldo:
            self.saldo -= valor_compra
            print(f'Olá {self.nome}, a sua compra de {valor_compra} foi aprovada! Se saldo atual é de R${self.saldo}')
        else:
            print(f'Olá {self.nome} o seu saldo foi insuficiente.')
        
f1 = Funcionario('Maria', 38, 'Gerente de contas')
f1.trabalhar()

c1 = Cliente('Arthur', 16, 200)
c2 = Cliente('José', 28, 100)
c1.apresentar()
c1.comprar(30)
c2.comprar(100)