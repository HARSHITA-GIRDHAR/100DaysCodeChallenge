import random

def select_movie():   
    movies = ["border", "queen", "dangal", "sultan", "secret superstar",
              "pathan","gangs of wasseypur","padmaavat"]
    return random.choice(movies)

def hide_movie(movie): 
    hidden = ""
    for char in movie:
        if char == ' ':
            hidden += ' '
        else:
            hidden += '*'
    return hidden

def reveal_movie(movie, guessed_letters):
    revealed = ""               
    for char in movie:
        if char == ' ':
            revealed += ' '
        elif char in guessed_letters:
            revealed += char
        else:
            revealed += '*'
    return revealed

def guess_letter(player_name):
    guess = input(f"{player_name}, guess a letter: ").strip().lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        return guess_letter(player_name)
    return guess

def main():   
    player1_score = 0 
    player2_score = 0 

    while True:
        movie_to_guess = select_movie()
        hidden_movie = hide_movie(movie_to_guess)

        print("\nPlayer 1 and Player 2, here's your chance to guess the movie!")
        attempts = 6
        guessed_letters = []

        while attempts > 0:
            print("\n" + reveal_movie(hidden_movie, guessed_letters))
            player1_guess = guess_letter("Player 1")
            player2_guess = guess_letter("Player 2")

            if player1_guess in guessed_letters:
                print("Player 1, you already guessed that letter.")
            elif player1_guess in movie_to_guess:
                print("Player 1, correct guess!")
                guessed_letters.append(player1_guess)
                hidden_movie = reveal_movie(movie_to_guess, guessed_letters)
                if hidden_movie == movie_to_guess:
                    print(f"Player 1 wins! The movie is: {movie_to_guess}.")
                    player1_score += 1
                    break
            else:
                print("Player 1, incorrect guess.")
                attempts -= 1
                print(f"Player 1, attempts left: {attempts}")

            if player2_guess in guessed_letters:
                print("Player 2, you already guessed that letter.")
            elif player2_guess in movie_to_guess:
                print("Player 2, correct guess!")
                guessed_letters.append(player2_guess)
                hidden_movie = reveal_movie(movie_to_guess, guessed_letters)
                if hidden_movie == movie_to_guess:
                    print(f"Player 2 wins! The movie is: {movie_to_guess}.")
                    player2_score += 1
                    break
            else:
                print("Player 2, incorrect guess.")
                attempts -= 1
                print(f"Player 2, attempts left: {attempts}")

        if attempts == 0 and hidden_movie != movie_to_guess:
            print(f"\nNo attempts left! The movie was: {movie_to_guess}.")

        print(f"\nPlayer 1's score: {player1_score}")
        print(f"Player 2's score: {player2_score}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
    
