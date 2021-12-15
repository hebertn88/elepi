from utils import *


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

    id_funcionario = Column(Integer, primary_key = True)
    nome = Column(String, nullable = False, unique = True)
    data_admissao = Column(Date, nullable = False)
    data_demissao = Column(Date)
    departamento_id = Column(Integer, ForeignKey('departamentos.id_departamento'))


class Epis(Base):
    __tablename__ = 'epis'

    id_epi = Column(Integer, primary_key = True)
    descricao = Column(String, nullable = False, unique = True)
    valor_custo = Column(Float,  nullable = False, default = 0)
    estoque_novos = Column(Integer,  nullable = False, default = 0)
    estoque_usados = Column(Integer,  nullable = False, default = 0)


class EpisDepartamentos(Base):
    __tablename__ = 'epis_departamentos'

    id_epi_departamento = Column(Integer, primary_key = True)
    epi_id = Column(Integer, ForeignKey('epis.id_epi'))
    departamento_id = Column(Integer, ForeignKey('departamentos.id_departamento'))
    vida_util = Column(Integer,  nullable = False, default = 0)


class EpisMovimentacao(Base):
    __tablename__ = 'epis_movimentacao'

    id_movimento = Column(Integer, primary_key = True)
    data_movimento = Column(Date, nullable = False, default = datetime.today())
    descricao = Column(String, nullable = False)
    usuario_id = Column(Integer, ForeignKey('usuarios.id_usuario'))
    funcionario_id = Column(Integer, ForeignKey('funcionarios.id_funcionario'))
    epi_id = Column(Integer, ForeignKey('epis.id_epi'))
    qtd = Column(Integer, nullable = False, default = 1)
    valor_custo = Column(Float,  nullable = False, default = 0)


class MotivosDevolucao(Base):
    __tablename__ = 'motivos_devolucao'

    id_motivo = Column(Integer, primary_key = True)
    descricao = Column(String, nullable = False, unique = True)
    

class FuncionariosEpis(Base):
    __tablename__ = 'funcionarios_epis'

    id_funcionarios_epis = Column(Integer, primary_key = True)
    funcionario_epi = Column(Integer, ForeignKey('funcionarios.id_funcionario'))
    epis_id = Column(Integer, ForeignKey('epis.id_epi'))
    data_entrega = Column(Date, nullable = False)
    data_devolucao = Column(Date)
    motivo_id = Column(Integer, ForeignKey('motivos_devolucao.id_motivo'))

Base.metadata.create_all(engine)