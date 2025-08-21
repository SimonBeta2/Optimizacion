from pymongo import MongoClient


# Clase para representar un estudiante
class Student:
    def __init__(self, id, name, age, course):
        self.id = id
        self.name = name
        self.age = age
        self.course = course

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "course": self.course
        }

    @staticmethod
    def from_dict(data):
        return Student(data['id'], data['name'], data['age'], data['course'])


class StudentRepository:

    def __init__(self):
        #self.client = MongoClient("mongodb+srv://juanfedevmaster:kqeV8VbhaWUuIOPS@cluster0.uzawp.mongodb.net/")
        self.client = MongoClient("mongodb://localhost:27017")
        self.db = self.client['school']
        self.collection = self.db['students']

    def add_student(self, student):
        self.collection.insert_one(student.to_dict())
        print(f"Student {student.name} added successfully.")

    def find_student(self, id=None):
        if id is not None:
            result = self.collection.find_one({"id": id})
            return Student.from_dict(result)

        result = self.collection.find()
        if result:
            return Student.from_dict(result)
        else:
            return None

    def modify_student(self, id, name, age, course):
        updated_data = {"name": name, "age": age, "course": course}
        result = self.collection.update_one({"id": id}, {"$set": updated_data})
        if result.matched_count > 0:
            print(f"Student {id} updated successfully.")
        else:
            print(f"Student {id} not found.")

    def delete_student(self, id):
        result = self.collection.delete_one({"id": id})
        if result.deleted_count > 0:
            print(f"Student {id} deleted successfully.")
        else:
            print(f"Student {id} not found.")

    def list_students(self):
        students = self.collection.find()
        for student in students:
            print(f"ID: {student['id']}, Name: {student['name']}, Age: {student['age']}, Course: {student['course']}")


def main():
    repository = StudentRepository()

    while True:
        print("\n1. Add Student")
        print("2. Modify Student")
        print("3. Delete Student")
        print("4. Get Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            id = input("Enter student ID: ")
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            course = input("Enter student course: ")
            student = Student(id, name, age, course)
            repository.add_student(student)
        elif choice == "2":
            id = input("Enter student ID to modify: ")
            name = input("Enter new name: ")
            age = int(input("Enter new age: "))
            course = input("Enter new course: ")
            repository.modify_student(id, name, age, course)
        elif choice == "3":
            id = input("Enter student ID to delete: ")
            repository.delete_student(id)
        elif choice == "4":
            id = input("Enter student ID: ")
            student = repository.find_student(id)
            print(f"ID: {student.id}, Name: {student.name}, Age: {student.age}, Course: {student.course}")
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


main()