
import json
import csv

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Convert Json to CSV
    5. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
csv_file = "Enrollments.csv"
json_file = "Enrollments.json"
FILE_NAME: str = "Enrollments.json"


students: list = []  # a table of student data
menu_choice: str  # Hold the choice made by the user.

class FileProcessor:
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        try:
            file = open(FILE_NAME, "r")
            student_data = json.load(file)
            file.close()
        except Exception as e:
            IO.output_error_messages(message="Please check that the file exists and that it is in a json format.", error=e)
        except FileNotFoundError as e:
            IO.output_error_messages(message="There was a problem with reading the file.", error=e)
        finally:
            if file.closed == False:
                file.close()
        return student_data
    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file)
            file.close()
            print("The following data was saved to file!")
            for student in students:
                print(f'Student {student["FirstName"]} '
                      f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        except TypeError as e:
            IO.output_error_messages("Please check that the data is in valid JSON format", e)
        except Exception as e:
            IO.output_error_messages("Error: There was a problem with the file.", e)
        finally:
            if file.closed == False:
                file.close()

    @staticmethod
    def convert_json_to_csv(json_file, csv_file):
        with open(json_file, 'r') as json_file:
            data = json.load(json_file)
        if not data:
            print("Json file is empty")
            return
        if isinstance(data, dict):
            data = [data]
        with open(csv_file, 'w') as csv_file:
            csv_writer = csv.writer(csv_file)

            header = data[0].keys()
            csv_writer.writerow(header)

            for row in data:
                csv_writer.writerow(row.values())
        print("Conversion is successful!")

class IO:
    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        print(message)
        if error is not None:
            print("------Error--Message --------")
            print(error.__doc__)
            print(error.__str__())

    @staticmethod
    def output_menu(menu: str):
        print(menu)

    @staticmethod
    def input_menu_choice():
        try:
            choice = input("Please Select from the following menu (1, 2, 3, 4 or 5): ")
            if choice not in ["1", "2", "3", "4"]:
                raise Exception("Please only Choose between options 1-4")
        except Exception as e:
            IO.output_error_messages(message="Please select a valid option", error=e)
        return choice

    @staticmethod
    def output_student_courses(student_data: list):
        print("-" * 50)
        for student in students:
            print(f'Student {student["FirstName"]}'
                  f' {student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        student_first_name: str = ''
        student_last_name: str = ''
        course_name: str = ''
        student_data: dict = {}
        try:
            student_first_name = input("What is the Student's first name? ")
            if not student_first_name.isalpha():
                raise ValueError('First name should only have alphabetic characters!')
            student_last_name = input("What is the Student's last name? ")
            if not student_last_name.isalpha():
                raise ValueError('First name should only have alphabetic characters!')
            course_name = input("What is the name of the course? ")
            student_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}")
        except ValueError as e:
            IO.output_error_messages(message="Error Message: Invalid Name was Entered!", error=e)
        except Exception as e:
            IO.output_error_messages(message="Input error, please check the data your have entered.", error=e)

students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

def display_student_menu():
    while True:
        IO.output_menu(menu=MENU)
        menu_choice = IO.input_menu_choice()

        if menu_choice == '1':
            IO.input_student_data(student_data=students)
            continue

        elif menu_choice == "2":
            IO.output_student_courses(student_data=students)
            continue

        elif menu_choice == "3":
            FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
            continue

        elif menu_choice == "4":
            FileProcessor.convert_json_to_csv(json_file, csv_file)
        elif menu_choice == "5":
            print("Good bye!")
            break

    print("Program has closed!")


