from Players.Player import Player


class AIPlayer(Player):
    def do_discard(self):
        self.discard('9C')

    def optimal_grouping(self):
        return self.hand
