class Student:
    def __init__(self, name, surname, gender):
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
    def __init__(self, name, surname):
        super().__init__(name, surname)
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

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

print(best_student.grades)