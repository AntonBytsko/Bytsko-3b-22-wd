"""Класс Student, описывающий студента со свойствами имя, фамилия, курс
и оценками по каждому премету, и методом для расчета среднего балла"""


class Student:
    def __init__(self, name, surname, course, subj1, subj2, subj3, subj4, subj5):
        self.name = name
        self.surname = surname
        self.course = course
        self.subj1 = subj1
        self.subj2 = subj2
        self.subj3 = subj3
        self.subj4 = subj4
        self.subj5 = subj5

    def calc_average(self):
        calc_res = (self.subj1 + self.subj2 + self.subj3 + self.subj4 + self.subj5)/5
        res = "Студент " + self.name + " " + self.surname + " со средним баллом " + str(calc_res)
        return res


Student1 = Student("Anton", "Bytsko", 1, 5, 4, 3, 4, 4)

# Проверка результата
test_res = Student1.calc_average()

print(test_res)
