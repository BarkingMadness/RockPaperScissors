import random
# create class
class Rockpaperscissors():

    def __init__(self):
        # initialise variables so they can be used in the methods below
        self.game_no = 0 # counts number of games played
        self.human = 0 # counts game won by human player
        self.computer = 0 # counts games won by computer
        self.user_choice = "" # holds instance of human R,P,S selection
        self.comp_choice = "" # holds random choice made by computer
        self.again = "" # holds variable to determine if user wants another game

    # allows user to enter their choice of RPS
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

            return self.user_choice

    # allows computer to select RPS randomly, from list
    def random_number(self):
        rps_list = ['Rock', 'Paper', 'Scissors']
        self.comp_choice = random.choice(rps_list)
        print ("Computer selected: "), self.comp_choice
        return self.comp_choice

    # to decide winner of game
    def winner(self):
        if self.user_choice == 'R' and self.comp_choice == 'Paper':
            print "Paper covers Rock - You win!"
            self.human += 1
        elif self.user_choice == 'R' and self.comp_choice == 'Scissors':
            print "Scissors blunts paper = You lose!"
            self.computer += 1
        elif self.user_choice == 'P' and self.comp_choice == 'Rock':
            print "Paper covers rock - You win!"
            self.human += 1
        elif self.user_choice == 'P' and self.comp_choice == 'Scissors':
            print "Scissors cuts paper - You lose!"
            self.computer += 1
        elif self.user_choice == 'S' and self.comp_choice == 'Rock':
            print "Rock blunts Scissors - You lose!"
            self.computer += 1
        elif self.user_choice == 'S' and self.comp_choice == 'Paper':
            print "Scissors cuts Paper - You Win!"
            self.human += 1
        else:
            print "It's a tie!"
        return self.human, self.computer

    # allows user to decide if they want to play another game
    def end_game(self):
        self.again = raw_input("Do you want to play again? : ")
        if self.again == "n":
            return False
        return

    # called by main function
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

# creates and instance of RockPaperScissors and then runs the programme
if __name__ == '__main__':
    game = Rockpaperscissors()
    game.game_loop()
