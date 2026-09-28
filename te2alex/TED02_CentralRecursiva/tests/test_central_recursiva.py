"""Testes automatizados. Execute na raiz do projeto: python -m unittest -v"""

import io
import math
import unittest
from contextlib import redirect_stdout
from unittest import mock

from central_recursiva import main as modulo_main
from central_recursiva.algoritmos import mdc, soma_digitos
from central_recursiva.excecoes import (
    CentralRecursivaError,
    EntradaInvalidaError,
    OperacaoInvalidaError,
)
from central_recursiva.processador import Resumo, processar_linha
from central_recursiva.validador import (
    converter_inteiro,
    validar_operacao_mdc,
    validar_operacao_soma,
)


class TestAlgoritmos(unittest.TestCase):
    def test_mdc(self):
        self.assertEqual(mdc(48, 18), 6)
        self.assertEqual(mdc(17, 19), 1)
        self.assertEqual(mdc(100, 25), 25)
        self.assertEqual(mdc(7, 7), 7)
        self.assertEqual(mdc(10**9, 1), 1)

    def test_mdc_confere_com_math_gcd(self):
        for a in range(1, 60):
            for b in range(1, 60):
                self.assertEqual(mdc(a, b), math.gcd(a, b))

    def test_soma_digitos(self):
        self.assertEqual(soma_digitos(0), 0)
        self.assertEqual(soma_digitos(9), 9)
        self.assertEqual(soma_digitos(2026), 10)
        self.assertEqual(soma_digitos(12345), 15)
        self.assertEqual(soma_digitos(10**18), 1)
        self.assertEqual(soma_digitos(999_999_999_999_999_999), 162)


class TestExcecoes(unittest.TestCase):
    def test_heranca(self):
        self.assertTrue(issubclass(CentralRecursivaError, Exception))
        self.assertTrue(issubclass(OperacaoInvalidaError, CentralRecursivaError))
        self.assertTrue(issubclass(EntradaInvalidaError, CentralRecursivaError))


class TestValidador(unittest.TestCase):
    def test_converter_inteiro_invalido(self):
        for texto in ("abc", "1.5", "+5", "1_0", "", "--3", "٣"):
            with self.assertRaises(EntradaInvalidaError):
                converter_inteiro(texto)

    def test_mdc_invalido(self):
        for partes in (["M"], ["M", "1"], ["M", "1", "2", "3"],
                       ["M", "0", "5"], ["M", "-1", "5"], ["M", "a", "5"]):
            with self.assertRaises(EntradaInvalidaError):
                validar_operacao_mdc(partes)

    def test_soma_invalida(self):
        for partes in (["S"], ["S", "1", "2"], ["S", "-1"], ["S", "x"]):
            with self.assertRaises(EntradaInvalidaError):
                validar_operacao_soma(partes)

    def test_validos(self):
        self.assertEqual(validar_operacao_mdc(["M", "48", "18"]), (48, 18))
        self.assertEqual(validar_operacao_soma(["S", "0"]), 0)


class TestProcessador(unittest.TestCase):
    def test_linhas(self):
        casos = {
            "M 48 18": "MDC = 6",
            "S 2026": "SOMA = 10",
            "S 0": "SOMA = 0",
            "M 0 25": "ERRO: EntradaInvalida",
            "S -50": "ERRO: EntradaInvalida",
            "M 5": "ERRO: EntradaInvalida",
            "X 10 20": "ERRO: OperacaoInvalida",
            "m 10 20": "ERRO: OperacaoInvalida",
        }
        for linha, esperado in casos.items():
            self.assertEqual(processar_linha(linha), esperado, linha)

    def test_linha_em_branco(self):
        self.assertIsNone(processar_linha("   "))

    def test_finally_atualiza_resumo(self):
        resumo = Resumo()
        processar_linha("M 48 18", resumo)
        processar_linha("X 1 2", resumo)
        processar_linha("S -1", resumo)
        self.assertEqual((resumo.processadas, resumo.com_erro), (3, 2))


class TestExemplosDoEnunciado(unittest.TestCase):
    def executar(self, entrada):
        saida = io.StringIO()
        with mock.patch("sys.stdin", io.StringIO(entrada)), \
                mock.patch("sys.argv", ["executar.py"]), \
                redirect_stdout(saida):
            modulo_main.main()
        return saida.getvalue()

    def test_exemplos(self):
        for n in (1, 2):
            with open(f"exemplos/entrada{n}.txt", encoding="utf-8") as f:
                entrada = f.read()
            with open(f"exemplos/saida{n}.txt", encoding="utf-8") as f:
                esperado = f.read()
            self.assertEqual(self.executar(entrada), esperado)

    def test_q_invalido(self):
        self.assertEqual(self.executar("abc\nM 1 2\n"), "ERRO: EntradaInvalida\n")


if __name__ == "__main__":
    unittest.main()
