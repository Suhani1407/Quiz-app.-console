import getpass
import random
import os

class Registration:
    def __init__(self, file_path="users.txt"):
        self.file_path = file_path

    def register(self):
        name = input("Welcome! Please enter your name: ")
        email = input("Enter your email: ")
        password = getpass.getpass("Enter your password: ")
        
        # Store user data in a file
        with open(self.file_path, "a") as file:
            file.write(f"{name},{email},{password}\n")
        
        print(f"Registration successful! Hello, {name}!")

    def display_details(self):
        if not os.path.exists(self.file_path):
            print("No registered users found.")
            return

        print("Registered users:")
        with open(self.file_path, "r") as file:
            for line in file:
                name, email, _ = line.strip().split(",")
                print(f"Name: {name}, Email: {email}")


def authenticate(file_path, username, password):
    if not os.path.exists(file_path):
        return False

    with open(file_path, "r") as file:
        for line in file:
            name, email, stored_password = line.strip().split(",")
            if (username == name or username == email) and password == stored_password:
                return True
    return False


# Quiz data
quiz_data = {
    "Python": [
        {"question": "Who created Python?", "options": ["Guido van Rossum", "Bjarne Stroustrup", "Linus Torvalds", "Larry Wall"], "answer": "Guido van Rossum"},
        {"question": "What is the print function used for in Python?", "options": ["To display output", "To take input", "To store data", "To analyze data"], "answer": "To display output"},
        {"question": "What is the use of the len() function in Python?", "options": ["To calculate length", "To calculate size", "To calculate sum", "To calculate average"], "answer": "To calculate length"},
    ],
    "DBMS": [
        {"question": "What is DBMS?", "options": ["Database Management System", "Data Base Management System", "Database Management Services", "Data Base Management Services"], "answer": "Database Management System"},
        {"question": "Which DBMS is open-source?", "options": ["MySQL", "Oracle", "Microsoft SQL Server", "MongoDB"], "answer": "MySQL"},
    ],
    "DSA": [
        {"question": "What is DSA?", "options": ["Data Structure Algorithm", "Data Science Algorithm", "Database System Architecture", "Digital Signal Algorithm"], "answer": "Data Structure Algorithm"},
        {"question": "Which data structure is suitable for searching?", "options": ["Array", "Linked List", "Stack", "Hash Table"], "answer": "Hash Table"},
    ],
}


def quiz(subject):
    questions = quiz_data[subject]
    random.shuffle(questions)
    score = 0
    for question in questions:
        print(question["question"])
        for i, option in enumerate(question["options"]):
            print(f"{i+1}. {option}")
        try:
            answer_index = int(input("Enter answer number: ")) - 1
            if question["options"][answer_index] == question["answer"]:
                score += 1
        except (ValueError, IndexError):
            print("Invalid choice, moving to the next question.")
    print(f"Your score is {score}/{len(questions)}")


def main():
    file_path = "users.txt"
    print("1. Register\n2. Login")
    choice = input("Enter your choice: ")
    reg = Registration(file_path)

    if choice == "1":
        reg.register()
        return main()
    elif choice == "2":
        username = input("Enter username (name/email): ")
        password = getpass.getpass("Enter password: ")
        if authenticate(file_path, username, password):
            print("Login successful!")
            print("Select subject:")
            print("1. Python")
            print("2. DBMS")
            print("3. DSA")
            subjects = {"1": "Python", "2": "DBMS", "3": "DSA"}
            subject_choice = input("Enter subject number: ")
            subject = subjects.get(subject_choice)
            if subject:
                quiz(subject)
                play_again = input("Do you want to play again? (yes/no): ")
                if play_again.lower() == "yes":
                    main()
                else:
                    print("Thank you for playing!")
            else:
                print("Invalid subject choice.")
        else:
            print("Invalid login details.")
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
