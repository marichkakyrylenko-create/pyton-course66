backpack = [
    {"item": "apple", "type": "food", "quantity": 35},
    {"item": "water", "type": "drink", "quantity": 5},
    {"item": "knife", "type": "weapon", "quantity": 2}
]

print("Рюкзак:")
for item in backpack:
    print(f"{item['item']} — {item['type']} — {item['quantity']} шт.")

name = input("Назва предмета: ").strip()
item_type = input("Тип предмета: ").strip()
quantity = int(input("Кількість: "))


found = False

for item in backpack:
    if item["item"] == name:
        item["quantity"] += quantity
        found = True

if not found:
    backpack.append({
        "item": name,
        "type": item_type,
        "quantity": quantity
    })


total = 0

for item in backpack:
    total += item["quantity"]

print("\nОновлений рюкзак:")
for item in backpack:
    print(f"{item['item']} — {item['type']} — {item['quantity']} шт.")

print(f"\nВсього предметів: {total}")
