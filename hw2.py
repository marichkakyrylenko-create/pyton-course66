CORRECT_CARD = "4441"
CORRECT_PIN = "7421"

# Авторизація
for attempt in range(3):
    card = input("Введіть останні 4 цифри картки: ")
    pin = input("Введіть PIN-код: ")

    if card == CORRECT_CARD and pin == CORRECT_PIN:
        print("Авторизація успішна!")
        break
    else:
        print("Неправильна картка або PIN.")
        print("Залишилось спроб:", 2 - attempt)

else:
    print("Картку заблоковано через підозрілу активність!")
    exit()

# Меню
balance = 1000

while True:
    print("\n--- МЕНЮ ТЕРМІНАЛУ ---")
    print("1. Перевірити баланс")
    print("2. Зняти готівку")
    print("3. Поповнити рахунок")
    print("4. Завершити роботу")

    choice = input("Оберіть дію: ")

    if choice == "1":
        print("Ваш баланс:", balance)

    elif choice == "2":
        amount = int(input("Введіть суму для зняття: "))

        if amount > 0 and amount <= balance:
            balance = balance - amount
            print("Готівку успішно знято!")
            print("Залишок:", balance)
        else:
            print("Помилка! Некоректна сума або недостатньо коштів.")

    elif choice == "3":
        amount = int(input("Введіть суму поповнення: "))

        if amount > 0:
            balance = balance + amount
            print("Рахунок успішно поповнено!")
            print("Новий баланс:", balance)
        else:
            print("Помилка! Сума повинна бути більшою за 0.")

    elif choice == "4":
        print("Дякуємо за користування терміналом!")
        break

    else:
        print("Невідома команда. Спробуйте ще раз.")
