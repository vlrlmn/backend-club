def display_grade(all_grades):
    print(f"All Grades: {all_grades}")

def calc_average(all_grades):
    total_sum = sum(all_grades.values())
    num_students = len(all_grades)
    average = total_sum / num_students if num_students > 0 else 0
    print(f"Average grade: {average}")

def add_grade(all_grades):
    while True:
        try:
            student_name = str(input("Enter student name (or exit to stop): "))
            if student_name.lower() == 'exit':
                break
            if not student_name or not student_name.isalpha():
                print("Invalid student name")
                continue
        except ValueError:
            print("Invalid student name")
            continue
        try:
            grade = int(input("Enter grade: "))
            if grade < 0 or grade > 100:
                print("Grade must be between 0 and 100")
                continue
        except ValueError:
            print("Invalid grade, enter a number")
            continue

        all_grades[student_name] = grade


def main():
    all_grades = {}
    
    add_grade(all_grades)
    if (all_grades == {}):
        print("Grades list is empty!")
    else:
        display_grade(all_grades)
        calc_average(all_grades)


if __name__ == "__main__":
    main()