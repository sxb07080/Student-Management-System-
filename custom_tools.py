import re
import user_table
from sqlalchemy.orm import sessionmaker


u_engine = user_table.create_db()
u_session = sessionmaker(bind=u_engine)()

def read_file(file_name):
    with open(file_name, 'r',encoding='utf8') as f:
        return f.read()

def password_check(p):
    if not re.match(r'^[!@#$%^&*]', p):
        return False
    if not (re.search(r'\d', p) and re.search(r'[a-z]', p) and re.search(r'[A-Z]', p)):
        return False
    if not 6 <= len(p) <= 12:
        return False
    return True

def username_check(name):
    if 3 <= len(name) <= 6:
        if name[0].isupper():
            return True

def name_check(name):
    if not re.match(r'^[A-Z][a-z]* [A-Z][a-z]*$', name):
        return False
    if not all(len(part) >= 2 for part in name.split()):
        return False
    if any(char.isdigit() for char in name):
        return False
    return True

def phone_check(phone):
    return re.match(r'^\d{3}-\d{3}-\d{4}$', phone)

def age_check(age):
    age = int(age)
    return 0 < age < 100

def gender_check(gender):
    return gender.upper() in ['M', 'F', 'O']

def cus_input(current_value, username):
    return re.sub(r"%s", username, current_value)

def major_check(major):
    m = major.upper()
    if m.isalpha():
        return m

def exit_system():
    ans = input('Do you Want to Exit the System? Enter Y to confirm: ')
    if ans.upper() == 'Y':
        print('Exit the System...')
        exit()
