# Functions:
def find_best_savings_rate(annual_salary):
    # Variables:
    total_cost = 1000000
    monthly_salary = annual_salary / 12
    portion_down_payment = 0.25 * total_cost
    semi_annual_raise = 0.07
    r = 0.04

    # Calculate how long it will take you to save enough money to make the down payment:
    months = 36
    low = 0
    high = 10000
    steps_bisection = 0

    # Check if it's possible to pay with given salary, assume portion_saved = 1:
    max_savings = 0

    for month in range(months):
        # Add monthly return value:
        max_savings *= (1 + r / 12)

        # Raise salary every six months:
        if month % 6 == 0 and month != 0:
            monthly_salary *= (1 + semi_annual_raise)

        # Add portion saved from monthly salary:
        max_savings += monthly_salary

    if max_savings < portion_down_payment:
        print("It is not possible to pay the down payment in three years.")
        return

    # If possible:
    while True:
        monthly_salary = annual_salary / 12
        current_savings = 0
        i = (high + low) // 2
        portion_saved = i / 10000

        for month in range(months):
            # Add monthly return value:
            current_savings *= (1 + r/12)

            # Raise salary every six months:
            if month % 6 == 0 and month != 0:
                monthly_salary *= (1 + semi_annual_raise)

            # Add portion saved from monthly salary:
            current_savings += monthly_salary * portion_saved

        steps_bisection += 1

        if portion_down_payment - 100 < current_savings < portion_down_payment + 100:
            best_savings_rate = portion_saved
            print("Best savings rate:", best_savings_rate)
            print("Steps in bisection search:", steps_bisection)
            return best_savings_rate
        elif current_savings > portion_down_payment:
            high = i
        else:
            low = i


# Inputs:
starting_salary = float(input("Enter the starting salary: "))

# Call function:
find_best_savings_rate(starting_salary)
