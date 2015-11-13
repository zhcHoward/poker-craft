import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from core import player, pokercraft


class Interface(object):

    """docstring for Interface"""

    def __init__(self, players):
        self.players = players

    def display(self, player):
        print('Name:\t|')
        print('========================================')
        print('Base:\t|')
        print('========================================')
        print('\t|')
        print('Battle\t|')
        print('\t|================================')
        print('Field:\t|')
        print('\t|')
        print('========================================')
        print('\t|')
        print('Battle\t|')
        print('\t|================================')
        print('Field:\t|')
        print('\t|')
        print('========================================')
        print('Base:\t|')
        print('========================================')
        print('Name:\t|')


def main():
    players = [player.Player('zhc'), player.Player('abc')]
    ui = Interface(players)
    ui.display('zhc')

if __name__ == '__main__':
    main()
