class Player:
    def __init__(self, hand):
        self.hand = hand

    def score(self, group):
        return len(self.hand)

    def discard(self, card):
        return self.hand.remove(card)

    def do_discard(self):
        raise NotImplementedError('Need to extend')
