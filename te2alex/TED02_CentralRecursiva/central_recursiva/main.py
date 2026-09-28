

import sys

from central_recursiva.excecoes import EntradaInvalidaError
from central_recursiva.processador import Resumo, processar_linha
from central_recursiva.validador import converter_inteiro


def ler_quantidade(linha):
    quantidade = converter_inteiro(linha.strip())
    if quantidade < 0:
        raise EntradaInvalidaError("a quantidade de operações não pode ser negativa")
    return quantidade


def main():
    mostrar_resumo = "--resumo" in sys.argv[1:]
    resumo = Resumo()

    try:
        linhas = [l for l in sys.stdin.read().splitlines() if l.strip()]
        if not linhas:
            return

        try:
            quantidade = ler_quantidade(linhas[0])
        except EntradaInvalidaError as erro:
            print(erro.mensagem_saida)
            return

        for linha in linhas[1:quantidade + 1]:
            resultado = processar_linha(linha, resumo)
            if resultado is not None:
                print(resultado)

    finally:
        sys.stdout.flush()
        if mostrar_resumo:
            print(resumo, file=sys.stderr)


if __name__ == "__main__":
    main()
