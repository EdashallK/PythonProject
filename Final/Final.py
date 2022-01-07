import os
import pathlib
import pickle


# This project will create a student profile and save it to a file

# Here we create a student object
class Student:
    def __init__(self, name, ID, Class):
        self.name = name
        self.ID = ID
        self.Class = Class

    # simple display the object
    def to_string(self):
        print("__________________________")
        print("Here is the student's profile")
        print(self.name)
        print(self.ID)
        print(self.Class)
        print("__________________________")


# We then prompt the user for the student information to create that  Student object
def student_profile():
    stuName = input('Enter a name: ')
    stuID = input('Enter the ID: ')
    stuClass = input('Enter their class of: ')
    tempStu = Student(stuName, stuID, stuClass)
    return tempStu


def create_student():
    serialize(student_profile())


def delete_student():
    roster = deserialize()
    person = (input("who do you want to remove from the roster"))
    for student in roster:
        if student.name == person:
            roster.remove(student.name)
    with open('roster.pickle', 'wb') as f:
        pickle.dump(roster, f, )


def display_all_students():
    roster = deserialize()
    for student in roster:
        print(student.name + " " + student.ID + " " + student.Class)


def display_name():
    roster = deserialize()
    for student in roster:
        print(student.name)


def display_IDs():
    roster = deserialize()
    for student in roster:
        print(student.ID)


def display_classes():
    roster = deserialize()
    for student in roster:
        print(student.Class)


def search_by_name():
    roster = deserialize()
    for student in roster:
        if student.name == input("what is the name you would like to search for?"):
            print(student.name + " " + student.ID + " " + student.Class)


def search_by_id():
    roster = deserialize()
    for student in roster:
        if student.ID == input("what is the ID you would like to search for?"):
            print(student.name + " " + student.ID + " " + student.Class)


def search_by_class():
    roster = deserialize()
    for student in roster:
        if student.Class == input("what is the class you would like to search for?"):
            print(student.name + " " + student.ID + " " + student.Class)


def deserialize():
    try:
        with open('roster.pickle', 'rb') as fin:
            return pickle.load(fin)
    except FileNotFoundError:
        with open('roster.pickle', 'wb') as fin:
            try:
                pickle.dump([], fin)
                print("Oops there was no previous roster made please try again.")
                create_student()
            except EOFError:
                return []


def serialize(student):
    roster = deserialize()
    roster.append(student)
    with open('roster.pickle', 'wb') as f:
        pickle.dump(roster, f, )
