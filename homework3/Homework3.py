def calculate_age():
    # Запрашиваем дату рождения
    birth_date = input("Введите дату рождения (дд.мм.гггг): ")
    day, month, year = map(int, birth_date.split('.'))

    # Запрашиваем сегодняшнюю дату
    current_date = input("Введите сегодняшнюю дату (дд.мм.гггг): ")
    current_day, current_month, current_year = map(int, current_date.split('.'))

    # Вычисляем возраст
    age = current_year - year

    # Проверяем, был ли день рождения в этом году
    if (current_month < month) or (current_month == month and current_day < day):
        age -= 1

    print(f"Ваш возраст: {age} лет.")

# Вызываем функцию
calculate_age()

