# importing
import os
import time
import json

# Data file name
DATA_FILE = "data.json"

# Initialize data lists
employees = []
Companies = []

# ==========================================
# ===== CLASSES DEFINITION (Moved Up) =====
# ==========================================

class Employee:
    def __init__(self, name, age, Id, salary, currency, rank, status):
        self.name = name
        self.age = age
        self.Id = Id
        self.salary = salary
        self.currency = currency
        self.rank = rank
        self.status = status

class Company:
    def __init__(self, name_company, Type, employees_number, Company_location, company_economics, Company_founding_date, company_id):
        self.name_company = name_company
        self.Type = Type
        self.employees_number = employees_number
        self.Company_location = Company_location
        self.company_economics = company_economics
        self.Company_founding_date = Company_founding_date
        self.company_id = company_id

# ==========================================
# ===== SYSTEM SAVE & LOAD FUNCTIONS =====
# ==========================================

def save_data():
    """Saves the current employees and companies lists to a JSON file."""
    data = {
        "employees": [
            {
                "name": emp.name,
                "age": emp.age,
                "Id": emp.Id,
                "salary": emp.salary,
                "currency": emp.currency,
                "rank": emp.rank,
                "status": emp.status
            } for emp in employees
        ],
        "Companies": [
            {
                "name_company": comp.name_company,
                "Type": comp.Type,
                "employees_number": comp.employees_number,
                "Company_location": comp.Company_location,
                "company_economics": comp.company_economics,
                "Company_founding_date": comp.Company_founding_date,
                "company_id": comp.company_id
            } for comp in Companies
        ]
    }
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def load_data():
    """Loads employees and companies from the JSON file if it exists."""
    global employees, Companies
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as file:
                data = json.load(file)
                
                # Load Employees
                for emp_data in data.get("employees", []):
                    employees.append(Employee(**emp_data))
                    
                # Load Companies
                for comp_data in data.get("Companies", []):
                    Companies.append(Company(**comp_data))
        except (json.JSONDecodeError, TypeError):
            # If the file is empty or corrupted, start fresh
            pass

# Function to Clear Screen
def Clear_Screen():
    os.system("cls" if os.name == "nt" else "clear")

# ==========================================
# ===== EMPLOYEE MANAGEMENT FUNCTIONS =====
# ==========================================

def add_an_employee():
    Clear_Screen()
    try:
        name = str(input("\nWhat's the name of the employee : \n"))
        age = int(input("\nHow old is the employee : \n"))
        Id = input("\nWhat's the Id of the employee : \n")
        salary = int(input("\nHow many is the salary of the employee : \n"))
        currency = input("\nWhat's the currency that the employee will receive their salary : \n")
        rank = input("\nWhat's the rank of the employee\n( Executive Leadership / Middle Management / First-line Management / Senior Staff / Entry-level Staff ) : \n")
        status = input("\nWhat's the status of the employee (working / vacation) : \n")

        new_employee = Employee(name, age, Id, salary, currency, rank, status)
        employees.append(new_employee)
        
        save_data()
        print("\n\nEmployee added successfully 👍")
    except ValueError:
        print("\nInvalid input! Employee not added. ❌")
    
    input("\nPress enter to continue...")
    Clear_Screen()

def Show_employees():
    Clear_Screen()
    if not employees:
        print("There aren't any employees.")
        input("\nPress enter to continue...")
        Clear_Screen() 
    else:
        print("===== employees list =====\n")
        for index, emp in enumerate(employees, start=1):
            print(f"\n[{index}]")
            print(f"Name : {emp.name}")
            print(f"Age : {emp.age}")
            print(f"ID : {emp.Id}")
            print(f"Salary : {emp.salary} {emp.currency}")
            print(f"Rank : {emp.rank}")
            print(f"Status : {emp.status}")
            print("_" * 30)

        num_emp = len(employees)
        if 0 < num_emp <= 15:
            print("\nGood, there are some employees 👍")
        elif 15 < num_emp <= 35:
            print("\nOh, there are many employees 👏")
        elif num_emp > 35:
            print("\nOh my gosh, how many employees! 🙀😯")

        input("\nPress enter to continue...")
        Clear_Screen()

