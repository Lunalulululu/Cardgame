
SUIT_TO_COLOUR = dict(zip('HDCS', 'RRBB')) # {'H':'R'}
VALUE_STRING_TO_VALUE = dict(zip('A23456780JQK', range(1, 14))) #{'A': 1, '2': 2}

VALUE_TO_VALUE_STRING = {v: k for k, v in VALUE_STRING_TO_VALUE.items()} #{1: 'A', 2:'2'}


class Card:
    def __init__(self, card_string):
        if isinstance(card_string, tuple):
            card_string = VALUE_TO_VALUE_STRING[card_string[0]] + card_string[1]
        self.value_str = card_string[0]
        self.value = VALUE_STRING_TO_VALUE[self.value_str]
        self.suit = card_string[1]
        self.colour = SUIT_TO_COLOUR[self.suit]
        self.inv_colour = 'R' if self.colour == 'B' else 'B'
        self.orphan_value = -20 if self.is_ace() else -self.value

    def __eq__(self, other):
        return self.value_str == other.value_str and self.suit == other.suit

    def __repr__(self):
        return f'Card(\' {self.value_str}{self.suit}\')'

    def __str__(self):
        return f'{self.value_str}{self.suit}'
    def is_ace(self):
        return self.value_str == 'A'
    def is_black(self):
        return self.value_str == 'B'
    def is_red(self):
        return