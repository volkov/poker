import random


seed = None


class Round:

    def __init__(self, *args,  **kwargs):
        self.hands = [Hand(arg) for arg in args]

    def stats(self):
        return "\n".join(
            f"{i + 1}: {hand.definitions}: {hand.stats()}"
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

    def deal(self, definitions):
        return [self.cards.pop() for _ in range(len(definitions))]

    def shuffle(self):
        random.shuffle(self.cards)


class Hand:

    def __init__(self, definitions):
        self.cards = None
        self.definitions = definitions

    def stats(self):
        return 0.9

    def deal(self, deck: Deck):
        self.cards = deck.deal(self.definitions)


