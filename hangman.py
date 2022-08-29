word = 'hangman'
trials = 7


def word_selected_dashed():
    word_selected_dashed = []
    for i in range(len(word)):
        word_selected_dashed.append('_')
    return ''.join(word_selected_dashed)


_word = word_selected_dashed()
guessed_word = list(_word)

while trials > 0:
    if ''.join(guessed_word) == word:
        print("Done")
        break

    letter = input("Guess letter: ")

    if letter in word:
        print("Correct, trial: " + str(trials))
        for i in range(len(word)):
            if list(word)[i] == letter:
                guessed_word[i] = letter
    elif letter not in word:
        trials -= 1
        print("Don't have letter " + str(letter) + ". trial: " + str(trials))

    if trials == 0:
        print("Die")
