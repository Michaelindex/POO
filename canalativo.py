"""from classe import AssinaturaTv
tv = AssinaturaTv()
print(tv)
print('Canais DIsponíveis')
print(tv.canaisDisponiveis)
print('---')
print('Canal Ativo')
print(tv.canalAtivo)
print('---')
tv.canalAtivo = 15
print(tv.canalAtivo)
print('---')
tv.canalAtivo = 25
print('Canal Ativo')
print(tv.canalAtivo)
print('---') """

from classe import Valor

geladeira = Valor()
print(f"A descrição é:{geladeira.descricao}, o Preço de Custo foi:{geladeira.precoCusto} e o Preço de Venda é:{geladeira.precoVenda}")