from typing import List
from Infrastructure.Connection.DbCaderno import DbCaderno
from Domain.Entities.Anotacao import Anotacao

def GetAnotacaoByQtd(qtd: int) -> List[Anotacao] :
    with DbCaderno() as session:
        try:
            return session.query(Anotacao).limit(qtd).all()
        except Exception as e:
            print(f"Erro ao buscar anotações: {e}")
            return []

def GetAnotacaoById(id: int) -> Anotacao:
    with DbCaderno() as session:
        try:
            return session.query(Anotacao).filter(Anotacao.Id == id).first()
        except Exception as e:
            print(f"Erro ao buscar anotação por ID: {e}")
            return None
        
def Add(anotacao: Anotacao):
    with DbCaderno() as session:
        try:
            session.add(anotacao)
            session.commit()
            print("Anotação adicionada com sucesso.")
        except Exception as e:
            session.rollback()
            print(f"Erro ao adicionar anotação: {e}")

def Update(anotacao: Anotacao):
    with DbCaderno() as session:
        try:
            anotacao_atual = session.query(Anotacao).filter(Anotacao.Id == anotacao.Id).first()
            if anotacao_atual:
                anotacao_atual.Titulo = anotacao.Titulo
                anotacao_atual.Anotacao = anotacao.Anotacao

                session.commit()
                print("Anotação atualizada com sucesso.")
            else:
                print(f"Anotação com ID {anotacao.Id} não encontrada.")
        except Exception as e:
            session.rollback()
            print(f"Erro ao atualizar anotação: {e}")

def Delete(id: int):
    with DbCaderno() as session:
        try:
            anotacao = session.query(Anotacao).filter(Anotacao.Id == id).first()
            if anotacao:
                session.delete(anotacao)
                session.commit()
                print("Anotação removida com sucesso.")
            else:
                print(f"Anotação com ID {id} não encontrada.")
        except Exception as e:
            session.rollback()
            print(f"Erro ao remover anotação: {e}")
            raise(e)