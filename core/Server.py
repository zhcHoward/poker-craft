from __future__ import division, print_function, unicode_literals
import Pyro4
import sys
import os
import time
import player
import pokercraft
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))


class Server(object):

    def __init__(self):
        self.players = []

    def connection(self):
        return 0

    def add_player(self, player_name):
        if len(self.players) < 2:
            self.players.append(player.Player(player_name))
            print('{} successfully join the server.'.format(player_name))
            return 0
        else:
            print('{} fail to join the server.'.format(player_name))
            return 1

    # def num_players(self):
    #     return len(self.players)

    def game(self):
        while True:
            if len(self.players) == 2:
                break
            else:
                time.sleep(0.5)
        pc = pokercraft.PokerCraft(self.players)
        pc.init_battle_field()
        pc.shuffle()


def main():
    server = Server()
    Pyro4.Daemon.serveSimple({server: 'server.pokercraft'},
                             ns=True)


if __name__ == '__main__':
    main()

# ns = Pyro4.locateNS()       # find the name server
# register the greeting maker as a Pyro object
# uri = daemon.register(Server)
# register the object with a name in the name server
# ns.register("pokercraft", uri)

# print("Ready.")
# daemon.requestLoop()
