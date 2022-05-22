import random


def beats(one, two):
    return (
        (one == "rock" and two == "scissors")
        or (one == "scissors" and two == "paper")
        or (one == "paper" and two == "rock")
    )


class Player:
    moves = ["rock", "paper", "scissors"]

    def move(self):
        return "rock"

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(self.moves)


class CyclePlayer(Player):
    def __init__(self):
        self.my_move = None

    def move(self):
        if self.my_move is None:
            return "rock"
        elif self.my_move == self.moves[0]:
            return self.moves[1]
        elif self.my_move == self.moves[1]:
            return self.moves[2]
        else:
            return self.moves[0]

    def learn(self, my_move, their_move):
        self.my_move = my_move


class ReflectPlayer(Player):
    def __init__(self):
        self.their_move = "rock"

    def move(self):
        return self.their_move

    def learn(self, my_move, their_move):
        self.their_move = their_move


class HumanPlayer(Player):
    def move(self):
        while True:
            user = input("Choose Rock, Paper or Scissors: ").lower()
            if user in self.moves:
                return user
            else:
                print("Don't understand. Try again.")


class Game:
    def __init__(self, HumanPlayer, RandomPlayer):
        self.HumanPlayer = HumanPlayer
        self.RandomPlayer = RandomPlayer

    playerscore_p1 = 0
    playerscore_p2 = 0

    def play_round(self):
        playermove1 = self.HumanPlayer.move()
        playermove2 = self.RandomPlayer.move()
        print(f"Player 1: {playermove1}  Player 2: {playermove2}")

        if beats(playermove1, playermove2):
            self.playerscore_p1 += 1
            print("You win!")
        elif playermove1 == playermove2:
            self.playerscore_p1 = self.playerscore_p1
            self.playerscore_p2 = self.playerscore_p2
            print("It's a tie!")
        else:
            self.playerscore_p2 += 1
            print("Computer wins!")

        print(f"Player 1:({self.playerscore_p1}) "
              f"Player 2:({self.playerscore_p2})")

        self.HumanPlayer.learn(playermove1, playermove2)
        self.RandomPlayer.learn(playermove2, playermove1)

    def play_game(self):
        print("Let's play 5 rounds of rock, paper, scissors!")
        for round in range(1, 6):
            print(f"Round {round}:")
            self.play_round()
        print(f" Final Score: P1({self.playerscore_p1})"
              f" P2({self.playerscore_p2})")
        if self.playerscore_p1 == self.playerscore_p2:
            print("A tie game. No one wins.")
        elif self.playerscore_p1 > self.playerscore_p2:
            print("P1 wins!")
        else:
            print("P2 wins!")

        print("Game over!")


if __name__ == "__main__":
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()
