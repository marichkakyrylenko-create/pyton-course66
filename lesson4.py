# Менеджер команди пригодників з функціями та обробкою помилок

team = [
    {"name": "Аріа",    "class": "лучниця",   "level": 5, "hp": 42},
    {"name": "Богдан",  "class": "воїн",       "level": 7, "hp": 68},
    {"name": "Соломія", "class": "чарівниця",  "level": 4, "hp": 30},
]


def print_team(team):
    print("Твоя команда пригодників:")
    for hero in team:
        print(hero["name"], "-", hero["class"], "- рівень", hero["level"], "- HP", hero["hp"])


def team_stats(team):
    total_hp    = 0
    total_level = 0
    for hero in team:
        total_hp    = total_hp    + hero["hp"]
        total_level = total_level + hero["level"]
    average_level = total_level / len(team)
    return total_hp, average_level


def get_int_input(prompt):
    while True:
        value = input(prompt)
        try:
            return int(value)
        except ValueError:
            print("Це не схоже на ціле число. Спробуй ще раз.")


def add_hero(team):
    print()
    print("Додаємо нового героя до команди.")
    new_name  = input("Ім'я нового героя: ")
    new_class = input("Клас героя (воїн/лучниця/чарівниця): ")
    new_level = get_int_input("Рівень героя: ")
    new_hp    = get_int_input("Кількість HP: ")
    new_hero  = {
        "name":  new_name,
        "class": new_class,
        "level": new_level,
        "hp":    new_hp,
    }
    team.append(new_hero)
    print(new_name, "приєднався(лася) до команди!")


def find_hero(team, name):
    for hero in team:
        if hero["name"].lower() == name.lower():
            return hero
    return None

#функція зміни HP героя за допомогою кнопки 
def change_hp(team, name, delta):
    for hero in team:
        if hero["name"].lower() == name.lower():
            hero["hp"] += delta
            print(f"{name} тепер має {hero['hp']} HP.")
            return
    print(f"Героя з ім'ям {name} немає в команді.")

def main():
    print_team(team)
    change_hp(team, "Аріа", 10)
    add_hero(team)
    print()
    print_team(team)

    total_hp, average_level = team_stats(team)
    print()
    print("Загальний HP команди:", total_hp)
    print("Середній рівень команди:", average_level)

    print()
    search_name = input("Введи ім'я героя для пошуку: ")
    found_hero  = find_hero(team, search_name)

    if found_hero is not None:
        print("Знайдено:", found_hero["name"], "-", found_hero["class"], "- рівень", found_hero["level"])
    else:
        print("Героя з таким ім'ям немає в команді.")


main()