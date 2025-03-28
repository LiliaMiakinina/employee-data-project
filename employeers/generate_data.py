import csv
from random import choice, randint
from faker import Faker

fake = Faker()
def generate_employee_data(num_employees: int):
    employees = []
    for _ in range(num_employees):
        name = fake.name()
        hiring_date = fake.date_this_decade()
        department = choice(['HR', 'IT', 'Sales', 'Marketing'])
        birthday = fake.date_of_birth(minimum_age=18, maximum_age=65).strftime('%Y-%m-%d')

        employee = {
            'name': name,
            'hiring_date': hiring_date,
            'department': department,
            'birthday': birthday
        }
        employees.append(employee)
    return employees
def write_to_csv(employees, filename='database.csv'):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['name', 'hiring_date', 'department', 'birthday'])
        writer.writeheader()
        writer.writerows(employees)
if __name__ == '__main__':
    employees = generate_employee_data(10)
    write_to_csv(employees)