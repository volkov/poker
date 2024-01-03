import random
from typing import List

seed = None


class Round:

    def __init__(self, *args,  **kwargs):
        self.hands = [Hand(arg) for arg in args]

    def stats(self):
        return "\n".join(
            f"{i + 1}: {','.join(hand.definitions)}: {hand.stats()}"
            for i, hand in enumerate(self.hands)
        )

    def deal(self):
        deck = Deck()
        for hand in self.hands:
            hand.deal(deck)
        return "\n".join(
            f"{i + 1}: {hand.cards[0]} {hand.cards[1]}"
            for i, hand in enumerate(self.hands)
        )


class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank}{self.suit}"


def new_deck():
    for suit in ["♠", "♣", "♥", "♦"]:
        for rank in ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]:
            yield Card(rank, suit)


class Deck:

    def __init__(self):
        if seed is not None:
            random.seed(seed)
        self.cards = list(new_deck())
        self.shuffle()

    def deal(self, definitions) -> List[Card]:
        return [self.cards.pop(), self.cards.pop()]

    def shuffle(self):
        random.shuffle(self.cards)


def parse_cards(cards: str):
    return [Card(cards[i], cards[i + 1]) for i in range(0, len(cards), 2)]


class Hand:

    def __init__(self, definition: str = None, cards=None):
        self.cards = parse_cards(cards) if isinstance(cards, str) else cards
        self.definitions = [it.strip() for it in definition.split(",")]

    def stats(self):
        return 0.9

    def match(self):
        return any(Definition(definition).match(self.cards) for definition in self.definitions)

    def deal(self, deck: Deck):
        self.cards = deck.deal(self.definitions)


def rank(r):
    return "23456789TJQKA".index(r)


class Definition:

    def __init__(self, definition):
        self.firstRank = definition[0]
        self.secondRank = definition[1]
        self.suited = 's' in definition
        self.plus = '+' in definition
        self.pairs = definition[0] == definition[1]

    def match(self, cards):
        print(self.firstRank, self.secondRank, self.suited, self.plus, self.pairs)
        print(rank(self.firstRank), rank(self.secondRank))
        print(rank(cards[0].rank), rank(cards[1].rank))
        if self.pairs and cards[0].rank != cards[1].rank:
            return False
        if self.suited and cards[0].suit != cards[1].suit:
            return False
        if self.plus:
            return (cards[0].rank == self.firstRank or cards[1].rank == self.secondRank or
                    cards[0].rank == self.secondRank or cards[1].rank == self.firstRank)
        return (rank(cards[0].rank) >= rank(self.firstRank) and rank(cards[1].rank) >= rank(self.secondRank) or
                rank(cards[0].rank) >= rank(self.secondRank) and rank(cards[1].rank) >= rank(self.firstRank))

