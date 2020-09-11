import names
import random
import csv
import matplotlib.pyplot as plt

# Exercise 1
genders = ['female', 'male']
course_names = ['Maths', 'English', 'Danish', 'Biology','Chemisty','Geology','Religion']
classrooms = ['A101','A102','A103','A104','A105','A106','A107','A108','A109','A110','A111','A112','A113']

class Course():
    def __init__(self, name, classroom, teacher, ETCS, grade = None):
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.ETCS = ETCS
        self.grade = grade        
    
    def __str__(self):
        output = f'Name: {self.name}, Classroom: {self.classroom}, Teacher: {self.teacher}, ETCS: {self.ETCS}'
        if self.grade != None:
            output += f', Grade: {self.grade}'
        return output

class DataSheet():
    def __init__(self, courses=[]):
        self.courses = courses 
    
    def __str__(self):
        output = ""
        for cIndex in range(0, len(self.courses)):
            output += str(self.courses[cIndex])
            if cIndex < (len(self.courses)-1):
                output += "\n"
        return output

    def get_grades_as_list(self):
        grades = []
        for course in self.courses:
            if course.grade != None:
                grades.append(course.grade)
        return grades

class Student():
    def __init__(self, name, gender, image_url, dataSheet):
        self.name = name
        self.gender = gender
        self.image_url = image_url
        self.dataSheet = dataSheet

    def __str__(self):
        return f'Name: {self.name}, gender: {self.gender}, image_url: {self.image_url}.\nDataSheet:\n{self.dataSheet}'

    def short(self):
        return f'Name: {self.name}, gender: {self.gender}, image_url: {self.image_url}.'

    def get_avg_grade(self):
        avg = 0
        grades = self.dataSheet.get_grades_as_list()
        for grade in grades:
            if(grade != ""):
                avg += (grade / len(grades))
        return avg

    def get_etcs_progression(self):
        prog = 0
        for course in self.dataSheet.courses:
            prog += course.ETCS
        return ((prog/150)*100)

    def get_courses_taken(self):
        return self.dataSheet.courses


def write_students_to_csv(students, output_file):
    with open(output_file, "w", newline='\n') as file:
        fieldnames = ['stud_name','stud_gender','course_name','teacher','etcs','classroom','grade','image_url']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for student in students:
            for course in student.dataSheet.courses:
                writer.writerow({'stud_name':student.name,'stud_gender':student.gender,'course_name':course.name,'teacher':course.teacher,'etcs':course.ETCS,'classroom':course.classroom,'grade':course.grade,'image_url':student.image_url})

def generate_student(n):
    students = []
    for index in range(0, n):
        gender = random.choice(genders)
        courses =  []
        minCourse = min(random.randint(0, len(course_names))+1,len(course_names))
        for cIndex in range(0, minCourse):
            if random.randint(0,11) < 8:
                course = Course(course_names[cIndex],random.choice(classrooms),names.get_full_name(),10, random.randint(0,101))
                courses.append(course)
            else:
                course = Course(course_names[cIndex],random.choice(classrooms),names.get_full_name(),10)
                courses.append(course)
        dataSheet = DataSheet(courses)
        image_url = f'img%d.png' % index
        student = Student(names.get_full_name(gender),gender,image_url, dataSheet)
        students.append(student)
    return students

def generate_students_to_csv(output_file, n = 1):
    students = generate_student(n)
    write_students_to_csv(students, output_file)

def load_students_from_csv(input_file):
    students = []
    with open(input_file, "r") as file:
        reader = csv.DictReader(file)
        last_used_name = ""
        last_used_gender = ""
        last_used_image_url = ""
        temp_courses = []
        for row in reader:
            stud_name = row['stud_name']
            stud_gender = row['stud_gender']
            image_url = row['image_url']
            # course
            course_name = row['course_name']
            teacher = row['teacher']
            ects = row['etcs']
            classroom = row['classroom']
            grade = row['grade']
            if grade == '':
                current_course = Course(course_name,classroom,teacher,int(ects))
            else:
                current_course = Course(course_name,classroom,teacher,int(ects),int(grade))

            if stud_name == last_used_name or last_used_name == "":
                temp_courses.append(current_course)
            else:
                dataSheet = DataSheet(temp_courses)
                students.append(Student(last_used_name,last_used_gender,last_used_image_url,dataSheet))   
                temp_courses = []
                temp_courses.append(current_course)
            last_used_name = stud_name
            last_used_gender = stud_gender
            last_used_image_url = image_url
        dataSheet = DataSheet(temp_courses)
        students.append(Student(last_used_name,last_used_gender,last_used_image_url,dataSheet))   
    return students

def sort_students_by_avg_grades(students):
    sorted_list = sorted(students, key=lambda student: student.get_avg_grade(), reverse=True)
    return sorted_list

