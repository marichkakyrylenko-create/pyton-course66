name = input("Назва товару: ")
price = float(input("Ціна: "))
quantity = int(input("Кількість: "))

sum = price * quantity

discount = float(input("Знижка (%): "))

result = sum - sum * discount / 100

print("Товар:", name)
print("До сплати:", result, "грн.") 