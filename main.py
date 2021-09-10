import random
import list

print("Hangman Game")
input("Press Enter to play")
word = random.choice(list.words)
print("_________\n"
      "|       |\n"
      "|       O\n"
      "|\n"
      "|\n"
      "|__")
blank = "_ "
blanks = blank*len(word)
print(blanks)
bool = False
wrong = 0

while not bool:
    guess = input("Guess a letter: ")
    index = int(word.find(guess))
    b_list = blanks.split()
    num = 0

    for c in b_list:
        if word[num] == guess:
            b_list[num] = guess
        num += 1
    blanks = " ".join(b_list)
    print(blanks)

    if guess not in word:
        wrong += 1
        if wrong == 1:
            print("_________\n"
                  "|       |\n"
                  "|       O\n"
                  "|       |\n"
                  "|\n"
                  "|__")
        if wrong == 2:
            print("_________\n"
                  "|       |\n"
                  "|       O\n"
                  "|      /|\n"
                  "|\n"
                  "|__")
        if wrong == 3:
            print("_________\n"
                  "|       |\n"
                  "|       O\n"
                  "|      /|\ \n"
                  "|\n"
                  "|__")
        if wrong == 4:
            print("_________\n"
                  "|       |\n"
                  "|       O\n"
                  "|      /|\ \n"
                  "|      /\n"
                  "|__")
        if wrong == 5:
            print("_________\n"
                  "|       |\n"
                  "|       O\n"
                  "|      /|\ \n"
                  "|      / \ \n"
                  "|__")
            bool = True
            print("You Lose\n"
                  "The word was " + word)

    if "_" not in blanks:
        bool = True
        print("You win!")