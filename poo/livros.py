class Livro:
    def __init__(self, nome, paginas, status):
        self.nome = nome
        self.paginas = paginas
        self.status = status
        
    def verificar_status(self):
        print('Disponível' if self.status else 'Indisponível')
            
class Biblioteca():
    def __init__(self):
        self.livros = []
    
    def adicionar_livros(self, livro):
        self.livros.append(livro)
        
    def listar_livros(self):
        for livro in self.livros:
            print(f'Nome: {livro.nome} - {livro.paginas} páginas.')
            
        
livro1 = Livro('Harry Potter', 320, True)
livro2 = Livro('Bíblia', 1.300, False)

biblioteca = Biblioteca()
biblioteca.adicionar_livros(livro1)
biblioteca.adicionar_livros(livro2)

biblioteca.listar_livros()
livro1.verificar_status()




