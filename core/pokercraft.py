import json
import random


class PokerCraft(object):

    """docstring for PokerCraft"""

    def __init__(self, players):
        self.players = players
        with open('../res/soldier.json') as soldier, \
                open('../res/hero.json') as hero:
            self.soldiers = json.load(soldier)
            self.heros = json.load(hero)

    def init_battle_field(self):
        # store data of battle field, ie, hp and position of each poker
        self.bf = [
            {'name': self.players[0].name,
             'base': self.players[0].base,
             'bf':[[], []]
             },
            {'name': self.players[1].name,
             'base': self.players[1].base,
             'bf':[[], []]
             }]

    def shuffle(self):
        random.shuffle(self.soldiers)
        random.shuffle(self.heros)

    def attack(self, attacker, victim):
        victim.hp -= attacker.atk
        return attacker, victim

    def battle_field(self):
        pass

    def event_handle(self, event):
        pass


def main():
    pokercarft = PokerCraft()
    pokercarft.shuffle()
    print(pokercarft.soldiers, pokercarft.heros, sep='\n')

if __name__ == '__main__':
    main()
