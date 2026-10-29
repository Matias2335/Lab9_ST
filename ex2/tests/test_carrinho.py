from carrinho import total_com_desconto


def test_total_exato():
    assert total_com_desconto([10, 20, 30, 40, 50]) == 141.0


def test_preco_com_centavos_exige_arredondamento():
    # 60 + 12.34 * 0.9 = 71.106 -> 71.11 (duas casas)
    assert total_com_desconto([10, 20, 30, 12.34]) == 71.11