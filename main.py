from PyQt6 import QtCore, QtGui, QtWidgets
import sys
import csv
from module import *
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(530, 360)
        MainWindow.setStyleSheet("background-color:black;")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # create tabs
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 530, 360))
        self.tabWidget.setObjectName("tabWidget")

        self.tab = QtWidgets.QWidget()
        self.tab.setStyleSheet('''background-color:
        qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.590909,
        stop:0.254237 rgba(0, 0, 0, 255), stop:0.779661 rgba(201, 74, 105, 255))''')
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")

        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setStyleSheet('''background-color:
        qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.590909,
        stop:0.254237 rgba(0, 0, 0, 255), stop:0.779661 rgba(201, 74, 105, 255))''')
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        # create font for all labels and line edits
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(15)

        # create labels for log in tab
        self.login_email_label = QtWidgets.QLabel(parent=self.tab)
        self.login_email_label.setGeometry(QtCore.QRect(30, 50, 170, 30))
        self.login_email_label.setFont(font)
        self.login_email_label.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ForbiddenCursor))
        self.login_email_label.setStyleSheet("background-color: None;color:white;")
        self.login_email_label.setObjectName("login_email_label")

        self.login_name_label = QtWidgets.QLabel(parent=self.tab)
        self.login_name_label.setGeometry(QtCore.QRect(30, 110, 170, 30))
        self.login_name_label.setFont(font)
        self.login_name_label.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ForbiddenCursor))
        self.login_name_label.setStyleSheet("background-color: None;color:white;")
        self.login_name_label.setObjectName("login_name_label")

        self.login_password_label = QtWidgets.QLabel(parent=self.tab)
        self.login_password_label.setGeometry(QtCore.QRect(30, 170, 170, 30))
        self.login_password_label.setFont(font)
        self.login_password_label.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ForbiddenCursor))
        self.login_password_label.setStyleSheet("background-color: None;color:white;")
        self.login_password_label.setObjectName("login_password_label")

        # create line edits for log in tab
        self.login_email_lineEdit = QtWidgets.QLineEdit(parent=self.tab)
        self.login_email_lineEdit.setGeometry(QtCore.QRect(230, 50, 280, 30))
        self.login_email_lineEdit.setStyleSheet("color:white;background-color:black;")
        self.login_email_lineEdit.setObjectName("login_email_lineEdit")

        self.login_username_lineEdit = QtWidgets.QLineEdit(parent=self.tab)
        self.login_username_lineEdit.setGeometry(QtCore.QRect(230, 110, 280, 30))
        self.login_username_lineEdit.setStyleSheet("color:white;background-color:black;")
        self.login_username_lineEdit.setObjectName("login_username_lineEdit")

        self.login_password_lineEdit = QtWidgets.QLineEdit(parent=self.tab)
        self.login_password_lineEdit.setGeometry(QtCore.QRect(230, 170, 280, 30))
        self.login_password_lineEdit.setStyleSheet("color:white;background-color:black;")
        self.login_password_lineEdit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.login_password_lineEdit.setObjectName("login_password_lineEdit")

        # create labels for sign up tab
        self.signup_email_label = QtWidgets.QLabel(parent=self.tab_2)
        self.signup_email_label.setGeometry(QtCore.QRect(30, 30, 170, 30))
        self.signup_email_label.setFont(font)
        self.signup_email_label.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ForbiddenCursor))
        self.signup_email_label.setStyleSheet("background-color: None;color:white;")
        self.signup_email_label.setObjectName("signup_email_label")

        self.signup_name_label = QtWidgets.QLabel(parent=self.tab_2)
        self.signup_name_label.setGeometry(QtCore.QRect(30, 90, 170, 30))
        self.signup_name_label.setFont(font)
        self.signup_name_label.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ForbiddenCursor))
        self.signup_name_label.setStyleSheet("background-color: None;color:white;")
        self.signup_name_label.setObjectName("signup_name_label")

        self.signup_password_label = QtWidgets.QLabel(parent=self.tab_2)
        self.signup_password_label.setGeometry(QtCore.QRect(30, 150, 170, 30))
        self.signup_password_label.setFont(font)
        self.signup_password_label.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ForbiddenCursor))
        self.signup_password_label.setStyleSheet("background-color: None;color:white;")
        self.signup_password_label.setObjectName("signup_password_label")

        self.signup_password_again_label = QtWidgets.QLabel(parent=self.tab_2)
        self.signup_password_again_label.setGeometry(QtCore.QRect(30, 210, 170, 30))
        self.signup_password_again_label.setFont(font)
        self.signup_password_again_label.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ForbiddenCursor))
        self.signup_password_again_label.setStyleSheet("background-color: None;color:white;")
        self.signup_password_again_label.setObjectName("signup_password_again_label")

        # create line edits for sign up tab
        self.signup_email_lineEdit = QtWidgets.QLineEdit(parent=self.tab_2)
        self.signup_email_lineEdit.setGeometry(QtCore.QRect(230, 30, 280, 30))
        self.signup_email_lineEdit.setStyleSheet("color:white;background-color:black")
        self.signup_email_lineEdit.setObjectName("signup_email_lineEdit")

        self.signup_username_lineEdit = QtWidgets.QLineEdit(parent=self.tab_2)
        self.signup_username_lineEdit.setGeometry(QtCore.QRect(230, 90, 280, 30))
        self.signup_username_lineEdit.setStyleSheet("color:white;background-color:black;")
        self.signup_username_lineEdit.setObjectName("signup_username_lineEdit")

        self.signup_password_lineEdit = QtWidgets.QLineEdit(parent=self.tab_2)
        self.signup_password_lineEdit.setGeometry(QtCore.QRect(230, 150, 280, 30))
        self.signup_password_lineEdit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.signup_password_lineEdit.setStyleSheet("color:white;background-color:black;")
        self.signup_password_lineEdit.setObjectName("signup_password_lineEdit")

        self.signup_password_again_lineEdit = QtWidgets.QLineEdit(parent=self.tab_2)
        self.signup_password_again_lineEdit.setGeometry(QtCore.QRect(230, 210, 280, 30))
        self.signup_password_again_lineEdit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.signup_password_again_lineEdit.setStyleSheet("color:white;background-color:black;")
        self.signup_password_again_lineEdit.setObjectName("signup_password_again_lineEdit")

        # create font for push buttons
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(13)
        font.setBold(True)

        # create push buttons
        self.login_pushButton = QtWidgets.QPushButton(parent=self.tab)
        self.login_pushButton.setGeometry(QtCore.QRect(215, 270, 100, 25))
        self.login_pushButton.setFont(font)
        self.login_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.login_pushButton.setStyleSheet("color:white;")
        self.login_pushButton.setObjectName("login_pushButton")
        self.login_pushButton.clicked.connect(self.log_in)

        self.signup_pushButton = QtWidgets.QPushButton(parent=self.tab_2)
        self.signup_pushButton.setGeometry(QtCore.QRect(215, 270, 100, 25))
        self.signup_pushButton.setFont(font)
        self.signup_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.signup_pushButton.setStyleSheet("color:white;")
        self.signup_pushButton.setObjectName("signup_pushButton")
        self.signup_pushButton.clicked.connect(self.sign_up)


        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.login_name_label.setText(_translate("MainWindow", "User name"))
        self.login_password_label.setText(_translate("MainWindow", "Password"))
        self.login_pushButton.setText(_translate("MainWindow", "Log in"))
        self.login_email_label.setText(_translate("MainWindow", "Email"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Log in"))
        self.signup_name_label.setText(_translate("MainWindow", "User name"))
        self.signup_password_label.setText(_translate("MainWindow", "Password"))
        self.signup_password_again_label.setText(_translate("MainWindow", "Password again"))
        self.signup_email_label.setText(_translate("MainWindow", "Email"))
        self.signup_pushButton.setText(_translate("MainWindow", "Sign up"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Sign up"))

    def sign_up(self):
        user = {
            "email": self.signup_email_lineEdit.text(),
            "user_name": self.signup_username_lineEdit.text(),
            "password": self.signup_password_lineEdit.text(),
            "password2": self.signup_password_again_lineEdit.text(),
        }
        if check_user(user):
            with open("dataset.csv", "a", newline="") as f:
                cf = csv.writer(f)
                cf.writerow(user.values())
            show_messagebox("User signup", "User Signup successful", "info")


    def log_in(self):
        try:
            flag = True
            user = {
                "email": self.login_email_lineEdit.text(),
                "user_name": self.login_username_lineEdit.text(),
                "password": self.login_password_lineEdit.text(),
            }
            with open("dataset.csv", "r") as f:
                users = csv.reader(f)
                for u in users:
                    if u[0] == user["email"] and u[1] == user["user_name"] and u[2] == user["password"]:
                        flag = False
                        break
            if flag:
                raise UserNotFoundError("User not found")
        except Exception as err:
            show_messagebox(str(err.__class__.__name__), str(err), "error")
        else:
            show_messagebox("User found", "User Login successful", "info")



if __name__ == "__main__":
    check_file()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
