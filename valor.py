
"""
from classe import Produto

computador = Produto('i5 10°gen', 8900.30)
videoGame = Produto('PlayStation 5', 5350.29)
celular = Produto('Samsung s21 PRO', 99990.32)

computador.exibirPreco()
videoGame.exibirPreco()
celular.exibirPreco()
"""

from classe import Valor
geladeira = Valor('Geladeira', 2500)
print(f'O Preço de custo do/a {geladeira.descricao}, é R${geladeira.precoCusto}')

geladeira.precoVenda=float(input("Insira um valor para o preço de Venda"))

print(geladeira.precoVenda)