from utils import *
from models import MotivosDevolucao, Usuarios, Departamentos, Funcionarios, Epis, EpisDepartamentos


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
    
    with Session(engine) as session:
        
    if db.session.query(Usuarios).filter_by(usuario = usuario.usuario).one_or_none(): #retorna False se usuario ja existir
        print('insere usuario: False')
        return False

    try: #insere ususario
        db.session.add(usuario)
        db.session.commit()
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
    usuario = db.session.query(Usuarios).filter_by(usuario = usuario).one_or_none()

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

    if db.session.query(Departamentos).filter_by(nome = departamento.nome).one_or_none(): #retorna False se usuario ja existir
        print('insere departamento: False')
        return False

    try: #insere departamento
        db.session.add(departamento)
        db.session.commit()
        print('insere departamento: True')
        return True
    except Error as erro:
        print(f"insere departamento: {erro}")
        return erro


def insere_funcionario(nome, departamento_id, data_admissao = datetime.today()):
    """
    Insere novo funcionario.\n
    Retorno:\n
    True = funcionario inserido com sucesso.\n
    False = funcionario ja existe.
    """
        
    nome = trata_texto(nome)
    departamento = Departamentos(id_departamento = departamento_id)
    funcionario = Funcionarios(nome = nome, data_admissao = data_admissao, departamento_id = departamento.id_departamento)

    if db.session.query(Departamentos).filter_by(id_departamento = departamento.id_departamento).one_or_none(): #retorna False se departamento nao existir
        if db.session.query(Funcionarios).filter_by(nome = funcionario.nome).one_or_none(): #retorna False se funcionario ja existir
            print('insere funcionario: False')
            return False
        else: #insere funcionario se nao existir
            try:
                db.session.add(funcionario)
                db.session.commit()
                print('insere funcionario: True')
                return True
            except Error as erro:
                print(f"insere funcionario: {erro}")
                return erro
    else:
        print('insere funcionario: [Departamento]False')
        return False


def insere_epi(descricao, valor_custo = 0, estoque_novos = 0, estoque_usados = 0):
    """
    Insere novo epi.\n
    Retorno:\n
    True = epi inserido com sucesso.\n
    False = epi ja existe.
    """

    descricao = trata_texto(descricao)
    epi = Epis(descricao = descricao, valor_custo = valor_custo, estoque_novos = estoque_novos, estoque_usados = estoque_usados)

    if db.session.query(Epis).filter_by(descricao = epi.descricao).one_or_none(): #retorna False se epi ja existe
        print('insere epi: False')
        return False
    else: #insere epi
        try:
            db.session.add(epi)
            db.session.commit()
            print('insere epi: True')
            return True
        except Error as erro:
            print(f"insere epi: {erro}")
            return erro


def associa_epi_departamento(epi, departamento, vida_util = 0):
    """
    Associa Epi - Departamento.\n
    Retorno:\n
    True = associado com sucesso.\n
    False = associacao já existe.
    """

    epi_departamento = EpisDepartamentos(epi_id = epi, departamento_id = departamento, vida_util = vida_util)

    if db.session.query(EpisDepartamentos).filter_by(epi_id = epi_departamento.epi_id, departamento_id = epi_departamento.departamento_id).one_or_none():
        print('associa epi-departamento: False')
        return False
    else:
        try:
            db.session.add(epi_departamento)
            db.session.commit()
            print('associa epi-departamento: True')
            return True
        except Error as erro:
            print(f"associa epi-departamento: {erro}")
            return erro


def insere_motivo(motivo):
    """
    Insere novo motivo de devolucao\n
    Retorno:\n
    True = motivo inserido com sucesso.\n
    False = motivo ja existe.
    """

    motivo = trata_texto(motivo)
    motivo = MotivosDevolucao(descricao = motivo)

    if db.session.query(MotivosDevolucao).filter_by(descricao = motivo.descricao).one_or_none():
        print('insere motivo: False')
        return False
    else:
        try:
            db.session.add(motivo)
            db.session.commit()
            print('insere motivo: True')
            return True
        except Error as erro:
            print(f"insere motivo: {erro}")
            return erro


def entrega_epi():
    pass
    #registra na tabela funcionario-epi
    #registra tabela extrato epi
    #estoque tabela estoque epi