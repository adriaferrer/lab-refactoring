from random import choice


def deal_cards(deck):
    """
    Randomly chooses two cards of the deck for the player and for the dealer.
    :param deck:
    :return: The hand of the player and the dealer. List of lists of 2 elements (str)
    """
    player_hand = [choice(deck) for x in range(2)]
    dealer_hand = [choice(deck) for x in range(2)]
    return player_hand, dealer_hand