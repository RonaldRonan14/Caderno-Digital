from typing import List
from Infrastructure.Repositories import AnotacaoRepository
from Domain.Entities.Anotacao import Anotacao

def GetAnotacaoByQtd(qtd: int) -> List[Anotacao]:
    return AnotacaoRepository.GetAnotacaoByQtd(qtd)

def GetAnotacaoById(id: int) -> Anotacao:
    return AnotacaoRepository.GetAnotacaoById(id)

def Add(anotacao: Anotacao):
    AnotacaoRepository.Add(anotacao)

def Update(anotacao: Anotacao):
    AnotacaoRepository.Update(anotacao)

def Delete(id: int):
    try:
        AnotacaoRepository.Delete(id)
    except Exception as e:
        raise(e)