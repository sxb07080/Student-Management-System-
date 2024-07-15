from sqlalchemy import update

import custom_tools
import student_table
import score_table
import first_menu
from student_table import Students
from sqlalchemy.orm import sessionmaker


s_engine = student_table.create_db()
s_session = sessionmaker(bind=s_engine)()

def display_add_student_requirements():
    print("===================================Add Student===================================")
    print("1. The first letter of firstname and lastname must be capitalized")
    print("2. Firstname and lastname must each have at least two letters")
    print("3. No digit allowed in the name")
    print("4. Age must between 0 and 100")
    print("5. Gender can be M (Male), F (Female) or O (Other)")
    print("6. Phone must be in the (xxx-xxx-xxxx) format")

def check_add_student_details():
    while True:
        first_name = input("Please Enter Student's first name: ")
        last_name = input("Please Enter student's last name: ")
        full_name = f"{first_name} {last_name}"
        if custom_tools.name_check(full_name):
            break
        else:
            print("\t \u274C Invalid student name!")

    age = int(input("Please Enter Student's Age: "))
    while not custom_tools.age_check(age):
        print("\t \u274C Invalid student age!")
        age = int(input("Please Enter Student's Age: "))

    gender = input("Please enter Student's Gender: ").upper()
    while not custom_tools.gender_check(gender):
        print("\t \u274C Invalid student gender!")
        gender = input("Please enter Student's Gender: ").upper()

    major = input('Please enter Student\'s Major: ').upper()
    while not custom_tools.major_check(major):
        print("\t \u274C Invalid student major!")
        major = input("Please enter Student's Major: ").upper()

    phone_number = input("Please enter Student's Phone: ")
    while not custom_tools.phone_check(phone_number):
        print("\t \u274C Invalid student phone!")
        phone_number = input("Please enter Student's Phone: ")

    student_table.add_student(full_name, age, gender, major, phone_number)
    display_add_student_options()

def display_add_student_options():
    print("\t \u2666 1. Continue")
    print("\t \u2666 2. Exit")
    code = input(f'Please Select 1 or 2: ')
    while True:
        if code == '1':
            display_add_student_requirements()
            check_add_student_details()
        if code == '2':
            return

def display_show_student_options():
    print("===================================Show Student===================================")
    print("\t \u2666 1. Show All Students")
    print("\t \u2666 2. Show Students by Name")
    print("\t \u2666 3. Show Students by ID")
    print("\t \u2666 4. Other Return")
    code = input(f'Please Select 1 - 4: ')
    if code == '1':
        student_table.show_all_students()
    if code == '2':
        name = input('Please Enter Student Name to Display: ')
        student_table.show_students_by_name(name)
        pass
    if code == '3':
        name = input('Please Enter Student ID to Display: ')
        student_table.show_students_by_id(name)
    if code == '4':
        return

def modify_student():
    print("===================================Modify Student===================================")
    m = input("Please enter Student ID to Modify: ")
    student = s_session.query(Students).filter(Students.id == m).first()
    if student is None:
        print("\t \u274C No record found!")
        return
    else:
        new_age = input(f"New Age (press Enter without modification): ")
        while True:
            if new_age == '':
                break
            elif not custom_tools.age_check(new_age):
                print("\t \u274C Invalid student age!")
                new_age = int(input("Please Enter Student's Age: "))
            else:
                s_session.execute(update(Students).where(Students.id == m).values(age=new_age))
                s_session.commit()
                break
        new_major = input(f"New Major (press Enter without modification): ").upper()
        while True:
            if new_major == '':
                break
            elif not custom_tools.major_check(new_major):
                print("\t \u274C Invalid student major!")
                new_major = input("Please enter Student's Major: ").upper()
            else:
                s_session.execute(update(Students).where(Students.id == m).values(major=new_major))
                s_session.commit()
                break
        new_phone = input(f"New Phone (press Enter without modification to return): ")
        while True:
            if new_phone == '':
                break
            elif not custom_tools.phone_check(new_age):
                print("\t \u274C Invalid student phone!")
                new_phone = input("Please enter Student's Phone: ")
            else:
                s_session.execute(update(Students).where(Students.id == m).values(phone=new_phone))
                s_session.commit()
                break
        print("\t \u2714 Record modified successfully")

def delete_student_options():
    print("===================================Delete Student===================================")
    print("\t \u2666 1. Delete Students by Name")
    print("\t \u2666 2. Delete Students by ID")
    print("\t \u2666 3. Other Return")
    code = input(f'Please Select 1 - 3: ')
    if code == '1':
        name = input('Please Enter Student Name to Delete: ')
        student_table.delete_student_by_name(name)
    if code == '2':
        id = input('Please Enter Student ID to Delete: ')
        student_table.delete_student_by_id(id)
    if code == '3':
        return

def display_query_student_scores():
    print("===================================Query Student Scores===================================")
    print("\t \u2666 1. Display Student Score by Name")
    print("\t \u2666 2. Update Student Score by ID")
    print("\t \u2666 3. Other Return")
    code = input(f'Please Select 1 - 3: ')
    if code == '1':
        name = input('Please Enter Student Name to Display the Score: ')
        score_table.display_student_score_by_name(name)
    if code == '2':
        id = input('Please Enter Student ID to Update the Score: ')
        score_table.update_student_score_by_ID(id)
    if code == '3':
        return

def return_to_previous_menu():
    return first_menu.start()

def read_updated_student_txt(username):
    new = custom_tools.read_file('student.txt')
    content = custom_tools.cus_input(new, username)
    while True:
        code = input (content + '\nPlease select (1 - 6): ')
        if code == '1':
            display_add_student_requirements()
            check_add_student_details()
            # display_add_student_options()
        elif code == '2':
            display_show_student_options()
        elif code == '3':
            modify_student()
        elif code == '4':
            delete_student_options()
        elif code == '5':
            display_query_student_scores()
        elif code == '6':
            return_to_previous_menu()
        else:
            print('\t \u274C Invalid input')


if __name__ == '__main__':
    read_updated_student_txt()
