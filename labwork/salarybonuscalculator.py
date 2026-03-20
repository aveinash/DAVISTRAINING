# Function to calculate bonus
def calculate_bonus(salary, experience):
    if experience >= 10:
        bonus = salary * 0.20
    elif experience >= 5:
        bonus = salary * 0.10
    else:
        bonus = salary * 0.05
    
    total_salary = salary + bonus
    return bonus, total_salary


# Loop for multiple employees
n = int(input("Enter number of employees: "))

for i in range(n):
    salary = float(input(f"Enter salary of employee {i+1}: "))
    experience = int(input(f"Enter years of experience of employee {i+1}: "))
    
    bonus, total = calculate_bonus(salary, experience)
    
    print(f"Bonus: {bonus}")
    print(f"Total Salary: {total}")
    print()