import pytest
from temperaturas import maior, dia_do_maior


def test_maior_varias():
    assert maior([21, 25, 19, 30, 22]) == 30


def test_maior_um_elemento():
    assert maior([18]) == 18


def test_maior_dois():
    assert maior([30, 21]) == 30


def test_maior_maximo_na_posicao_1():
    assert maior([10, 40, 20]) == 40


def test_maior_vazia():
    with pytest.raises(ValueError, match="^lista vazia$"):
        maior([])


def test_dia_do_maior_varias():
    assert dia_do_maior([21, 25, 19, 30, 22]) == 3


def test_dia_do_maior_um_elemento():
    assert dia_do_maior([18]) == 0


def test_dia_do_maior_dois():
    assert dia_do_maior([30, 21]) == 0


def test_dia_do_maior_maximo_na_posicao_1():
    assert dia_do_maior([10, 40, 20]) == 1


def test_dia_do_maior_empate_devolve_o_primeiro():
    assert dia_do_maior([30, 21, 30]) == 0


def test_dia_do_maior_vazia():
    with pytest.raises(ValueError, match="^lista vazia$"):
        dia_do_maior([])