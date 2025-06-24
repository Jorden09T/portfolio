import json
import csv


csv_file = 'ABCU_Advising_Program_Input.csv'
json_file = 'ABCU_Advising_Program_Input.json'

FILE_NAME: str = "ABCU_Advising_Program_Input.json"

courses: list = []
menu_choice: str

class FileProcessor:
    @staticmethod
    def read_data_from_file(file_name: str, course_info: list):
        try:
            file = open(FILE_NAME, "r")
            course_info = json.load(file)
            file.close()
        except Exception as e:
            IO.output_error_message(message="Please check that file exists and that is in json format.", error=e)
        except FileNotFoundError as e:
            IO.output_error_message(message="There was a problem with reading the file.", error=e)
        finally:
            if file.closed == False:
                file.close()
        return course_info

    @staticmethod
    def write_data_to_file (file_name: str, course_info: list):
        try:
            file = open(FILE_NAME, "w")
            json.dump(courses, file)
            file.close()
            print("The following data was saved to file!")
            for course in courses:
                print(f'Course {course["CourseId"]}'
                      f'{course["CourseName"]} has been saved.')
        except TypeError as e:
            IO.output_error_message("Please check that the data is in valid JSON format", e)
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
    def output_error_message(message: str, error: Exception = None):
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
            choice = input("Please select from the following menu: ")
            if choice not in ["1", "2", "3", "4", "5"]:
                raise Exception("Please choose between 1-5")
        except Exception as e:
            IO.output_error_message(message="Please select a valid option", error=e)
        return choice

    @staticmethod
    def output_course_data(course_info: list):
        print("-" * 50)
        for course in courses:
            print(f'{course["CourseId"]} '
                  f'{course["CourseName"]} ')
        print("-" * 50)

    @staticmethod
    def input_course_data(course_info: list):
        course_id: str = ''
        course_name: str = ''
        course_info: dict = {}

        try:
            course_id = input("What is the course ID? ")
            if not course_id.isalnum():
                raise ValueError('Course ID should have letters and numbers!')
            course_name = input("What is the course name?")
            course_info = {"CourseId": course_id,
                           "CourseName": course_name}
            courses.append(course_info)
            print(f'You have registered {course_name}, {course_id}')
        except ValueError as e:
            IO.output_error_message(message="Error Message: Invalid Name was Entered!", error=e)
        except Exception as e:
            IO.output_error_message(message="Input Error! Please check the data you have entered.")
