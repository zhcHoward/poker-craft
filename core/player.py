class Player(object):

    """docstring for Player"""

    def __init__(self, name, base=[5, 5, 5], cards=[]):
        self.name = name
        self.base = base
        self.cards = cards

    def get_cards(self, cards):
        for each_card in cards:
            self.cards.append(each_card)

    def lose_cards(self, cards):
        for each_card in cards:
            self.cards.remove(each_card)

    def attacked(self, base_num, damage):
        self.base[base_num] -= damage
