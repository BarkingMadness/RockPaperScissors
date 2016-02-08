import random

#just one class
class Rockpaperscissors():

    def __init__(self):
        
        #initialise variables
        self.game_no = 1 #
        self.human = 0
        self.computer = 0
        self.user_choice = ""
        self.comp_choice = ""
        self.again = ""

    def user(self):
        self.user_choice = raw_input("Select (R)ock, (P)aper, or (S)cissors: ").upper()
        while self.user_choice != 'R' and self.user_choice != 'P' and self.user_choice != 'S':
            print("Invalid choice. Please enter R, P or S")
        if self.user_choice == "R":
            print ("\nYou selected: Rock")
        elif self.user_choice == "P":
            print ("\nYou selected: Paper")
        elif self.user_choice == "S":
            print ("\nYou selected: Scissors")
        else:
            print ("That's not a correct entry")
        return self.user_choice

    def random_number(self):
        rps_list = ['Rock', 'Paper', 'Scissors']
        self.comp_choice = random.choice(rps_list)
        print "Computer selected: ", self.comp_choice
        return self.comp_choice

    def end_game(self):
        self.again = raw_input("Do you want to play again?")
        if self.again == "n":
            return False
        return

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

    def game_loop(self):
        while True:
            self.user_choice = self.user()
            self.comp_choice = self.random_number()
            self.winner()
            print "Game No.: ", self.game_no
            print "The Score is: ", self.human, self.computer
            if self.end_game == False:
                self.game_no = self.game_no += 1
                return

if __name__ == '__main__':
    game1 = Rockpaperscissors()
    game1.game_loop()

