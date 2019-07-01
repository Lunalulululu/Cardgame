from OptimalDiscard import OptimalDiscard
from Players.Player import Player


class AIPlayer(Player):
    def do_discard(self):
        OptimalDiscard(self)

    def optimal_grouping(self):
