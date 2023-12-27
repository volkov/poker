class Round:

    def __init__(self, *args, **kwargs):
        self.hands = [Hand(arg) for arg in args]

    def stats(self):
        return "\n".join(
            f"{i + 1}: {hand.cards}: {hand.stats()}"
            for i, hand in enumerate(self.hands)
        )


class Hand:

    def __init__(self, cards):
        self.cards = cards

    def stats(self):
        return 0.9
