print(
    "Welcome to 'Guess the Number' Game. In this Game, You have given only 5 GUESSES in which the number(GUESS THE NUMBER FROM 0 to 50) entered by you should be relating to the number that is hidden in this game algo which you have to guess to win this game. And, if you have used, all your 5 guessings, but didn't find the right number. Then, YOU WILL LOSE THE GAME.")

g = 5
i = 1
while i <= 5:
    num = int(input("\nEnter the number : "))
    i = i + 1
    g = g - 1

    if num > 100:
        print("You are very far from the number !!")
    elif 50 <= num <= 100:
        print("You are far from the number !!")
    elif 21 <= num <= 50:
        print("Decrease the number !!")
    elif 10 <= num < 15:
        print("You are near to the number !!")
    elif 15 <= num <= 17 or 19 <= num <= 20:
        print("You are very near to the number !!")
    elif 0 <= num <= 10:
        print("Increase the number !!")
    elif num == 18:
        print("YOU WIN! You have entered a right number in", i - 1, "guess.")
        break

    print("You have only", g, "guessing left")
    if g == 0:
        print("GAME OVER!! You lose the game.")