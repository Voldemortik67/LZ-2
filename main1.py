import random

# Компьютер загадывает число от 1 до 10
secret_number = random.randint(1, 10)

print("Я загадал число от 1 до 10. Попробуй угадать!")

# Бесконечный цикл, пока игрок не угадает
while True:
    # Получаем ответ от игрока
    user_input = input("Введи свое число: ")

    # Проверяем, ввел ли пользователь число
    if not user_input.isdigit():
        print("Пожалуйста, вводи только цифры!")
        continue

    guess = int(user_input)

    # Сравниваем число игрока с загаданным
    if guess < secret_number:
        print("Мое число больше!")
    elif guess > secret_number:
        print("Мое число меньше!")
    else:
        print("Поздравляю, ты угадал! 🎉")
        break  # Выходим из цикла, игра окончена
