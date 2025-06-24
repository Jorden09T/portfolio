import student_menu
import course_menu

MMENU: str = """
-------- Advising Program --------
    Select from the following Menu:
    1. Register Courses
    2. Student Registration
    3. Exit
-----------------------------------
"""
class MMIO:
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
            if choice not in ["1", "2", "3"]:
                raise Exception("Please choose between 1-3")
        except Exception as e:
            MMIO.output_error_message(message="Please select a valid option", error=e)
        return choice

def display_main_menu():
    print("-------- Advising Program --------")
    print("Select from the following Menu:   ")
    print("1. Register Courses               ")
    print("2. Student Registration           ")
    print("3. Exit                           ")
    print("----------------------------------")

    choice = input("Please select an option ")
    return choice

def run_main_app():
    while True:
        choice = display_main_menu()
        if choice == '1':
            course_menu.course_menu_display()

        elif choice == '2':
            print("loading...")
            student_menu.display_student_menu()

        elif choice == '3':
            print("Goodbye!")
            break
    print("Program was successfully closed")

if __name__ == "__main__":
    run_main_app()