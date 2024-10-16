# Генерация списка "случайных" чисел
def generate_numbers():
    numbers = []
    for i in range(10):
        numbers.append((i * 37 + 29) % 201)  # Генерация чисел от 0 до 200
    return numbers

# Основная функция
def find_multiples():
    numbers = generate_numbers()  # Генерация списка чисел
    print("Сгенерированные числа:", numbers)

    x = int(input("Введите цифру X (от 1 до 9): "))  # Ввод цифры

    # Поиск кратных числу X
    multiples = list(filter(lambda num: num % x == 0, numbers))

    print(f"Числа, кратные {x}: {multiples}")  # Вывод результата

# Запуск программы
find_multiples()
