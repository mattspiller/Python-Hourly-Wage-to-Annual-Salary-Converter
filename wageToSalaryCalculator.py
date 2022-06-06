print("Enter hourly wage: ", end='')
wage = float(input())

print("Enter hours worked per week: ", end='')
weeklyHours = int(input())

print("Enter vacation days per year: ", end='')
vacationDays = int(input())

annualSalary = wage * weeklyHours * (52 - float(vacationDays)/7.0)

print("Annual Salary: ", annualSalary)
