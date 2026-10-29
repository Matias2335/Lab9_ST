import pytest
from classificacao import classificar_aluno


def test_aprovado():
    assert classificar_aluno(8.0, 80) == "Aprovado"


def test_reprovado():
    assert classificar_aluno(3.0, 90) == "Reprovado"


@pytest.mark.parametrize("media, presenca, esperado", [
    (0, 80, "Reprovado"),               # menor média válida
    (10, 80, "Aprovado"),               # maior média válida
    (7.0, 80, "Aprovado"),              # fronteira Aprovado
    (6.9, 80, "Recuperacao"),
    (5.0, 80, "Recuperacao"),           # fronteira Recuperacao
    (4.9, 80, "Reprovado"),
    (8.0, 75, "Aprovado"),              # menor presença que não reprova por falta
    (8.0, 74, "Reprovado por falta"),
    (8.0, 0, "Reprovado por falta"),    # menor presença válida
    (8.0, 100, "Aprovado"),             # maior presença válida
])
def test_classificacao_nas_fronteiras(media, presenca, esperado):
    assert classificar_aluno(media, presenca) == esperado


@pytest.mark.parametrize("media", [-1, -0.1, 10.1, 11])
def test_media_invalida(media):
    with pytest.raises(ValueError, match="^Media invalida$"):
        classificar_aluno(media, 80)


@pytest.mark.parametrize("presenca", [-1, -0.1, 100.1, 101])
def test_presenca_invalida(presenca):
    with pytest.raises(ValueError, match="^Presenca invalida$"):
        classificar_aluno(8.0, presenca)