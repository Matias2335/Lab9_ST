import pytest
from parcelamento import parcela


@pytest.mark.parametrize("n", [0, 13])
def test_parcelas_invalidas(n):
    with pytest.raises(ValueError, match="^parcelas invalidas$"):
        parcela(100, n)


@pytest.mark.parametrize("valor, n, esperado", [
    (100, 1, 100.0),      # menor n válido
    (100, 2, 50.0),       # sem juros
    (100, 3, 33.33),      # última sem juros
    (100, 4, 25.5),       # primeira com juros: 100 * 1.02 / 4
    (100, 12, 9.83),      # maior n válido: 100 * 1.18 / 12
])
def test_parcela_nas_fronteiras(valor, n, esperado):
    assert parcela(valor, n) == esperado