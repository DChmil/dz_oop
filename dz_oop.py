def around(curs):
    ss = {}
    for varium in curs:
        for key in varium.grades:
            if key in ss:
                ss[key] += varium.grades[key]
            else:
                ss[key] = varium.grades[key]
    for summ_curs in ss:
        print(f'Курс - {summ_curs}, средняя оценка - {round(sum(ss[summ_curs]) / len(ss[summ_curs]), 2)}')
    print()
    return

class Student:
    student_list = []
#    grand += courses_in_progress
    def __init__(self, name, surname, gender):
        Student.student_list.append(self)
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_st(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        sn = []
        if self.finished_courses == []:
            sn = ['Введение в программирование']
        else:
            sn.extend(self.finished_courses)
        st_grate = self.summ()
        separat = ", "
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {st_grate}\nКурсы в процессе изучения: {separat.join(self.courses_in_progress)}\nЗавершенные курсы: {separat.join(sn)}\n'
        return res

    def summ(self):
        st = []
        for lect in self.grades:
            st.extend(self.grades[lect])
        if st == []:
            st_grate = 'Нет оценок'
        else:
            st_grate = round(sum(st) / len(st), 2)
        return st_grate

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('ERROR')
            return
        return self.summ() < other.summ()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    lecturer_list = []
    def __init__(self, name, surname):
        super().__init__(name, surname)
        Lecturer.lecturer_list.append(self)
        self.grades = {}

    def __str__(self):
        st_grate = self.summ()
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка: {st_grate}\n'
        return res

    def summ(self):
        st = []
        for lect in self.grades:
            st.extend(self.grades[lect])
        if st == []:
            st_grate = 'Нет оценок'
        else:
            st_grate = round(sum(st) / len(st), 2)
        return st_grate

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('ERROR')
            return
        return self.summ() < other.summ()

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        return res

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['Java']

some_student = Student('Silver', 'Black', 'your_gender')
some_student.courses_in_progress += ['Python']
some_student.courses_in_progress += ['Web - разработка']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 9)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(some_student, 'Python', 10)

real_mentor = Reviewer('Mary', 'Grate')
real_mentor.courses_attached += ['Python']
real_mentor.courses_attached += ['Web - разработка']

real_mentor.rate_hw(best_student, 'Python', 8)
real_mentor.rate_hw(best_student, 'Python', 10)
real_mentor.rate_hw(some_student, 'Python', 9)
real_mentor.rate_hw(some_student, 'Python', 7)
real_mentor.rate_hw(some_student, 'Web - разработка', 10)
real_mentor.rate_hw(some_student, 'Web - разработка', 9)

cool_lector = Lecturer('Solo', 'Nilos')
cool_lector.courses_attached += ['Python']
cool_lector.courses_attached += ['Web - разработка']

best_student.rate_st(cool_lector, 'Python', 10)
best_student.rate_st(cool_lector, 'Python', 9)
some_student.rate_st(cool_lector, 'Python', 10)
some_student.rate_st(cool_lector, 'Web - разработка', 8)

other_lector = Lecturer('Nic', 'Sanni')
other_lector.courses_attached += ['Python']
other_lector.courses_attached += ['Анализ данных']

best_student.rate_st(other_lector, 'Python', 8)
best_student.rate_st(other_lector, 'Python', 10)
some_student.rate_st(other_lector, 'Python', 10)

print(best_student)
print(some_student)
print(f'Первый студент лучше второго - {best_student > some_student}')
print('-------------------------------')

print(cool_mentor)
print(real_mentor)
print('-------------------------------')

print(cool_lector)
print(other_lector)
print(f'Первый лектор лучше второго - {cool_lector > other_lector}')
print('-------------------------------')
print('Для студентов:')
sr_stud = around(Student.student_list)
print('Для лекторов:')
sr_lect = around(Lecturer.lecturer_list)