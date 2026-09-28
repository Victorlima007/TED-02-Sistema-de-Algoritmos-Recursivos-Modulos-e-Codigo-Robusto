

class CentralRecursivaError(Exception):

    mensagem_saida = "ERRO: ErroDesconhecido"

    def __init__(self, detalhe=""):
        self.detalhe = detalhe
        super().__init__(detalhe or self.mensagem_saida)


class OperacaoInvalidaError(CentralRecursivaError):

    mensagem_saida = "ERRO: OperacaoInvalida"


class EntradaInvalidaError(CentralRecursivaError):
    mensagem_saida = "ERRO: EntradaInvalida"
