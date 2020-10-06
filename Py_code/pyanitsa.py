class Card:
        suits = ['пикей','червей','бубей', 'треф']

        values = ['2', '3', '4', '5', '6', '7',
                  '8', '9', '10', 'валет', 'дама','король',
                  'туз']

        def __init__(self, v,s):
                """suit и value - целые числа"""
                self.value = v
                self.suit = s

        def __lt__(self, c2):
                return ((self.value < c2.value) or ((self.value
                        == c2.value) and (self.suit < c2.suit)))
        def __gt__(self, c2):
                return c2 < self

        def __repr__(self):
                v = self.values[self.value] + ' ' + self.suits[self.suit]
                return v

from random import shuffle

class Deck:
        def __init__(self):
                self.cards = []
                for i in range(0, 13):
                        for j in range(4):
                                self.cards.append(Card(i,j))
                shuffle(self.cards)
        def rm_card(self):
                if len(self.cards) == 0:
                        return
                return self.cards.pop()

class Player:
        def __init__(self, name):
                self.wins = 0
                self.card = None
                self.name = name

class Game:
        def __init__(self):
                name1 = input("Введите имя игрока 1: ")
                name2 = input("Введите имя игрока 2: ")
                self.deck = Deck()
                self.p1 = Player(name1)
                self.p2 = Player(name2)
        def wins(self, winner):
                w = "{} забирает карты"
                w = w.format(winner)
                print(w)
        def draw(self, p1n, p1c, p2n, p2c):
                d = "{} кладет {}, а {} кладет {}"
                d = d.format(p1n, p1c, p2n, p2c)
                print(d)        
        def play_game(self):
                cards = self.deck.cards
                print("Поехали!")
                while len(cards) >= 2:
                        m = "Нажмите Х для выхода. Нажмите любую другую клавищу для начала игры\n"
                        response = input(m)
                        if response.upper() == 'Х' or response.upper() == 'X':
                                break
                        p1c = self.deck.rm_card()
                        p2c = self.deck.rm_card()
                        p1n = self.p1.name
                        p2n = self.p2.name
                        self.draw(p1n, p1c, p2n, p2c)
                        if p1c > p2c:
                                self.p1.wins += 1
                                self.wins(self.p1.name)
                        else:
                                self.p2.wins += 1
                                self.wins(self.p2.name)

                win = self.winner(self.p1, self.p2)

                print("Игра окончена. {} выиграл!".format(win))
        def winner(self, p1, p2):
                if p1.wins > p2.wins:
                        return p1.name
                if p1.wins < p2.wins:
                        return p2.name
                return "Ничья!"
game = Game()
game.play_game()
card1 = Card(10,2)
card2 = Card(11,3)
print(card1 < card2)
print(card1 > card2)
print(card2 < card1)
print(card2 > card1)
print(card1)
print(card2)

deck = Deck()
for card in deck.cards:
        print(card)
