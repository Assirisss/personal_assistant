from models.contacts import CONTACT_FUNC, CONTACT
from models.finance import FINANCE_FUNC, FINANCE
from models.notes import FUNC_NOTE, NOTE
from models.tasks import TASK_FUNC, TASK
from Calculator import Calculator


def main():
    while True:
        print('Добро пожаловать в Персональный помощник!')
        print('Выберите действие:')
        print('1. Управление заметками')
        print('2. Управление задачами')
        print('3. Управление контактами')
        print('4. Управление финансовыми записями')
        print('5. Калькулятор')
        print('6. Выход')
        main_choice = input('Выберите действие: ')

        if main_choice == '1':
            while True:
                print('1. Создать заметку')
                print('2. Показать все заметки')
                print('3. Показать заметку по ID')
                print('4. Обновить заметку')
                print('5. Удалить заметку')
                print('6. Импорт заметок')
                print('7. Экспорт заметок')
                print('8. Назад')
                choice = input('Выберите действие: ')

                if choice == '1':
                    title = input('Введите заголовок заметки: ')
                    content = input('Введите содержимое заметки: ')
                    Note = FUNC_NOTE()
                    Note.create(NOTE(title, content))
                    print('Заметка успешно создана!')

                elif choice == '2':
                    Note = FUNC_NOTE()
                    notes = Note.show()
                    if notes:
                        for note in notes:
                            print(f"ID: {note['id']}, Заголовок: {note['title']}")
                    else:
                        print('Заметок нет!')

                elif choice == '3':
                    id = int(input('Введите ID заметки: '))
                    Note = FUNC_NOTE()
                    note = Note.show_by_id(id)
                    if note:
                        print(f"ID: {note['id']}, Заголовок: {note['title']}, Содержимое: {note['content']}")
                    else:
                        print('Заметка не найдена!')

                elif choice == '4':
                    id = int(input('Введите ID заметки: '))
                    title = input('Введите новый заголовок заметки: ')
                    content = input('Введите новое содержимое заметки: ')
                    Note = FUNC_NOTE()
                    Note.update(id, NOTE(title, content))
                    print('Заметка успешно обновлена!')

                elif choice == '5':
                    id = int(input('Введите ID заметки: '))
                    Note = FUNC_NOTE()
                    Note.delete(id)
                    print('Заметка успешно удалена!')

                elif choice == '6':
                    path = input('Введите путь к файлу: ')
                    Note = FUNC_NOTE()
                    Note.import_export(path_csv_file=path, mode= 'import')
                    print('Заметки успешно импортированы!')
                elif choice == '7':
                    Note = FUNC_NOTE()
                    Note.import_export(mode='export')
                    print('Заметки успешно экспортированы!')
                elif choice == '8':
                    main()

        elif main_choice == '2':
            while True:
                print('1. Создать задачу')
                print('2. Показать все задачи')
                print('3. Отметить задачу выполненной')
                print('4. Обновить задачу')
                print('5. Удалить задачу')
                print('6. Импорт задач')
                print('7. Экспорт задач')
                print('8. Назад')
                choice = input('Выберите действие: ')

                if choice == '1':
                    title = input('Введите заголовок задачи: ')
                    description = input('Введите описание задачи: ')
                    done = False
                    priority = input('Введите приоритет задачи (Высокий , Средний, Низкий): ')
                    due_date = input('Введите дату завершения задачи: ')
                    task = TASK_FUNC()
                    task.add_new_task(TASK(title, description, done, priority, due_date))
                    print('Задача успешно создана!')

                elif choice == '2':
                    filter_type = input('Введите тип сортировки (done, priority, due_date, not): ')
                    if filter_type in ['done', 'priority', 'due_date']:
                        value = input('Введите значение: ')
                    else:
                        value = None
                    Task = TASK_FUNC()
                    tasks = Task.show_all(filter_type, value)
                    if tasks:
                        for task in tasks:
                            print(f"ID: {task['id']}, Заголовок: {task['title']}, Описание: {task['description']}, Выполнено: {task['done']}, Приоритет: {task['priority']}, Дата завершения: {task['due_date']}")
                    else:
                        print('Задач нет!')



                elif choice == '3':
                    Task = TASK_FUNC()
                    id_task = int(input('Введите ID задачи: '))
                    Task.complete(id_task)


                elif choice == '4':
                    id_task = int(input('Введите ID задачи: '))
                    title = input('Введите новый заголовок задачи: ')
                    description = input('Введите новое описание задачи: ')
                    done = input('Задача выполнена? (True/False): ')
                    priority = input('Введите приоритет задачи (Высокий , Средний, Низкий): ')
                    due_date = input('Введите дату завершения задачи: ')
                    Task = TASK_FUNC()
                    Task.update(id_task, TASK(title, description, done, priority, due_date))


                elif choice == '5':
                    Task = TASK_FUNC()
                    id_task = int(input('Введите ID задачи: '))
                    Task.delete(id_task)

                elif choice == '6':
                    path = input('Введите путь к файлу: ')
                    Task = FUNC_NOTE()
                    Task.import_export(path_csv_file=path, mode='import')
                    print('Заметки успешно импортированы!')

                elif choice == '7':
                    Task = FUNC_NOTE()
                    Task.import_export(mode='export')
                    print('Заметки успешно экспортированы!')

                elif choice == '8':
                    main()
        elif main_choice == '3':
            while True:
                print('1. Создать контакт')
                print('2. Показать контакт по Имени или номеру')
                print('3. Редактировать контакт')
                print('4. Удалить контакт')
                print('5. Импорт контактов')
                print('6. Экспорт Контактов')
                print('7. Назад')
                choice = input('Выберите действие: ')

                if choice == '1':
                    name = input('Введите имя контакта: ')
                    phone = input('Введите номер телефона контакта: ')
                    email = input('Введите email контакта: ')
                    Contact = CONTACT_FUNC()
                    Contact.create(CONTACT(name, phone, email))
                    print('Контакт успешно создан!')

                elif choice == '2':
                    Contact = CONTACT_FUNC()
                    type = input('Введите тип поиска (name, phone): ')
                    value = input('Введите name: 'if type == 'name' else 'Введите phone: ')
                    contacts = Contact.find_contact(type, value)
                    if contacts:
                        for contact in contacts:
                            print(f"ID: {contact['id']}, Имя: {contact['name']}, Телефон: {contact['phone']}, Email: {contact['email']}")
                    else:
                        print('Контакт не найден!')


                elif choice == '3':
                    id = int(input('Введите ID контакта: '))
                    name = input('Введите новое имя контакта: ')
                    phone = input('Введите новый номер телефона контакта: ')
                    email = input('Введите новый email контакта: ')
                    Contact = CONTACT_FUNC()
                    Contact.update(id, CONTACT(name, phone, email))
                    print('Контакт Успешно обновлен!')

                elif choice == '4':
                    id = int(input('Введите ID контакта: '))
                    Contact = CONTACT_FUNC()
                    Contact.delete(id)
                    print('Контакт успешно удален!')


                elif choice == '6':
                    path = input('Введите путь к файлу: ')
                    Contact = CONTACT_FUNC()
                    Contact.import_export(path_csv_file=path, mode='import')
                    print('Контакты успешно импортированы!')


                elif choice == '7':
                    Contact = CONTACT_FUNC()
                    Contact.import_export(mode='export')
                    print('Контакты успешно экспортированы!')
                elif choice == '8':
                    main()

        elif main_choice == '4':
            while True:
                print('1. Создать финансовую запись')
                print('2. Показать финансовые записи')
                print('3. Генерация финансовых записей за период')
                print('4. Импорт финансовых записей')
                print('5. Экспорт финансовых записей')
                print('6. Общий баланс')
                print('7. Вывод расходов и доходов по категориям')
                print('8. Назад')
                choice = input('Выберите действие: ')

                if choice == '1':
                    amount = input('Введите сумму финансовой записи: ')
                    category = input('Введите категорию финансовой записи: ')
                    description = input('Введите описание финансовой записи: ')
                    Finance = FINANCE_FUNC()
                    Finance.create(FINANCE(amount, category, description))
                    print('Финансовая запись успешно создана!')

                elif choice == '2':
                    filter_type = input('Введите тип сортировки (category, date, not): ')
                    if filter_type in ['categoty', 'date']:
                        value = input('Введите категорию: ' if filter_type == 'category' else 'Введите дату: ')
                    Finance = FINANCE_FUNC()
                    finances = Finance.show_all_fin_not(filter_type, value)
                    if finances:
                        for finance in finances:
                            print(f"ID: {finance['id']}, Сумма: {finance['amount']}, Категория: {finance['category']}, Описание: {finance['description']}")
                    else:
                        print('Финансовых записей нет!')

                elif choice == '3':
                    start = input('Введите начальную дату: ')
                    end = input('Введите конечную дату: ')
                    Finance = FINANCE_FUNC()
                    finances = Finance.generate_period(start, end)
                    if finances:
                        for finance in finances:
                            print(f"ID: {finance['id']}, Сумма: {finance['amount']}, Категория: {finance['category']}, Описание: {finance['description']}")
                    else:
                        print('Финансовых записей нет!')

                elif choice == '4':
                    path = input('Введите путь к файлу: ')
                    Finance = FINANCE_FUNC()
                    Finance.import_export(path_csv_file=path, mode='import')
                    print('Финансовые записи успешно импортированы!')

                elif choice == '5':
                    Finance = FINANCE_FUNC()
                    Finance.import_export(mode='export')
                    print('Финансовые записи успешно экспортированы!')

                elif choice == '6':
                    Finance = FINANCE_FUNC()
                    print(f"Общий баланс: {Finance.all_balance()}")

                elif choice == '7':
                    Finance = FINANCE_FUNC()
                    print(Finance.return_income_expense_by_ctg())
                elif choice == '8':
                    main()

        elif main_choice == '5':
            while True:
                print('1. Сложение')
                print('2. Вычитание')
                print('3. Умножение')
                print('4. Деление')
                print('5. Назад')
                choice = input('Выберите действие: ')
                if choice == '1':
                    a = int(input('Введите первое число: '))
                    b = int(input('Введите второе число: '))
                    print(Calculator.add(a, b))
                elif choice == '2':
                    a = int(input('Введите первое число: '))
                    b = int(input('Введите второе число: '))
                    print(Calculator.subtract(a, b))
                elif choice == '3':
                    a = int(input('Введите первое число: '))
                    b = int(input('Введите второе число: '))
                    print(Calculator.multiply(a, b))
                elif choice == '4':
                    a = int(input('Введите первое число: '))
                    b = int(input('Введите второе число: '))
                    print(Calculator.divide(a, b))
                elif choice == '5':
                    main()
        elif main_choice == '6':
            break




