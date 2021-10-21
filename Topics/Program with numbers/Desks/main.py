n_students_classroom_1 = int(input())
n_students_classroom_2 = int(input())
n_students_classroom_3 = int(input())

n_desks_classroom_1 = n_students_classroom_1 // 2\
    if n_students_classroom_1 % 2 == 0 else n_students_classroom_1 // 2 + 1
n_desks_classroom_2 = n_students_classroom_2 // 2\
    if n_students_classroom_2 % 2 == 0 else n_students_classroom_2 // 2 + 1
n_desks_classroom_3 = n_students_classroom_3 // 2\
    if n_students_classroom_3 % 2 == 0 else n_students_classroom_3 // 2 + 1

print(n_desks_classroom_1 + n_desks_classroom_2 + n_desks_classroom_3)
