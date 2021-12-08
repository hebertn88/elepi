#sqlalchemy para manipulacao banco de dados
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

#import para exibição de Erros SQLite
from sqlite3 import Error

#import modulo de criptografia
from passlib.hash import pbkdf2_sha256

import unicodedata

from datetime import date, datetime

from sqlalchemy.sql.schema import ForeignKey


#Cria conexão e sessão com banco de dados
engine = create_engine("sqlite:///data/data.db")#, echo = True)
Session = sessionmaker(bind = engine)
session = Session()
Base = declarative_base()

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

class Usuarios(Base):
    __tablename__ = 'usuarios'
    
    id_usuario = Column(Integer, primary_key = True)
    usuario = Column(String, nullable = False, unique = True)
    senha = Column(String, nullable = False)


class Departamentos(Base):
    __tablename__ = 'departamentos'
    
    id_departamento = Column(Integer, primary_key = True)
    nome = Column(String, nullable = False, unique = True)

class Funcionarios(Base):
    __tablename__ = 'funcionarios'

    id_departamento = Column(Integer, primary_key = True)
    nome = Column(String, nullable = False, unique = True)
    data_admissao = Column(Date, nullable = False)
    data_demissao = Column(Date)
    departamento_id = Column(Integer, ForeignKey('departamentos.id_departamento'))


def insere_usuario(usuario, senha):
    """
    Insere novo usuario.\n
    Retorno:\n
    True = usuario inserido com sucesso.\n
    False = usuario ja existe
    """

    usuario = trata_texto(usuario)
    senha = pbkdf2_sha256.hash(senha) #criptografa senha
    usuario = Usuarios(usuario = usuario, senha = senha)
    
    if session.query(Usuarios).filter_by(usuario = usuario.usuario).one_or_none(): #retorna False se usuario ja existir
        print('insere usuario: False')
        return False

    try: #insere ususario
        session.add(usuario)
        session.commit()
        print('insere usuario: True')
        return True
    except Error as erro:
        print(f"insere usuario: {erro}")
        return erro


def valida_usuario(usuario, senha):
    """
    Valida usuario e senha.\n
    Retorno:\n
    True = usuario e senha validado com sucesso.\n
    False = senha invalida.\n
    None = usuario nao encontrado.
    """

    usuario = trata_texto(usuario)
    usuario = session.query(Usuarios).filter_by(usuario = usuario).one_or_none()

    if usuario: #se usuario existir faz a validacao de senha
        print(f"valida usuario: {pbkdf2_sha256.verify(senha, usuario.senha)}")
        return pbkdf2_sha256.verify(senha, usuario.senha)
    else: #se usuario nao existir retorna None
        print(f"valida usuario: {usuario}")
        return usuario


def insere_departamento(departamento):
    """
    Insere novo departamento.\n
    Retorno:\n
    True = departamento inserido com sucesso.\n
    False = departamento ja existe
    """

    departamento = trata_texto(departamento)
    departamento = Departamentos(nome = departamento)

    if session.query(Departamentos).filter_by(nome = departamento.nome).one_or_none(): #retorna False se usuario ja existir
        print('insere departamento: False')
        return False

    try: #insere departamento
        session.add(departamento)
        session.commit()
        print('insere departamento: True')
        return True
    except Error as erro:
        print(f"insere departamento: {erro}")
        return erro

def insere_funcionario(nome, departamento_id, data_admissao = date.today()):
    """
    Insere novo funcionario.\n
    Retorno:\n
    True = funcionario inserido com sucesso.\n
    False = funcionario ja existe.
    """
        
    nome = trata_texto(nome)
    departamento = Departamentos(id_departamento = departamento_id)
    funcionario = Funcionarios(nome = nome, data_admissao = data_admissao, departamento_id = departamento.id_departamento)

    if session.query(Departamentos).filter_by(id_departamento = departamento.id_departamento).one_or_none(): #retorna False se departamento nao existir
        if session.query(Funcionarios).filter_by(nome = funcionario.nome).one_or_none(): #retorna False se funcionario ja existir
            print('insere funcionario: False')
            return False
        else: #insere funcionario se nao existir
            try:
                session.add(funcionario)
                session.commit()
                print('insere funcionario: True')
                return True
            except Error as erro:
                print(f"insere funcionario: {erro}")
                return erro
    else:
        print('insere funcionario: [Departamento]False')
        return False
