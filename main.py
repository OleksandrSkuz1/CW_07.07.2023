if __name__ == '__main__':
    students = [
        {                           # [{}] - створюємо словник із списком учнів
            "name":"John",
            "present": None         # присутність None(невизначена, тому що ми їх ще не відмічали)
        },

        {
            "name":"Jerry",
            "present": None
        },
        {
            "name": "Jane",
            "present": None
        }
    ]

    # print(student['name'])        # для того щоб вивести [імя] кожного студента
    # print({student['name']}       # для того щоб вибрати [імя] кожного студента із {масиву}

    # for student in students:            # викор.цикл for in
    #     present_choice = input(f"Чи є {student['name']} на занятті (Y/N): " ) #  при проході кожного циклу запитує про кожного
    #                                                                           #  студента чи є він на занятті
    #     if present_choice.lower() == "y":       # якщо ви виберете y, тоді
    #         present = True
    #     else:
    #         present = False
    #
    #     student['present'] = present
    #      print(students)                         # виведе інформацію про кожного студента. Є він чи немає.



   # МЕТОД ДЛЯ ВИВОДУ КІЛЬКОСТІ СТУДЕНТІВ ПРИСУТНІХ І ЗАГАЛЬНОЇ КІЛ-ТІ ВІДСУТНІХ. Створюємо лічильник.

    # present_count = 0
    # for student in students:
    #     present_choice = input(f"Чи є {student['name']} на занятті (Y/N): ")
    #
    #     if present_choice.lower() == "y":
    #         student['present'] = True
    #         present_count += 1
    #     else:
    #         student['present'] = False
    #
    # print(f"Присутні {present_count}. Відсутні: {len(students) - present_count}")


    # Для того щоб проробити щось певну к-ть разів використ.:
    # for item in range(10):
    #     print(item)

    # # Для того щоб робити зчитування з певним кроком:
    # for item in range(2, 10, 2):  # перше число з якого старт; друге - к-ть; третє-крок
    #  print(item)

    # # Добавляємо студентів  в список (формуємо frame):
    # count_new_student = int(input("Скільки студентів хочете додати: "))
    # for i in range(count_new_student):
    #     name_student = input("Введіть імя студента: ")
    #     frame_student = {
    #         "name": name_student,
    #         "present": None
    #     }
    #     students.append(frame_student)
    #     print(students)
    #
    #
    #
    # count_delete_student = int(input("Скільки студентів вилучити: "))
    # for i in range(2):
    # name_student = input("Введіть імя студента: ")
    # frame_student = {
    #     "name": name_student,
    #     "present": None
    # }
    # student.remove(frame_student)
    # print(student)




    a = 0
    while a < 10:
        a += 1
        if a <= 10:
         print(a)


    # a = True
    # b = 0
    # while a:
    #     b += 1
    #     if b >= 100:
    #         break
    #         print(b)









    # credit_data = {
    #     'user1': {
    #         'credit1': 5000,
    #         'credit2': 2000,
    #         'credit3': 10000
    #     },
    #     'user2': {
    #         'credit1': 3000,
    #         'credit2': 1500,
    #         'credit3': 8000
    #     },
    #     'user3': {
    #         'credit1': 7000,
    #         'credit2': 0,
    #         'credit3': 5000
    #     },
    #     # Додайте інші користувачі та їх кредити сюди
    #     # ...
    #     'user20': {
    #         'credit1': 10000,
    #         'credit2': 5000,
    #         'credit3': 3000
    #     }
    # }
    #
    # credit_one_count = 0
    # credit_two_count = 0
    # credit_three_count = 0
    # for item in credit_data:
    #     for credit in credit_data[item]:
    #      if credit == "credit1":
    #         credit_one_count += credit_data[item][credit]
    #
    #      elif credit == "credit2":
    #         credit_two_count += credit_data[item][credit]
    #      elif credit == "credit3":
    #         credit_three_count += credit_data[item][credit]
    #
    #
    #     print(" Заборгованість по кредиту1 ", credit_one_count)
    #     print(" Заборгованість по кредиту2 ", credit_two_count)
    #     print(" Заборгованість по кредиту3 ", credit_three_count)
    #
    #     for item in credit_data:
    #         total_debt = 0
    #         for credit in credit_data[item]:
    #          total_debt += credit_data[item][credit]
    #
    #          if max_debt < total_debt:
    #              max_debt = total_debt
    #              user_max_debt = item
    #
    #              print(f"{user_max_debt} -- {max_debt}")




