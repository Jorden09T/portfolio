import course_info

import main

MENU: str = '''
-------- Advising Program --------
    Select from the following Menu:
    1. Add A course
    2. Load Course List
    3. Save to Database
    4. Convert to CSV
    5. Exit
-----------------------------------
'''
courses = course_info.FileProcessor.read_data_from_file(file_name=course_info.FILE_NAME, course_info=course_info.courses)
def course_menu_display():
    course_info.IO.output_menu(menu=MENU)
    while True:
        menu_choice = course_info.IO.input_menu_choice()

        if menu_choice == '1':
            course_info.IO.input_course_data(course_info=courses)
            continue

        elif menu_choice == '2':
            course_info.IO.output_course_data(course_info=courses)
            continue

        elif menu_choice == '3':
            course_info.FileProcessor.write_data_to_file(file_name=course_info.FILE_NAME, course_info=courses)
            continue

        elif menu_choice == '4':
            course_info.FileProcessor.convert_json_to_csv(course_info.json_file, course_info.csv_file)

        elif menu_choice == '5':
            print("Please wait heading back to Main Menu...")
            main.MMIO.output_menu(menu=main.MMENU)

    print("Program was successfully closed")

