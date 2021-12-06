#sqlalchemy para manipulacao banco de dados
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#import para exibição de Erros SQLite
from sqlite3 import Error

#import modulo de criptografia
from passlib.hash import pbkdf2_sha256


#Cria conexão e sessão com banco de dados
engine = create_engine("sqlite:///data/data.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Usuarios(Base):
    __tablename__ = 'usuarios'
    
    id_usuario = Column(Integer, primary_key=True)
    usuario = Column(String, nullable=False, unique=True)
    senha = Column(String, nullable=False)


def usuario_inserir(pusuario, psenha):
    psenha = pbkdf2_sha256.hash(psenha)
    usuario = Usuarios(usuario = pusuario, senha = psenha)
    
    if session.query(Usuarios).filter_by(usuario=pusuario).one_or_none():
        return False

    try:
        session.add(usuario)
        session.commit()
        return True
    except Error as erro:
        return erro


def usuario_valida(pusuario, psenha):
    usuario = session.query(Usuarios).filter_by(usuario=pusuario).one_or_none()
    if usuario:
        return pbkdf2_sha256.verify(psenha, usuario.senha)

