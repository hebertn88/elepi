import os

from datetime import datetime #manipulacao data e hora

#sqlalchemy para manipulacao banco de dados
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, Float
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

from sqlite3 import Error #exibicao dos erros SQLite

from passlib.hash import pbkdf2_sha256 #criptografia das senhas

import unicodedata #tratamento do texto


#######################################
#       F I M    I M P O R T S         
#######################################


#Cria conexão e sessão com banco de dados
class Conexao(object):

    def __init__(self, local):
        self.engine = create_engine(local)#, echo = True)
        self.Session = sessionmaker(bind = self.engine)
        self.session = self.Session()
        self.Base = declarative_base()

    def create_all(self):
        self.Base.metadata.create_all(self.engine)


db = Conexao("sqlite:///data/data.db")


def trata_texto(texto):
    """
    Trata textos convertendo para maiusulo,\n
    sem acentos e espaços indesejaveis.
    """

    texto = texto.strip().upper()
    texto = unicodedata.normalize("NFKD", texto)
    texto = texto.encode("ascii", "ignore")
    texto = texto.decode("utf-8").upper()
#    print(f"trata texto: \"{texto}\"")
    return(texto)


def formata_data(pdata):
    return datetime.strptime(pdata, '%d/%m/%Y')

