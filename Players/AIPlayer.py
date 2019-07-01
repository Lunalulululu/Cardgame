from OptimalDiscard import OptimalDiscard
from OptimalGrouping import OptimalGrouping
from Players.Player import Player


class AIPlayer(Player):
    def do_discard(self):
        OptimalDiscard(self)

    def do_grouping(self):
        if len(self.hand) == 10:
            OptimalGrouping(self)
