#import para verificacao do Arquivo do Banco de Dados
import os

#criptografia da senha do usuario
from passlib.hash import pbkdf2_sha256
from sqlalchemy.orm import session

#import do Arquivo models.py
import models as db

from sqlite3 import Error


if not os.path.isfile('./data/data.db'):
    print('Banco de dados não encontrado.')
    print('Criando novo Banco de dados...')

    try:
        db.Base.metadata.create_all(db.engine)
        print('Banco de Dados criado com sucesso!')
    except Error as erro:
        print('inicio erro banco')
        print(erro)
        print('fim erro banco')


db.usuario_inserir('hebert', '123456')
