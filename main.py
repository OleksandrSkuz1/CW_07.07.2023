if __name__ == '__main__':
    # students = [
    #     {
    #         "name":"John",
    #         "present": None
    #
    #     },
    #
    #     {
    #         "name":"Jerry",
    #         "present": None
    #
    #     },
    #     {
    #     "name": "Jane",
    #     "present": None
    #
    #
    #     }
    # ]
    #
    # # for student in students:
    # #     present_choice = present = input(f"Чи є {student['name']} на занятті (Y/N):")
    # #     if present_choice.lower() == "y":
    # #         present = True
    # #     else:
    # #         present = False
    # #
    # #         student["present"] = present
    # #         print(student)
    #
    # present = _count = 0
    # for student in students:
    #
    #     present_choice = input(f"Чи є {student['name']} на занятті (Y/N):")
    #     if present_choice.lower() == "y":
    #         student["present"] = True
    #         present_count += 1
    #     else:
    #         student["present"] = False
    #
    #         print(f"Присутні" {present_count}. Відсутні: {len(students) - present_count} )




    # for i in range(len(students)):
    #     print(students[i])


    # count_new_student = int(input("Скільки студентів додати: "))
    # for i in range(2):
    #     name_student = input("Введіть імя студента: ")
    #     frame_student = {
    #         "name": name_student,
    #         "present": None
    #     }
    #         student.append(frame_student)
    #     print(student)



    # count_delete_student = int(input("Скільки студентів вилучити: "))
    # for i in range(2):
    # name_student = input("Введіть імя студента: ")
    # frame_student = {
    #     "name": name_student,
    #     "present": None
    # }
    # student.remove(frame_student)
    # print(student)


    # a = 0
    # while a < 10:
    #     a += 1
    #     if a <= 10:
    #      print(a)
    #
    #
    # a = True
    # b = 0
    # while a:
    #     b += 1
    #     if b >= 100:
    #         break
    #         print(b)









    credit_data = {
        'user1': {
            'credit1': 5000,
            'credit2': 2000,
            'credit3': 10000
        },
        'user2': {
            'credit1': 3000,
            'credit2': 1500,
            'credit3': 8000
        },
        'user3': {
            'credit1': 7000,
            'credit2': 0,
            'credit3': 5000
        },
        # Додайте інші користувачі та їх кредити сюди
        # ...
        'user20': {
            'credit1': 10000,
            'credit2': 5000,
            'credit3': 3000
        }
    }

    credit_one_count = 0
    credit_two_count = 0
    credit_three_count = 0
    for item in credit_data:
        for credit in credit_data[item]:
         if credit == "credit1":
            credit_one_count += credit_data[item][credit]

         elif credit == "credit2":
            credit_two_count += credit_data[item][credit]
         elif credit == "credit3":
            credit_three_count += credit_data[item][credit]


        print(" Заборгованість по кредиту1 ", credit_one_count)
        print(" Заборгованість по кредиту2 ", credit_two_count)
        print(" Заборгованість по кредиту3 ", credit_three_count)

        for item in credit_data:
            total_debt = 0
            for credit in credit_data[item]:
             total_debt += credit_data[item][credit]

             if max_debt < total_debt:
                 max_debt = total_debt
                 user_max_debt = item

                 print(f"{user_max_debt} -- {max_debt}")




