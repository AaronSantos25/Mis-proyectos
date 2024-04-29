class User:
    def __init__(self, name, age, position, years_in_company, salary, dni, phone):
        self.name = name
        self.age = age
        self.position = position
        self.years_in_company = years_in_company
        self.salary = salary
        self.dni = dni
        self.phone = phone

class UserManager:
    def __init__(self):
        self.users = []

    def register_user(self):
        name = input("Enter name: ")
        age = input("Enter age: ")
        position = input("Enter position: ")
        years_in_company = input("Enter years in company: ")
        salary = input("Enter salary: ")
        dni = input("Enter DNI: ")
        phone = input("Enter phone number: ")

        user = User(name, age, position, years_in_company, salary, dni, phone)
        self.users.append(user)
        print("User registered successfully.")

    def search_user(self, name):
        for user in self.users:
            if user.name == name:
                return user
        return None

    def modify_user(self):
        name = input("Enter name of the user to modify: ")
        user = self.search_user(name)
        if user:
            print("Enter new user details (leave blank to keep previous value):")
            new_name = input(f"New name [{user.name}]: ") or user.name
            new_age = input(f"New age [{user.age}]: ") or user.age
            new_position = input(f"New position [{user.position}]: ") or user.position
            new_years = input(f"New years in company [{user.years_in_company}]: ") or user.years_in_company
            new_salary = input(f"New salary [{user.salary}]: ") or user.salary
            new_dni = input(f"New DNI [{user.dni}]: ") or user.dni
            new_phone = input(f"New phone number [{user.phone}]: ") or user.phone

            user.name = new_name
            user.age = new_age
            user.position = new_position
            user.years_in_company = new_years
            user.salary = new_salary
            user.dni = new_dni
            user.phone = new_phone
            print(f"User '{user.name}' has been modified.")
        else:
            print("User not found.")

    def delete_user(self):
        name = input("Enter name of the user to delete: ")
        user = self.search_user(name)
        if user:
            self.users.remove(user)
            print(f"User '{user.name}' has been deleted.")
        else:
            print("User not found.")

    def display_users(self):
        print("User List:")
        for user in self.users:
            print(f"Name: {user.name}, Age: {user.age}, Position: {user.position}, Years in Company: {user.years_in_company}, Salary: {user.salary}, DNI: {user.dni}, Phone: {user.phone}")

user_manager = UserManager()

while True:
    print("--- MENU ---")
    print("1. Register User")
    print("2. Modify User")
    print("3. Delete User")
    print("4. Display Users")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        user_manager.register_user()
    elif choice == "2":
        user_manager.modify_user()
    elif choice == "3":
        user_manager.delete_user()
    elif choice == "4":
        user_manager.display_users()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")
