#import para verificacao do Arquivo do Banco de Dados
import os
from datetime import datetime

#import do Arquivo models.py
import models as db
db.Base.metadata.create_all(db.engine)

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

db.insere_usuario('hebert', '123456')

if db.valida_usuario('hebert', '123456'):
    db.insere_departamento('Padaria')
    db.insere_funcionario('Joaoasdfdfdas','1', db.formata_data('01/09/2021'))