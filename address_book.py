import pandas as pd
book = pd.DataFrame(columns=["ФИО", "Адрес", "Телефон", "Дата рождения"])  # создаем пустую базу
while True :
    print("\n=== ГЛАВНОЕ МЕНЮ ===")
    print("1. Показать контакты")
    print("2. Добавить контакт")
    print("3. Удалить контакт")
    print("4. Редактировать контакт")
    print("0. Выход")
    choice = input("\nВыберите пункт меню: ").strip()  # чистим пробелы по краям
    if choice == "1":
        if book.empty:
            print("Книга пока пуста :(")
        else:
            print("\n", book)     
    elif choice == "2":
        fio = input("ФИО: ")
        address = input("Адрес: ")
        phone = input("Телефон: ")
        birth = input("Дата рождения: ")
        book.loc[len(book)] = [fio, address, phone, birth]  # пишем строку в самый конец таблицы
        print("Готово! Контакт добавлен.")
    elif choice == "3":
        if book.empty:
            print("Удалять нечего, книга пуста.")
            continue  # обратно в меню 
        print("\n", book)
        try:
            num = int(input("\nВведите индекс строки для удаления: "))
            if num in book.index:  # проверяем, есть ли такой номер
                book = book.drop(num).reset_index(drop=True)  # удаляем и пересчитываем индексы с нуля
                print("Запись успешно удалена.")
            else:
                print("Ошибка: нет строки с таким индексом!")
        except ValueError:
            print("Введите корректное число!")  # если ввели буквы вместо цифр
    elif choice == "4":
        if book.empty:
            print("Редактировать нечего, книга пуста.")
            continue
        print("\n", book)
        try:
            num = int(input("\nВведите индекс строки для изменения: "))
            if num in book.index:
                print("Enter — оставить без изменений")
                for col in book.columns:  # перебираем все колонки по очереди
                    val = input(f"Новый {col} (текущий: {book.loc[num, col]}): ").strip()
                    if val:  # если строка не пустая, обновляем данные
                        book.loc[num, col] = val
                print("Контакт обновлен!")
            else:
                print("Такого индекса нет.")
        except ValueError:
            print("Нужно ввести число!")  # защита от неверного ввода    
    elif choice == "0":
        print("Пока!")
        break  # выходим из цикла
    else:
        print("Не туда нажали, попробуйте еще раз.")