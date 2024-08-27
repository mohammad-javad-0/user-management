## PyQt6 User Management Application

### Description
This PyQt6 application is a simple user management system that allows users to sign up and log in using an email, username, and password. User data is stored in a CSV file for persistent storage, ensuring that user information is maintained across sessions.

### Features
- **User Sign Up**: Register a new user with email, username, and password.
- **User Login**: Log in existing users by verifying credentials.
- **Data Validation**: Ensures email and username uniqueness and password confirmation during sign-up.
- **Error Handling**: Custom error messages for user-related issues such as duplicate emails, usernames, and incorrect passwords.
- **Persistent Storage**: User information is stored in a CSV file (`dataset.csv`).

### Requirements
- Python 3.x
- PyQt6

### Installation
1. Clone the repository.

### Usage
1. Run the application with:
   ```
   python main.py
   ```
2. Use the "Sign Up" tab to create a new user.
3. Log in using the "Log In" tab with the registered credentials.

### Exception Handling
The application includes custom exceptions:
- **EmailExistsError**: Raised if the email already exists or is empty.
- **UserNameExistsError**: Raised if the username already exists or is empty.
- **PasswordError**: Raised if the password fields do not match or are empty.
- **UserNotFoundError**: Raised if the user credentials are incorrect during login.
