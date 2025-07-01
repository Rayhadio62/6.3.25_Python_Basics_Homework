    # Define calculate budget
def calculate_budget():
    # User input for monthly income
    income = float(input("Enter your monthly income: $"))

    # User input for 3 expenses
    housing_costs = float(input("Enter your monthly housing costs expense: $"))
    food = float(input("Enter your monthly food expense: $"))
    electricity = float(input("Enter your monthly electricity expense: $"))

    # Calculations for the total expenses and any remaining money
    total_expenses = housing_costs + food + electricity
    remaining_money = income - total_expenses

    # Budget advice
    if remaining_money < 0:
        advice = "You're iverspending! Cut back on expanses."
    elif remaining_money < 100:
        advice = "Your budget is tight. Be careful with spending"
    else:
        advice = "Great job! you have money left over."

    # Formatted summary
    print("\n=== Budget Summary ===")
    print(f"Monthly Income:         ${income:.2f}")
    print(f"Total Expenses:         ${total_expenses:.2f}")
    print(f" - Housing Costs:       ${housing_costs:.2f}")
    print(f" - Food:                ${food:.2f}")
    print(f" - Electricity:         ${electricity:.2f}")
    print(f"Remaining Money:        ${remaining_money:.2f}")
    print(f"Advice:                 {advice}")

# Call the function
calculate_budget()