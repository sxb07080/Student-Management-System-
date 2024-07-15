from sqlalchemy.exc import IntegrityError

import second_menu
import custom_tools
import user_table
from sqlalchemy.orm import sessionmaker


u_engine = user_table.create_db()
u_session = sessionmaker(bind=u_engine)()

def display_registration_requirements():
    print("===================================Registration===================================")
    print("\t \u2666 1. Account name is between 3 and 6 letters long")
    print("\t \u2666 2. Account name's first letter must be capitalized")

@staticmethod
def display_password_requirements():
    print("===================================Password Requirements===================================")
    print("\t \u2666 1. Password must start with one of the following special characters !@#$%^&*")
    print("\t \u2666 2. Password must contain at least one digit, one lowercase letter, and one uppercase letter")
    print("\t \u2666 3. Password is between 6 and 12 letters long")

def get_password(pw):
    if custom_tools.password_check(pw) == True:
        print("\t \u2714 Registration completed!")
        return True
    else:
        print("\t \u274C Invalid Password!")
        return False

def login():
    a = input("Please enter your username: ")
    b = input("Please enter your password: ")
    if user_table.validate_credentials(a, b):
        return a
    else:
        print("\t \u274C Login Failed! Invalid credentials")
        return None

def start():
    content = custom_tools.read_file('welcome.txt')

    while True:
        code = input (content + '\nPlease select (1 - 3): ')

        if code == '1':
            username = login()
            if username:
                second_menu.read_updated_student_txt(username)

        elif code == '2':
            display_registration_requirements()
            while True:
                u_name = input("Please enter account name: ")
                if custom_tools.username_check(u_name) == True:
                    try:
                        user_table.add_user(u_name, "")  # Use an empty password for now
                        break
                    except IntegrityError:
                        print("\t \u274C Registration Failed! Account Already Exists")
                else:
                    print("\t \u274C Account Name Not Valid!")

            display_password_requirements()
            while True:
                u_password = input("Please enter your password: ")
                try:
                    user_table.update_user_password(u_name, u_password)
                    print("\u2713 Registration completed!")
                    break
                except Exception as e:
                    print(f"\t \u274C Error: {e}")

        elif code == '3':
            custom_tools.exit_system()
        else:
            print('\t \u274C Invalid input')


if __name__ == "__main__":
    start()
