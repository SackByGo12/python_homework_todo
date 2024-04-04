import json

# Функция для загрузки списка задач из файла
def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    return tasks

# Функция для сохранения списка задач в файл
def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)

# Функция для добавления задачи в список
def add_task(tasks, task):
    tasks.append(task)
    save_tasks(tasks)
    print(f"Задача '{task}' была добавлена.")

# Функция для удаления задачи из списка
def delete_task(tasks, task_index):
    if 1 <= task_index <= len(tasks):
        deleted_task = tasks.pop(task_index - 1)
        save_tasks(tasks)
        print(f"Задача '{deleted_task}' была удалена.")
    else:
        print("Неверный номер задачи.")

# Функция для вывода всех задач
def show_all_tasks(tasks):
    if tasks:
        print("Список задач:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("Список задач пуст.")

def main():
    tasks = load_tasks()

    while True:
        print("\nМеню:")
        print("1. Показать все задачи")
        print("2. Добавить задачу")
        print("3. Удалить задачу")
        print("4. Выйти")

        choice = input("Выберите действие: ")

        if choice == '1':
            show_all_tasks(tasks)
        elif choice == '2':
            new_task = input("Введите новую задачу: ")
            add_task(tasks, new_task)
        elif choice == '3':
            task_index = int(input("Введите номер задачи для удаления: "))
            delete_task(tasks, task_index)
        elif choice == '4':
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте еще раз.")

if __name__ == '__main__':
    main()