from hello import transferLbtoKg


def test_transferLbtoKg():
    assert transferLbtoKg(10) == format(4.6, ".2f")