def bar_plot_student_grades(students):
    # Note that we are only taking the first name in the following list comprehension
    #  as to make the name more visible in the plot
    names = [student.name.split(" ")[0] for student in sorted_students]
    grades = [student.get_avg_grade() for student in sorted_students]
    plt.bar(names,grades, width=0.2, align='center')
    plt.title("Student Grades", fontsize=12)
    plt.xlabel("Names", fontsize=8)
    plt.ylabel("Average Grades", fontsize=8)
    plt.show()
    
def bar_plot_student_progression(students):
    categories = [x*10 for x in range(0,11)]
    hits = [x for x in range(0,11)]
    for student in students:
        prog = student.get_etcs_progression()
        catIndex = int(abs((prog-0.5) / 10))
        hits[catIndex] += 1
    plt.bar(categories, hits, width=5, align='center')
    plt.axis([0, max(categories), 0, max(hits)+5])
    plt.xticks(categories)
    plt.title("Student Progression", fontsize=12)
    plt.xlabel("Categories", fontsize=8)
    plt.ylabel("# Students", fontsize=8)
    plt.show()

############
# Exercise 2
class NotEnoughStudentsException(ValueError):
    def __init__(self, *args, **kwargs):
        ValueError.__init__(self, *args, **kwargs)

    def write_to_log(self, output_file="error.txt", append=True):
        opr = 'a' if append== True else 'w'
        with open(output_file, opr) as file:
            file.write(str(self) + "\n")
            print(f'[ERROR] Log written to: %s' % output_file)
            
def top_three_progress(students, allow_completion=False):
    if not len(students) < 3:
        top_three = []
        sorted_students = sorted(students, key=lambda student: student.get_etcs_progression(), reverse=True)
        for index in range(0,3):
            progression = sorted_students[index].get_etcs_progression()
            if not allow_completion and progression == 100:
                pass
            else:
                top_three.append(sorted_students[index])
        return top_three
    else:
        raise NotEnoughStudentsException('There needs to be at least three students, currenly: {}'.format(len(students)))

def write_top_three_to_file(students, output_file):
    try:
        top_three = top_three_progress(students)
        write_students_to_csv(top_three, output_file)
        print(f'Top three students written to: %s' % output_file)
    except NotEnoughStudentsException as exception:
        exception.write_to_log()

############
# Exercise 3
def pie_chart_plot_progression(students):
    categories = [x*10 for x in range(0,11)]
    hits = [0 for x in range(0,11)]
    for student in students:
        prog = student.get_etcs_progression()
        catIndex = int(abs(prog / 10))
        print(prog, catIndex)
        hits[catIndex] += 1
    
    # Get the categories in text with the % at the end or "" if no student hit the category
    proCategories = [f'%s%%' % categories[i] if hits[i] != 0 else '' for i in range(0,len(categories))]
    plt.pie(hits, labels=proCategories, autopct=lambda p:'{:.1f}%({:.0f})'.format(p,(p/100)*sum(hits)) if p != 0 else '', startangle=90)
    plt.title("ETCS Completion")
    plt.show()

def bar_plot_course_taken(students):
    male_c = {x:0 for x in course_names}
    female_c = {x:0 for x in course_names}
    for student in students:
        c_courses = student.get_courses_taken()
        for c in c_courses:
            if(student.gender == 'male'):
                male_c[c.name] += 1
            else:
                female_c[c.name] += 1
    m_v = list(male_c.values())
    f_v = list(female_c.values())
    plt.bar(male_c.keys(),m_v,width=0.5,color='blue',alpha=1.0, align='center')
    plt.tick_params(axis='both', which='major', labelsize=7)
    plt.axis([-1, len(course_names), 0, len(students)])
    plt.bar(female_c.keys(),f_v,width=0.5,color='red',alpha=1.0, align='center', bottom=m_v)
    plt.title("Number of students pr course")
    plt.show()

if __name__ == '__main__':
    n = 50
    #testing = 'Exercise 1'
    #testing = 'Exercise 2'
    testing = 'Exercise 3'
    
    print(f'[!] Running %s\n[!] With %d random students' % (testing,n))
    #generate_students_to_csv("std.csv", n)
    students = load_students_from_csv("std.csv")
    if testing == 'Exercise 1' :
        sorted_students = sort_students_by_avg_grades(students)
        bar_plot_student_grades(sorted_students)
        bar_plot_student_progression(sorted_students)

    if testing == 'Exercise 2':
        try:
            sorted_students = top_three_progress(students)
            for student in sorted_students:
                print(student)
        except NotEnoughStudentsException as exception:
            exception.write_to_log()
        write_top_three_to_file(students, "output.csv")

    if testing == 'Exercise 3':
        #pie_chart_plot_progression(students)
        bar_plot_course_taken(students)

    