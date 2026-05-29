#Crie uma classe que represente um vídeo com os atributos título, duração e views
class Video:
    def __init__(self, titulo, duracao, views):
        self.titulo = titulo
        self.duracao = duracao
        self.views = views

video = Video("Baleia Azul", "5:00", 10000)


# Como poderia ser criada uma classe que represente o objeto livro = Livro(titulo,autor,data_publicacao)?
class Livro:
    def __init__(self, titulo, autor, data_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.data_publicacao = data_publicacao
livro = Livro("A história do Xamã", "Eduardo Klen", "29/11/2008")