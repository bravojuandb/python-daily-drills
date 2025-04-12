# Monthly budget summary. Tracking income, expenses and savings goal.

"""

Objectives: 
- Declare variables of the correct type (string, float, bool)
- Perform arithmetic with numeric values.
- Use type() to confirm variable types.
- Format output using f-strings and .format()
- Practice logic with an if statement

"""

name = "Juan"
monthly_income = 3000

monthly_rent = 850.00
monthly_savings_goal = 500

has_side_hustle = True

disposable_income = monthly_income - monthly_rent - monthly_savings_goal

print(
    f"Hello {name}, \n"
    f" With a monthly income of €{monthly_income:.2f},\n"
    f"   after paying €{monthly_rent:.2f} in rent,\n"
    f"     and saving €{monthly_savings_goal:.2f},\n"
    f"       you have €{disposable_income:.2f} left to spend.\n"
    f"         Side hustle active: {has_side_hustle}"
)

if disposable_income < 1000:
    print("Warning: you´re under the threshold")