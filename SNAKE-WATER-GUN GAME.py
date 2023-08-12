import playsound

def winning_music():
    """
        Plays the winning music.
    """
    try:
        playsound.playsound("PROJECT FILES/MP3/winning_sound.mp3")
    except Exception as e:
        print(e)
        
def losing_music():
    """
    Plays the losing music.
    """
    try:
        playsound.playsound("PROJECT FILES/MP3/losing_sound.mp3")
    except Exception as e:
        print(e)

def tie_music():
    """
    Plays the tie music.
    """
    try:
        playsound.playsound("PROJECT FILES/MP3/tie_sound.mp3")
    except Exception as e:
        print(e)

def game_over_music():
    """
    Plays the Game Over Music.
    """
    try:
        playsound.playsound("PROJECT FILES/MP3/game_over_sound.mp3")
    except Exception as e:
        print(e)
    exit()

if __name__ == '__main__':

    lst = ["S", "W", "G"]
    dic = {"S": "SNAKE", "W": "WATER", "G": "GUN"}

    while True:
        name = input("\nEnter your name : ").capitalize()
        if not name.__str__():
            print("Invalid input! Please enter your name...")
            continue

        print(f"\nHi {name}!\nThis is a very quick and Easy Snake Water Gun game which is very much similar to stone paper scissor.\nThere are only 10 guesses in this Game to win. If you have more points than the computer then 'You will Win' and if less then 'Computer will Win' or if equal then the game will Tie")

        guesses = 10
        user_points = 0
        computer_points = 0

        attempts = 1
        while attempts <= 10:

            import random
            print(f"\nROUND {attempts}")
            print("Press s for SNAKE \nPress w for WATER \nPress g for GUN")
            user_choice = input("Enter your choice : ").capitalize()
            computer_choice = random.choice(lst).capitalize()

            if user_choice == computer_choice:

                print(f"\nRound {attempts} : Tie!\nNobody gets point.")
                print(f"You chose {dic[user_choice]} and the computer also chose {dic[computer_choice]}.")

                print(f"\n{name} points : {user_points}")

                print(f"Computer points : {computer_points}")

                guesses = guesses - 1
                print(f"\nNo. of guesses left : %d" %guesses)

                tie_music()

                attempts = attempts + 1
                continue

            elif (user_choice == "S" and computer_choice == "W") or (user_choice == "G" and computer_choice == "S") or (user_choice == "W" and computer_choice == "G"):

                print(f"\nRound {attempts} : You won this round!\nYou get 1 point.")
                print(f"You chose {dic[user_choice]} and the computer chose {dic[computer_choice]}.")

                if user_choice == "S" and computer_choice == "W":
                    print("The snake drank water.")

                elif user_choice == "G" and computer_choice == "S":
                    print("The snake shot dead by the gun.")

                elif user_choice == "W" and computer_choice == "G":
                    print("The gun sank into water.")

                user_points = user_points + 1
                print(f"\n{name} points : {user_points}")

                print(f"Computer points : {computer_points}")

                guesses = guesses - 1
                print(f"\nNo. of guesses left : %d" %guesses)

                winning_music()

                attempts = attempts + 1
                continue

            elif (user_choice == "W" and computer_choice == "S") or (user_choice == "S" and computer_choice == "G") or (user_choice == "G" and computer_choice == "W"):

                print(f"\nRound {attempts} : You lost this round and the Computer wins!\nComputer gets 1 point.")
                print(f"You chose {dic[user_choice]} and the computer chose {dic[computer_choice]}.")

                if user_choice == "W" and computer_choice == "S":
                    print("The snake drank the water.")

                elif user_choice == "S" and computer_choice == "G":
                    print("The snake shot dead by the gun.")

                elif user_choice == "G" and computer_choice == "W":
                    print("The gun sank into water.")

                print(f"\n{name} points : {user_points}")

                computer_points = computer_points + 1
                print(f"Computer points : {computer_points}")

                guesses = guesses - 1
                print(f"\nNo. of guesses left : %d" %guesses)

                losing_music()

                attempts = attempts + 1
                continue

            else:
                print("Invalid input!! Please make a right choice...")
                continue

        if user_points > computer_points:
            print(f"\nCongratulations {name}, You Win!")
            print(f"Your Points : {user_points}")
            print(f"Computer Points : {computer_points}")
            winning_music()

        elif computer_points > user_points:
            print(f"\nOh! You lose and the Computer wins!")
            print(f"Computer Points : {computer_points}")
            print(f"Your Points : {user_points}")
            losing_music()

        elif user_points == computer_points:
            print("\nGame Tie!")
            print(f"Your Points : {user_points}")
            print(f"Computer Points : {computer_points}")
            tie_music()

        if attempts > 10:
            print("\nGame Over!")
            game_over_music()
            exit()