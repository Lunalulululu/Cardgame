class Player:
    def __init__(self, discard_history, num, hand):
        self.discard_history = discard_history
        self.num = num
        self.hand = hand
        self.final_group = None

    def group(self, group):
        self.final_group = group

    def score(self, group):
        return len(self.hand)

    def discard(self, card):
        round = 11 - len(self.hand)
        if self.num == 0:
            self.discard_history[round - 1] = [card]
        else:
            self.discard_history[round - 1].append(card)
        self.hand.remove(card)

    def do_discard(self):
        raise NotImplementedError('Need to extend')

    def last_player_history(self):
        k
