#banco de dados
import sqlite3
from sqlite3 import Error

#criptografia da senha do usuario
from passlib.hash import pbkdf2_sha256 

class Conexao(object):

    def __init__(self, database):
        self.database = database


    def conecta(self):
       self.connection = sqlite3.connect(self.database)
       self.cursor = self.connection.cursor()


    def commit(self):
        self.connection.commit()


    def encerra(self):
        self.connection.close()


    def consultar(self, sql):
        try:
            self.conecta()
            self.cursor.execute(sql)
            dados = self.cursor.fetchall()
            self.encerra()
            return dados
        except Error as erro:
            print(erro)
  

    def inserir(self,sql):
        try:
            self.conecta()
            self.cursor.execute(sql)
            self.commit()
            self.encerra()
        except Error as erro:
            print(erro)


def senha_criptografa(senha):
    senha = pbkdf2_sha256.hash(senha)
    return senha


def senha_verifica(senha1, cript1):
    return pbkdf2_sha256.verify(senha1, cript1)


db = Conexao('data.db') #instancia classe conexao para manuseio do banco de dados

senha = senha_criptografa('123456') #criptografa senha
db.inserir(f"INSERT INTO usuarios (usuario, senha) VALUES ('Maria', '{senha}')") #insere usuario

gprint(db.consultar('select * from usuarios')) #mostra todos usuarios

dado = db.consultar("select senha from usuarios where usuario like 'hebert'") #captura senha do usuario pesquisado

print(senha_verifica('123456', dado[0][0])) #verifica senha do usuario