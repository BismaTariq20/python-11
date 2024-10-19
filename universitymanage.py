class University:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.faculties = []  # List to store Faculty objects

    def add_faculty(self, faculty):
        self.faculties.append(faculty)
        print(f"Faculty '{faculty.name}' has been added to the university.")

    def display_faculties(self):
        print(f"Faculties in {self.name}:")
        for faculty in self.faculties:
            print(f"- {faculty.name}")

    def __str__(self):
        return f"University: {self.name}, Location: {self.location}"


class Faculty:
    def __init__(self, name, department):
        self.name = name
        self.department = department
        self.students = []  # List to store Student objects
        self.teachers = {}  # Dictionary to store teachers by name (Punjab/Sindh)

    def add_student(self, student):
        self.students.append(student)
        print(f"Student '{student.name}' has been added to the faculty '{self.name}'.")

    def display_students(self):
        print(f"Students in the faculty of {self.name}:")
        for student in self.students:
            print(f"- {student.name}")

    def add_teacher(self, name, campus):
        self.teachers[name] = campus  # Store teacher name with campus information

    def display_teachers(self):
        print(f"Teachers in the faculty of {self.name}:")
        for teacher_name, campus in self.teachers.items():
            print(f"- {teacher_name} ({campus})")

    def __str__(self):
        return f"Faculty: {self.name}, Department: {self.department}"


class Student:
    def __init__(self, name, student_id, year=None):  # Add a default value for year
        self.name = name
        self.student_id = student_id
        self.year = year

    def __str__(self):
        return f"Student: {self.name}, ID: {self.student_id}, Year: {self.year}"


def main():
    # Create a university
    university = University("OBF University", "Punjab and Sindh")

    # Add Campuses (implicit in this example)
    punjab_campus = "Punjab"
    sindh_campus = "Sindh"

    # Create faculties
    engineering_faculty = Faculty("Engineering", "Computer Science")
    business_faculty = Faculty("Business", "Finance")

    # Add faculties to the university
    university.add_faculty(engineering_faculty)
    university.add_faculty(business_faculty)

    # Create students (assuming no specific year, provide None for year)
    student1 = Student("Bisma", "67895", None)  # Provide None for year
    student2 = Student("Nimra", "57221", None)  # Provide None for year
    student3 = Student("Yusra", "12345", None)  # Provide None for year

    # Add students to faculties
    engineering_faculty.add_student(student1)
    engineering_faculty.add_student(student2)
    business_faculty.add_student(student3)

    # Add teachers (assuming specific campuses)
    engineering_faculty.add_teacher("Zia Khan", punjab_campus)
    engineering_faculty.add_teacher("Abu Hurairah", punjab_campus)
    engineering_faculty.add_teacher("Naveed", punjab_campus)
    business_faculty.add_teacher("Amir Khan", sindh_campus)
    business_faculty.add_teacher("Waseem", sindh_campus)
    business_faculty.add_teacher("Nasir", sindh_campus)

    # Display university details
    print(university)
    university.display_faculties()

    # Display faculty details with teachers
    print("\nFaculty Details:")
    for faculty in university.faculties:
        faculty.display_students()
        faculty.display_teachers()

    # Example of searching for a student (modify as needed)
    # ... (same logic as before)


# Run the main function
if __name__ == "__main__":
    main()