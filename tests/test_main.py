import poker.round
import pytest
from poker import Round, Definition, Card, Hand


poker.round.seed = 42


# FIXME: This stats are incorrect
def test_stats():
    assert Round("AKs", "??").stats() == """
1: AKs: 0.9
2: ??: 0.9
    """.strip()


def test_deal():
    assert Round("AKs", "??").deal() == """
1: K♦ 7♠
2: K♠ 6♦
    """.strip()


def test_match_cards():
    assert Definition("AKs").match([Card("A", "♠"), Card("K", "♠")])


@pytest.mark.parametrize("definition, cards, expected", [
    ("AKs", "A♠K♠", True),
    ("AKs", "A♠K♣", False),
    ("AKs", "A♠Q♠", False),

])
def test_match_hand(definition, cards, expected):
    assert Hand(definition, cards).match() == expected
