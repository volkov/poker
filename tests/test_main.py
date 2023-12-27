from poker import Round


def test_sample():
    assert Round("AKs", "??").stats() == """
1: AKs: 0.9
2: ??: 0.9
    """.strip()
