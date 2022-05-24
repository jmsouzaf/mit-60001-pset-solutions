# Inputs:
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

# Variables:
portion_down_payment = 0.25 * total_cost
monthly_salary = annual_salary / 12
r = 0.04

# Calculate how long it will take you to save enough money to make the down payment:
months = 0
current_savings = 0
while current_savings < portion_down_payment:
    # Add monthly return value:
    current_savings *= (1 + r/12)

    # Raise salary every six months:
    if months % 6 == 0 and months != 0:
        monthly_salary *= (1 + semi_annual_raise)

    # Add portion saved from monthly salary:
    current_savings += monthly_salary * portion_saved

    months += 1

print("Number of months:", months)