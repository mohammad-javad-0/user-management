from PyQt6.QtWidgets import QMessageBox
import os

class EmailExistsError(Exception):
    pass

class UserNameExistsError(Exception):
    pass

class PasswordError(Exception):
    pass

class UserNotFoundError(Exception):
    pass


def show_messagebox(title, message, state):
    msg = QMessageBox()
    msg.setStyleSheet('''
    QMessageBox {background-color:black;color:white;}
    QPushButton:hover {background-color: lightblue;color: black}"
    ''')
    if state == "error":
        QMessageBox.critical(msg, title, message)
    else:
        QMessageBox.information(msg, title, message)


def check_file():
    if "dataset.csv" not in os.listdir(os.path.dirname(os.path.abspath(__name__))):
        with open("dataset.csv", "a") as f:
            cf = csv.writer(f)
            cf.writerow(["email", "user_name", "password"])


def check_user(user):
    try:
        with open("dataset.csv", "r") as f:
            users = csv.reader(f)
            for u in users:
                if u[0] == user["email"] or user["email"] == "":
                    raise EmailExistsError("Email already exists or Email is empty")
                elif u[1] == user["user_name"] or user["user_name"] == "":
                    raise UserNameExistsError("User name already exists or User name is empty")
            if user["password"] == user["password2"] and user["password"] != "":
                return True
            raise PasswordError("A password is not the same as repeating a password or passwords is empty")
    except Exception as err:
        show_messagebox(str(err.__class__.__name__), str(err), "error")