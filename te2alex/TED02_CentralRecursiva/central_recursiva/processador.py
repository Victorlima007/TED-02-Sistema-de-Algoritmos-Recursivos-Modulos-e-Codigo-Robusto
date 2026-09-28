
from central_recursiva.algoritmos import mdc, soma_digitos
from central_recursiva.excecoes import CentralRecursivaError
from central_recursiva.validador import (
    identificar_operacao,
    validar_operacao_mdc,
    validar_operacao_soma,
)


class Resumo:

    def __init__(self):
        self.processadas = 0
        self.com_erro = 0

    def __str__(self):
        return (f"linhas processadas: {self.processadas} | "
                f"com erro: {self.com_erro}")


def processar_linha(linha, resumo=None):
    partes = linha.split()
    if not partes:
        return None

    houve_erro = False

    try:
        operacao = identificar_operacao(partes[0])

        if operacao == "M":
            a, b = validar_operacao_mdc(partes)
            return f"MDC = {mdc(a, b)}"

        n = validar_operacao_soma(partes)
        return f"SOMA = {soma_digitos(n)}"

    except CentralRecursivaError as erro:
        houve_erro = True
        return erro.mensagem_saida

    finally:
        if resumo is not None:
            resumo.processadas += 1
            if houve_erro:
                resumo.com_erro += 1
