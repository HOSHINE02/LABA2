# Генератор нечетных чисел из диапазона range(30)
def get_number1():
    for num in range(30):
        if num % 2 != 0:  # Проверка на нечетность
            yield num

# Основная логика
odd_numbers = list(get_number1())  # Преобразуем генератор в список

# Вывод первого, пятого и последнего элементов
first = odd_numbers[0] if len(odd_numbers) > 0 else None
fifth = odd_numbers[4] if len(odd_numbers) > 4 else None
last = odd_numbers[-1] if len(odd_numbers) > 0 else None

print("Первое нечетное число:", first)
print("Пятое нечетное число:", fifth)
print("Последнее нечетное число:", last)
