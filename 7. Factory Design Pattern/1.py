class Person:
    def greet(self):
        raise NotImplementedError


class Student(Person):
    def greet(self):
        print("Hello, I am a student.")


class Teacher(Person):
    def greet(self):
        print("Hello, I am a teacher.")


def build_person(person_type):
    PERSON_TYPES = {"Student": Student, "Teacher": Teacher}
    return PERSON_TYPES[person_type]()


# Usage
person1 = build_person("Student")
person1.greet()  # Output: Hello, I am a student.

person2 = build_person("Teacher")
person2.greet()  # Output: Hello, I am a teacher.
