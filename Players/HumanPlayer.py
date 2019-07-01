from Players.Player import Player


class HumanPlayer(Player):
    def do_discard(self):
        card = input('Enter card to discard')
        self.discard(card)
