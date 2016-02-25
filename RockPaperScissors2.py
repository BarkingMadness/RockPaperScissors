# imports random to allow computer to choose random 'RPS'
import random


# create class
class Rockpaperscissors():

    def __init__(self):
        # initialise variables so they can be used in the methods below
        self.game_no = 0 # counts number of games played
        self.human = 0 # counts games won by human player
        self.computer = 0 # counts games won by computer
        self.user_choice = "" # holds instance of human R,P,S selection
        self.comp_choice = "" # holds random choice made by computer
        self.again = "" # holds variable to determine if user wants another game

    # allows user to enter their choice of RPS. While loop asks player for choice until 'R', 'P', or 'S' is entered.
    def user(self):
            self.user_choice = raw_input("Select (R)ock, (P)aper, or (S)cissors: ").upper()
            while self.user_choice != 'R' and self.user_choice != 'P' and self.user_choice != 'S':
                self.user_choice = raw_input("Invalid choice - Please select (R)ock, (P)aper, or (S)cissors: ").upper()
            if self.user_choice == "R":
                print ("\nYou selected: Rock")
            elif self.user_choice == "P":
                print ("\nYou selected: Paper")
            elif self.user_choice == "S":
                print ("\nYou selected: Scissors")

            return self.user_choice # returns the user selection to the program so it can be used later.

    # allows computer to select RPS randomly, from list
    def random_number(self):
        rps_list = ['R', 'P', 'S']
        self.comp_choice = random.choice(rps_list)
        print ("Computer selected: "), self.comp_choice
        return self.comp_choice # returns the computer selection to the programe so it can be used later

    # to decide the winner of the game and add 1 to the humn or computer score
    def winner(self):
        beats = {'R': 'S', 'S': 'P', 'P': 'R'}
        if beats[self.user_choice] == self.comp_choice:
            print ("Player 1 won!")
            self.human += 1
        if beats[self.comp_choice] == self.user_choice:
            print ("Player 2 won!")
            self.computer += 1
        print ("Draw!")


    # allows user to decide if they want to play another game
    def end_game(self):
        self.again = raw_input("Do you want to play again? : ")
        if self.again == "n":
            return False
        return

    # called by main function below. 
    def game_loop(self):
        while True:
            self.game_no += 1
            print "Game No.: ", self.game_no
            self.user_choice = self.user()
            self.comp_choice = self.random_number()
            self.winner()
            print "The Score is: ", self.human, "-",  self.computer
            self.again = self.end_game()
            if self.again == False:
                return

# creates an instance of RockPaperScissors called 'game'. Then calls the 'main_loop' using 'game'.
if __name__ == '__main__':
    game = Rockpaperscissors()
    game.game_loop()
