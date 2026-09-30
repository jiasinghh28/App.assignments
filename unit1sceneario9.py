class Course:
    def __init__(self, course_name, duration, fee):
        self.course_name = course_name
        self.duration = duration
        self.fee = fee

    def display(self):
        print(f"Course Name : {self.course_name}")
        print(f"Duration    : {self.duration} months")
        print(f"Fee         : ₹{self.fee}")
        print("-" * 30)


class ShortTermCourse(Course):
    def category(self):
        return "Short-Term"


class LongTermCourse(Course):
    def category(self):
        return "Long-Term"


class Institute:
    def __init__(self, institute_name):
        self.institute_name = institute_name
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def display_all_courses(self):
        print("\nInstitute Name:", self.institute_name)
        print("=" * 40)

        for course in self.courses:
            course.display()
            print("Category    :", course.category())
            print("=" * 40)


# Create Institute
institute = Institute("ABC Institute")

# Create Courses
course1 = ShortTermCourse("Python Programming", 3, 5000)
course2 = ShortTermCourse("Web Development", 4, 7000)
course3 = LongTermCourse("Data Science", 12, 25000)
course4 = LongTermCourse("Artificial Intelligence", 10, 30000)

# Add courses to institute
institute.add_course(course1)
institute.add_course(course2)
institute.add_course(course3)
institute.add_course(course4)

# Display all courses
institute.display_all_courses()
