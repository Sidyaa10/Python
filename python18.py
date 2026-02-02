#Building a guessing game

secret_word ="Apollo"

guess =""
guess_count= 0
guess_limit=3
out_of_guesses= False


while guess != secret_word and not(out_of_guesses):
    if guess_count<guess_limit:
     guess = input("Enter your guess(Hint its a God): ")
     guess_count=guess_count+1
    else:
        out_of_guesses=True

if out_of_guesses:
    print("You are out of guesses, Better luck next time")
else:
   print("You Win, You guessed the correct God. May he bless you with good fortune.")
