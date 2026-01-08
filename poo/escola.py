class Escola:
    def __init__(self, nome, idade, status):
        self.nome = nome
        self.idade = idade
        self.status = status
        
    def apresentar(self):
        print(f'Meu nome é {self.nome}')
        
    def verificar_status(self):
        print(f'Status {"ATIVO" if self.status else "INATIVO"}')
        
class Aluno(Escola):
    def __init__(self, nome, idade, status, ano):
        super().__init__(nome, idade, status)
        self.ano = ano
        
    def apresentar(self):
        # Pegou o método apresentar() da classe Pai
        super().apresentar()
        print(f'Eu sou um aluno da escola')
        
        
class Professor(Escola):
    def __init__(self, nome, idade, status, materia):
        super().__init__(nome, idade, status)
        self.materia = materia
    
    def apresentar(self):
        # Pegou o método apresentar() da classe Pai
        super().apresentar()
        print(f'Eu sou um professor da escola')

class Assistente(Escola):
    def __init__(self, nome, idade, status, bloco):
        super().__init__(nome, idade, status)
        self.materia = bloco
    
    def apresentar(self):
        # Pegou o método apresentar() da classe Pai
        super().apresentar()
        print(f'Eu sou um(a) assistente da escola')
        
a1 = Aluno(nome='Marcos',idade=12,status=True,ano=8)
print(a1.ano)

p1 = Professor(nome='Roberto',idade=34,status=True,materia='Geometria')
as1 = Assistente(nome='Ana Maria',idade=29,status=True,bloco='Bloco C')
a1.apresentar()
p1.apresentar()
as1.verificar_status()