def delete_employee():
    Clear_Screen()
    if not employees:
        print("There aren't any employees to delete ❌")
        input("\nPress enter to continue...")
        Clear_Screen()
    else:
        for index, emp in enumerate(employees, start=1):
            print(f"[{index}] Name: {emp.name} | ID: {emp.Id}")
            print("-" * 30)
        try:
            deleted_employee_number = int(input("\nEnter the number of the employee you want to delete : \n"))
            if 1 <= deleted_employee_number <= len(employees):
                removed_employee = employees.pop(deleted_employee_number - 1)
                save_data()
                print(f"\nThe employee {removed_employee.name} was removed successfully ⭐")
            else:
                print("\nCan't find an employee with this number ❌")
        except ValueError:
            print("\nPlease enter a valid number ❌")
        
        input("\nPress enter to continue : ")
        Clear_Screen()

# ==========================================
# ===== COMPANY MANAGEMENT FUNCTIONS =====
# ==========================================

def Add_Company():
    Clear_Screen()
    try:
        name_company = str(input("What's the name of the company : \n"))
        Type = str(input("What's the type of the company : \n"))
        employees_number = int(input("How many employees are in the company : \n"))
        Company_location = str(input("Where's the Company (country / city ) : \n"))
        company_economics = int(input("What is the valuation/economics of the company : \n"))
        Company_founding_date = input("When was the Company established : \n")
        company_id = input("What's the id of the company : \n")

        new_Company = Company(name_company, Type, employees_number, Company_location, company_economics, Company_founding_date, company_id)
        Companies.append(new_Company)
        
        save_data()
        print("\nCompany added successfully 👍")
    except ValueError:
        print("\nInvalid input ❌")
    
    input("\nPress enter to continue : ")
    Clear_Screen()

def SHOW_company_INFORMATIONS():
    Clear_Screen()
    if not Companies:
        print("There aren't any companies registered.")
    else:
        print("====== Companies ======")
        for master, Comp in enumerate(Companies, start=1):
            print(f"\n[{master}]")
            print(f"Name : {Comp.name_company}")
            print(f"Type : {Comp.Type}")
            print(f"How many employees : {Comp.employees_number}")
            print(f"Company location : {Comp.Company_location}")
            print(f"Company economics : {Comp.company_economics}")
            print(f"Company founding date : {Comp.Company_founding_date}")
            print(f"Company id : {Comp.company_id}")
            print("=" * 30)

        num_comp = len(Companies)
        if 0 < num_comp <= 2:
            print("\nGood, you have Companies 👍")
        elif 2 < num_comp <= 5:
            print("\nOh, you have many Companies 👏")
        elif num_comp > 5:
            print("\nOh my gosh, how many Companies you have 🙀😯")

    input("\nPress enter to continue...")
    Clear_Screen()

# ==========================================
# ===== MAIN MENU & EXECUTION =====
# ==========================================

def Main_Menu():
    # Load existing data on startup
    load_data()
    
    while True:
        Clear_Screen()
        print("========== MAIN MENU ==========")
        print("1. Add an Employee")
        print("2. Show All Employees")
        print("3. Delete an Employee")
        print("4. Add a Company")
        print("5. Show Company Information")
        print("6. Exit")
        print("===============================")
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            add_an_employee()
        elif choice == '2':
            Show_employees()
        elif choice == '3':
            delete_employee()
        elif choice == '4':
            Add_Company()
        elif choice == '5':
            SHOW_company_INFORMATIONS()
        elif choice == '6':
            print("\nAre you sure you want to leave? (Data is already saved automatically) ✅")
            leave = input("Press Y to leave and N to go back: ").strip().upper()
            if leave == "Y":
                Clear_Screen()
                print("3")
                time.sleep(1)
                Clear_Screen()
                print("2")
                time.sleep(1)
                Clear_Screen()
                print("1")
                time.sleep(1)
                Clear_Screen()
                print("\nGoodbye!")
                time.sleep(1)
                Clear_Screen()
                break
            else:
                Clear_Screen()
        else:
            print("\nInvalid choice! Please select between 1 and 6.")
            time.sleep(1)

if __name__ == "__main__":
    
    Main_Menu()
