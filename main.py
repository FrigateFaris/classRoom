import pickle
import random as rd
import string


class DataBase:
    @staticmethod
    def save_to_pickle(object):
        with open('pickled.bin', 'wb') as file:
            pickle.dump(object, file)


class Student:
    def __init__(self, student_id: int, student_name: str, student_surname: str):
        self.student_id = student_id
        self.student_name = student_name
        self.student_surname = student_surname

    def __str__(self):
        return f'{self.student_id} - {self.student_name} - {self.student_surname}'


class Classroom:
    def __init__(self, student_id: int, student_list: list):
        self.student_id = student_id
        self.student_list = student_list

    def __str__(self):
        return f'{self.student_id} - {self.student_list}'


class Creator:
    @staticmethod
    def create_student():
        student_id = rd.randint(1000, 100000)
        student_name = ''.join([rd.choice(string.ascii_letters) for _ in range(3, 12)]).capitalize()
        student_surname = ''.join([rd.choice(string.ascii_letters) for _ in range(7, 17)]).capitalize()
        return Student(student_id, student_name, student_surname)

    @staticmethod
    def create_classroom():
        student_id = rd.randint(1000, 100000)
        student_list = [Creator.create_student() for _ in range(3, 15)]
        return Classroom(student_id, student_list)


print(Creator.create_student())
