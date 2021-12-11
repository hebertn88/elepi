from utils import *
from models import *
from control import *

#        self.Base.metadata.create_all(self.engine)


"""if not os.path.isfile('./data/data.db'):
    print('Banco de dados não encontrado.')
    print('Criando novo Banco de dados...')

    try:
        db.Base.metadata.create_all(db.engine)
        print('Banco de Dados criado com sucesso!')
    except Error as erro:
        print('inicio erro banco')
        print(erro)
        print('fim erro banco')"""


insere_usuario('eldorado', '123456')

if valida_usuario('eldorado', '123456'):
    insere_departamento('padaria')
    insere_funcionario('Maria','1', formata_data('01/09/2021'))
    insere_epi('Camiseta Branca P', 25.0, 10)
    insere_epi('Camiseta Branca M', 25.0, 10)
    associa_epi_departamento(1, 1, 18)
    insere_motivo('fim da vida util')
