from random import randint

class Game():

    def __init__(self):
            
        Game.Attempts(self)

    def GetUserNumber(self):

        try:
            user_number = int(input("\nEnter a number between 0 and 100, and try to get it right in 10 attempts: "))
            return user_number
        except:
            print("\nInvalid value!! Please try again!")
            Game.GetUserNumber(self)

    def Valid_Attempts(self, user_number, current_attempts, mysterious_number):

        if user_number == mysterious_number:
            print(f'Congratulations! You got it right with {current_attempts} attempts :)')
        
        elif user_number < mysterious_number:
            print("The mysterious number is bigger!")
        
        elif user_number > mysterious_number:
            print("The mysterious number is smaller!")

    def Attempts(self):

        user_number = 0
        mysterious_number = randint(0, 100)

        max_attempts = 10
        current_attempts = 1

        while current_attempts <= max_attempts and user_number != mysterious_number:

            user_number = Game.GetUserNumber(self)
            Game.Valid_Attempts(self, user_number, current_attempts, mysterious_number)
            current_attempts += 1

        if current_attempts == 10:
            print("You lose!!")
            Game()


if __name__ == "__main__":

    Game()