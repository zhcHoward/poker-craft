import Pyro4


class Client(object):

    """docstring for Client"""

    def __init__(self, arg):
        self.arg = arg

if __name__ == '__main__':
    server = Pyro4.Proxy('PYRONAME:server.pokercraft')
    if server.connection() == 0:
        print('Connected to server.')

    name = input('What is your name?').strip()
    if server.add_player(name) == 0:
        print('Successfully join the server.')
    else:
        print('Error, more than 2 players were added.')
