


class Produto:
    def __init__(self, descricao, preco):
        self.descricao = descricao
        self.preco = preco
    def exibirPreco(self):
        print(f'{self.descricao} por apenas {self.preco}')

class Pessoa:
    def __init__(self, nome='', altura='', cpf='', rg='', data='') -> None:
        self.nome = nome
        self.altura = altura
        self.cpf = cpf
        self.rg = rg
        self.data = data
    def cadastrarPessoa(self):
        self.nome = input("Seu Nome: ")
        self.altura = input("Fale Sua Altura: ")
        self.cpf = input("Informe seu CPF:")
        self.rg = input("Informe seu RG: ")
        self.data = input("Informe sua data de Nascimento: ")
        
        print(f"O nome da pessoa é:{self.nome} \nA Altura da pessoa é:{self.altura} \nO CPF:{self.cpf} \nO RG:{self.rg}\nNasceu em:{self.data}")

class AssinaturaTv:
    def __init__(self) -> None:
        self.canaisDisponiveis = (2, 5, 7, 15, 30, 50)
        self.__canalAtivo = 7
        self.volume = 10
    @property
    def canalAtivo(self):
        return(self.__canalAtivo)
    @canalAtivo.setter
    def canalAtivo(self, canal):
        try:
            index=self.canaisDisponiveis.index(canal)
            self.__canalAtivo = canal
            print(f'O canal ativo agora é: {canal}')
        except:
            index=-1
            print(f'O canal {canal} não está disponível')






class Valor:
    def __init__(self, descricao, precoCusto):
        self.descricao = descricao
        self.precoCusto = precoCusto
        self.__precoVenda = None
    @property
    def precoVenda(self):
        return(self.__precoVenda)
    @precoVenda.setter
    def precoVenda(self, pvenda):
        if pvenda>self.precoCusto:
            self.__precoVenda=pvenda
        else:
            print("***O valor inserido é menor que o preço de custo***")