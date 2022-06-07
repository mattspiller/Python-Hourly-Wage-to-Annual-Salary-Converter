# Author: Matt Spiller
# Updated: June 7, 2022

def wageToSalaryCalculator():
    print("Enter hourly wage: ", end='')
    wage = float(input())

    print("Enter hours worked per week: ", end='')
    weeklyHours = int(input())

    print("Enter vacation days per year: ", end='')
    vacationDays = int(input())

    annualSalary = wage * weeklyHours * (52 - float(vacationDays) / 7.0)

    print("Annual Salary: ", annualSalary)
    runAgainPrompt()


def runAgainPrompt():
    print("Would you like to do another calculation? (y,n): ", end='')
    runAgain = input()

    while runAgain != "y" and runAgain != "n":
        print("Response must be 'y' or 'n'. Would you like to do another calculation? (y,n): ", end='')
        runAgain = input()

    if runAgain == "y":
        wageToSalaryCalculator()
    else:
        return


wageToSalaryCalculator()
