#sqlalchemy para manipulacao banco de dados
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from passlib.hash import pbkdf2_sha256

#class Conexao(object):

#def __init__(self):

#Cria conexão e sessão com banco de dados
engine = create_engine("sqlite:///data.db")
Session = sessionmaker(bind=engine)
session = Session()
base = declarative_base()


class Usuario(base):

    __tablename__ = 'usuarios'
    
    id_usuario = Column(Integer, primary_key=True)
    usuario = Column(String, nullable=False, unique=True)
    senha = Column(String, nullable=False)


def usuario_inserir(pusuario, psenha):
    psenha = pbkdf2_sha256.hash(psenha)
    usuario = Usuario(usuario = psenha, senha = psenha)
    session.add(usuario)
    session.commit()


def usuario_valida(pusuario, psenha):
    usuario = session.query(Usuario).filter_by(usuario=pusuario).one_or_none()

    #print(query.usuario)

    #usuario = {}

    #for u in query:
    #    usuario['usuario'] = u.usuario
    #    usuario['senha'] = u.senha
    if usuario:
        return pbkdf2_sha256.verify(psenha, usuario.senha)


#result = con.session.execute("select * from usuarios")
#for r in result:
#    print(r)
"""
metadata_obj = MetaData()

user = Table('user', metadata_obj,
    Column('user_id', Integer, primary_key=True),
    Column('user_name', String(16), nullable=False),
    Column('email_address', String(60), key='email'),
    Column('nickname', String(50), nullable=False)
)

user_prefs = Table('user_prefs', metadata_obj,
    Column('pref_id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey("user.user_id"), nullable=False),
    Column('pref_name', String(40), nullable=False),
    Column('pref_value', String(100))
)

SQLmetadata_obj.create_all(engine)

"""