# Функция для генерации хода компьютера
def computer(counter):
    moves = ["камень", "ножницы", "бумага"]
    return moves[counter % 3]  # Используем счётчик для выбора хода

# Основная игра
def play():
    player_score = 0
    computer_score = 0
    counter = 0  # Счётчик для генерации хода компьютера

    print("Игра 'Камень-Ножницы-Бумага'. Играем до 5 очков!")

    while player_score < 5 and computer_score < 5:
        player_choice = input("Ваш ход ('камень', 'ножницы', 'бумага'): ").strip().lower()
        computer_choice = computer(counter)
        
        print("Компьютер выбрал:", computer_choice)

        # Проверка результатов
        if player_choice == computer_choice:
            print("Ничья!")
        elif (player_choice == "камень" and computer_choice == "ножницы") or \
             (player_choice == "ножницы" and computer_choice == "бумага") or \
             (player_choice == "бумага" and computer_choice == "камень"):
            player_score += 1
            print("Вы выиграли раунд!")
        else:
            computer_score += 1
            print("Компьютер выиграл раунд!")

        print("Счет: Вы", player_score, ":", computer_score, "Компьютер")
        counter += 1  # Увеличиваем счётчик после каждого раунда

    if player_score == 5:
        print("Вы выиграли игру!")
    else:
        print("Компьютер выиграл игру!")

# Запуск игры
play()
