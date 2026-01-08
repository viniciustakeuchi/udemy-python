class Personagens():
    def falar(self):
        print('Eu sou um personagem')

class Guerreiro(Personagens):
    def falar(self):
        print('Eu sou um guerreiro forte e destemido!')

class Mago(Personagens):
    def falar(self):
        print('Eu sou um mago sabio e poderoso!')
        
class Arqueiro(Personagens):
    def falar(self):
        print('Eu sou um arqueiro rápido e destemido!')

# Criar os objetos com lista 
personagens = [Guerreiro(), Mago(), Arqueiro()]

for p in personagens:
    p.falar()

class Cachorro():
    def emitir_som(self):
        print('au au au!')

class Gato():
    def emitir_som(self):
        print('miau!')
        
animais = [Cachorro(), Gato()]

for a in animais:
    a.emitir_som()

class Pessoa1:
    def microfone(self):
        print('Meu nome é Maria')
        
class Pessoa2:
    def microfone(self):
        print('Meu nome é Ana')
        
sala = [Pessoa1(), Pessoa2()]

for pessoas in sala:
    pessoas.microfone()
        
        
        