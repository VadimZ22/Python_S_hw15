import csv
import argparse
from student_log import log_info, log_error


class Control:

    def __init__(self, is_title, is_digit):
        self.is_title = is_title
        self.is_digit = is_digit

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __set__(self, instance, value):
        if not self.is_title(value):
            msg = f'Неверный формат записи! {value} должно начинаться с заглавной буквы!'
            log_error(msg)
            raise ValueError(msg)
        for i in value:
            if self.is_digit(i):
                msg = f'Неверный формат записи! В {value} не должно быть цифр!'
                log_error(msg)
                raise ValueError(msg)
        setattr(instance, self.param_name, value)


class Student:

    first_name = Control(str.istitle, str.isdigit)
    last_name = Control(str.istitle, str.isdigit)
    surname = Control(str.istitle, str.isdigit)

    def __init__(self, first_name, last_name, surname):
        self.first_name = first_name
        self.last_name = last_name
        self.surname = surname
        self._subjects = self.load_subjects()
        log_info('Создан экземпляр класса Student!')



    def load_subjects(self):
        dict = {}
        with open('subjects.csv', 'r', encoding='utf-8') as f:
            file = csv.reader(f, dialect='excel', delimiter=' ')
            for i in file:
                dict[str(*i)] = {'оценки':[], 'результаты тестов':[]}
            return dict

    def __repr__(self):
        return f'Student({self._first_name}, {self._last_name}, {self._surname})'

    def get_test_res(self, subj):
        res = len(self._subjects[subj]['результаты тестов'])
        if res:
            return sum(i for i in self._subjects[subj]['результаты тестов']) / res
        else: return None


    def set_test_res(self, subj, value):
        if 0 < value < 100:
            self._subjects[subj]['результаты тестов'].append(value)


    def get_grades(self):
        res = sum(len(self._subjects[i]['оценки']) for i in self._subjects)
        if res:
            return sum(j for i in self._subjects for j in self._subjects[i]['оценки']) / res
        else: return None


    def set_grades(self, subj, value):
        if 0 < value < 100:
            self._subjects[subj]['оценки'].append(value)





def create_student(name):
    return Student(*name)


# st3 = Student('Петров12', '1Иван', 'Петрович')
# st1 = Student('Петров', 'Иван', 'Петрович')
# st2 = Student('петров', 'иван', 'петрович')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Программа создает экземпляр класса Student')
    parser.add_argument('param', metavar='name', type=str, nargs='*',
                        help='Введите ФИО будущего студента через пробел')
    args = parser.parse_args()
    create_student(args.param)


# Вызов
# python .\student.py Сидоров Сергей Юрьевич