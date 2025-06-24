

#include <iostream>
#include <algorithm>
#include <string>
#include <fstream>
#include <vector>

using namespace std;


void loadDataStructure(vector<string>& courses, const string& fileName) {
    ifstream inputFile(fileName);
    if (inputFile.is_open()) {
        string course;
        while (getline(inputFile, course)) {
            courses.push_back(course);
        }
        inputFile.close();
        cout << "Data loaded succcesfully.\n";
    }
    else {
        cout << "Error opening file. Please Check file name!";
    }
}

void loadCourseList(const vector<string>& courses) {
    vector<string> sortedCourses = courses;
    sort(sortedCourses.begin(), sortedCourses.end());

    cout << "Course List:\n";
    for (const string& course : sortedCourses) {
        cout << course << endl;
    }
}

void printCourseInfo(const vector<string>& courses, const string& courseCode) {
    cout << "Course Information for " << courseCode << ": \n";
    auto it = find_if(courses.begin(), courses.end(),
        [courseCode](const string& course) {
            return course.find(courseCode) != string::npos;
        });

    if (it != courses.end()) {
        cout << *it << endl;
    }
    else {
        cout << "Course not found.\n";
    }
}

int main()
{

    cout << "Welcome to the course Planner!\n";

    vector<string> courses;

    cout << "Opening Course Data\n";
    cout << "Loading.....\n";

    ifstream inputFile;
    string fileName = "";
    inputFile.open("ABCU_Advising_Program_Input.csv");
    getline(inputFile, fileName);

    while (true) {
        int choice;
        cout << "\nMenu:\n";
        cout << "1. Load Data Structure\n";
        cout << "2. Load Course List\n";
        cout << "3. Print Course information\n";
        cout << "4. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        cin.ignore();

        switch (choice) {
        case 1:
            loadDataStructure(courses, fileName);
            break;
        case 2:
            loadCourseList(courses);
            break;
        case 3:
        {
            string courseCode;
            cout << "Enter the Course Code: ";
            cin >> courseCode;
            transform(courseCode.begin(), courseCode.end(), courseCode.begin(), ::toupper);
            printCourseInfo(courses, courseCode);
        }
        break;
        case 4:
            cout << "Exiting the Program.\n";
            return 0;
        default:
            cout << "Invalid choice. Please Try again!\n";
        }

    }

    return 0;

}
