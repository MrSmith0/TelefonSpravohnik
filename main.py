# Имя файла для хранения контактов
FILE_NAME = "contacts.txt"


# Загрузка контактов из файла
def load_contacts():
    contacts = []
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                name, phone = line.strip().split(":")
                contacts.append({"name": name, "phone": phone})
    except FileNotFoundError:
        print("Файл с контактами не найден, будет создан новый файл.")
    return contacts


# Сохранение контактов в файл
def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        for contact in contacts:
            file.write(f"{contact['name']}:{contact['phone']}\n")
    print("Контакты успешно сохранены.")


# Показать все контакты
def show_contacts(contacts):
    if contacts:
        for index, contact in enumerate(contacts, start=1):
            print(f"{index}. Имя: {contact['name']}, Телефон: {contact['phone']}")
    else:
        print("Контактов нет.")


# Создать новый контакт
def create_contact(contacts):
    name = input("Введите имя: ")
    phone = input("Введите номер телефона: ")
    contacts.append({"name": name, "phone": phone})
    print("Контакт успешно добавлен.")


# Найти контакт
def find_contact(contacts):
    search = input("Введите имя или номер для поиска: ")
    results = [c for c in contacts if search.lower() in c['name'].lower() or search in c['phone']]
    if results:
        for contact in results:
            print(f"Имя: {contact['name']}, Телефон: {contact['phone']}")
    else:
        print("Контакт не найден.")


# Изменить контакт
def update_contact(contacts):
    search = input("Введите имя или номер для изменения: ")
    for contact in contacts:
        if search.lower() in contact['name'].lower() or search in contact['phone']:
            print(f"Найден контакт: Имя: {contact['name']}, Телефон: {contact['phone']}")
            new_name = input("Введите новое имя (оставьте пустым для пропуска): ")
            new_phone = input("Введите новый номер (оставьте пустым для пропуска): ")
            if new_name:
                contact['name'] = new_name
            if new_phone:
                contact['phone'] = new_phone
            print("Контакт успешно обновлен.")
            return
    print("Контакт не найден.")


# Удалить контакт
def delete_contact(contacts):
    search = input("Введите имя или номер для удаления: ")
    for contact in contacts:
        if search.lower() in contact['name'].lower() or search in contact['phone']:
            contacts.remove(contact)
            print("Контакт успешно удален.")
            return
    print("Контакт не найден.")


# Главное меню
def main():
    contacts = load_contacts()
    while True:
        print("\n1. Показать все контакты")
        print("2. Создать контакт")
        print("3. Найти контакт")
        print("4. Изменить контакт")
        print("5. Удалить контакт")
        print("6. Сохранить файл")
        print("7. Выход")

        choice = input("Выберите действие: ")
        if choice == "1":
            show_contacts(contacts)
        elif choice == "2":
            create_contact(contacts)
        elif choice == "3":
            find_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            save_contacts(contacts)
        elif choice == "7":
            save_contacts(contacts)
            print("Выход. Контакты сохранены.")
            break
        else:
            print("Неверный выбор, попробуйте снова.")


# Запуск программы
if __name__ == "__main__":
    main()
