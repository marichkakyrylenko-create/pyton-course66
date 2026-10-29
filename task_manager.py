from asyncio import tasks
import random

from hw2 import choice

def generate_password(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%"
    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("Згенерований пароль:", password)   
    return password

def check_password_strength(password):
    has_digit = False
    has_upper = False
    for char in password:
        if char.isdigit():
            has_digit = True
        if char.isupper():
            has_upper = True
    if len(password) >= 8 and has_digit and has_upper:
        return "надійний"
    elif len(password) >= 6:
        return "середній"
    else:
        return "слабкий"

def set_master_password():
    while True:
        password = input("Введи пароль: ")
        if check_password_strength(password) == "слабкий":
            choice = input("Хочеш виправити пароль? (так/ні): ")
            if choice == "так":   
                password = generate_password(12)
                return password
            else:
                return password

def login_gate(master_password):
    password = input("Введи пароль: ")
    if password == master_password:
        return True
    else:
        return False
        
def show_menu():
    print("1) Додати завдання \n2) Переглянути завдання \n3) Видалити завдання \n4) Вийти")
    if input("Ваш вибір: ") 
        if choice == "1":
            add_task()
        elif choice == "2": 
            view tasks()
        elif choice=="3" :
            delete task(tasks)
        else:
            break

def add_task(tasks):
    choice = input("введи назву завдання")
    tasks.append({"text": choice, "done": False})

def view_tasks():
    if not tasks:
        print("\Список завдань:")
        for i, task in enumerate[Any](tasks,start=1):
            print(f"{i}. {task['test']} - {'✓' if task['done'] else '✗'}

def delete_task(tasks):
    view_tasks(tasks)
    choice = input("введи номер завдання для видалення ")
    tasks.pop(choice - 1)