from collections import Counter


def OptimalDiscard(player):
    """Discard a card from my player.hand according to a strategy
    based on the cards I have discarded"""

    def
    round = 11 - len(player.hand)
    translate = {'1': 1, '2': 2, '3': 3, '4': 4,
                 '5': 5, '6': 6, '7': 7, '8': 8,
                 '9': 9,
                 'J': 11, 'Q': 12, 'K': 13, '0': 10, 'A': 20}
    translate2 = {'C': 'B', 'S': 'B', 'H': 'R', 'D': 'R'}
    # take the non-Aces cards and sort them according to their values.
    non_aces = []
    for card in player.hand:
        if card not in ('AS', 'AD', 'AH', 'AC'):
            non_aces.append((translate[card[0]], translate2[card[1]]))
    non_aces = sorted(non_aces)

    if round == 1:
        # discard the card 'Q', otherwise the card that has highest value
        for card in player.hand:
            if card[0] == 'Q':
                return player.discard(card)
        return_list = [card for card in non_aces if card[0] == non_aces[-1][0]]
        value = return_list[0][0]
        for card in player.hand:
            if translate[card[0]] == value:
                return player.discard(card)

    elif 2 <= round <= 9:
        # create a freq dictionary of all my discarded cards
        my_discard_history = []
        other_player_history = []
        for list_index in range(round - 1):
            for player_index in range(4):
                if player_index == player.num:
                    (my_discard_history
                     .append(player.discard_history[list_index][player_index]))
                else:
                    (other_player_history
                     .append(player.discard_history[list_index][player_index]))

        # Prefer the value I discarded before (excluding Aces)
        # that others haven't discarded
        # otherwise, prefer the value I have discarded

        value_lst = [card[0] for card in player.hand if card in my_discard_history and
                     card[0] != 'A' and card not in other_player_history]
        second_value_list = [card[0] for card in player.hand if card in
                             my_discard_history and card[0] != 'A']
        d = Counter(value_lst)
        d2 = Counter(second_value_list)

        if 2 <= round <= 9:
            if d:
                for card in player.hand:
                    for count in range(round):
                        if card[0] == d.most_common(count + 1)[count][0]:
                            return player.discard(card)
            if d2:
                for card in player.hand:
                    for count in range(round):
                        if card[0] == d2.most_common(count + 1)[count][0]:
                            return player.discard(card)
            # if none of those values appear in my player.hand,
            # discard the card that has the highest value at the 2-8th
            # round, return the lowest possible value card at 8th round.
            return_list = []
            if round <= 8:
                return_list = [card for card in non_aces
                               if card[0] == non_aces[-1][0]]
            else:
                return_list = [card for card in non_aces
                               if card[0] == non_aces[0][0]]
            if return_list:
                value = return_list[0][0]
                for card in player.hand:
                    if translate[card[0]] == value:
                        return player.discard(card)
            # if only two Aces are left, I can only pick ace
            else:
                return player.discard(player.hand[0])
    # last_round
    else:
        return player.discard(player.hand[0])
