import random

def choose_word():
    word = ['стол', 'стул', 'кровать', 'диван', 'кресло']
    return random.choice(word)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 6

    print('Здравствуйте, сегодня мы загадываем слова из темы Мебель. Отгадайте слово - это предмет интерьера. Желаем удачи!')
    print(display_word(word_to_guess, guessed_letters))

    while attempts > 0 and "_" in display_word(word_to_guess, guessed_letters):
        user_guess = input("Введите букву: ").lower()

        if user_guess in guessed_letters:
            print("Попробуйте еще раз")
            continue

        guessed_letters.append(user_guess)

        if user_guess in word_to_guess:
            print("Отличная попытка!")
        else:
            print("Неверная попытка!")
            attempts += 1

        print(display_word(word_to_guess, guessed_letters))

    if "_" not in display_word(word_to_guess, guessed_letters):
        print("Поздравляем! Вы угадали слово")
    else:
        print("Извините все попытки закончились. Вы не угадали. Это слово: ", word_to_guess)

hangman()


