

import re

from central_recursiva.excecoes import (
    EntradaInvalidaError,
    OperacaoInvalidaError,
)

OPERACOES_CONHECIDAS = ("M", "S")

_PADRAO_INTEIRO = re.compile(r"-?[0-9]+")


def identificar_operacao(codigo):
    if codigo not in OPERACOES_CONHECIDAS:
        raise OperacaoInvalidaError(f"operação desconhecida: {codigo!r}")
    return codigo


def converter_inteiro(texto):
    if not _PADRAO_INTEIRO.fullmatch(texto):
        raise EntradaInvalidaError(f"não é um inteiro válido: {texto!r}")
    return int(texto)


def validar_operacao_mdc(partes):
    if len(partes) != 3:
        raise EntradaInvalidaError("a operação M exige exatamente 2 números")

    a = converter_inteiro(partes[1])
    b = converter_inteiro(partes[2])

    if a < 1 or b < 1:
        raise EntradaInvalidaError("a operação M exige inteiros positivos")

    return a, b


def validar_operacao_soma(partes):
    if len(partes) != 2:
        raise EntradaInvalidaError("a operação S exige exatamente 1 número")

    n = converter_inteiro(partes[1])

    if n < 0:
        raise EntradaInvalidaError("a operação S exige inteiro não negativo")

    return n
