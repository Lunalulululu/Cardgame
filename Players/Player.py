class Player:
    def __init__(self, discard_history, num, hand):
        self.discard_history = discard_history
        self.num = num
        self.hand = hand

    def score(self, group):
        return len(self.hand)

    def discard(self, card):
        return self.hand.remove(card)

    def do_discard(self):
        raise NotImplementedError('Need to extend')
