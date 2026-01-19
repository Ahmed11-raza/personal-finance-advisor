def financial_advice(income, expenses, savings_goal):
    remaining = income - expenses

    if remaining <= 0:
        return "Your expenses exceed or equal your income. Consider reducing non-essential spending."
    
    advice = f"After expenses, you have {remaining} remaining.\n"

    if remaining >= savings_goal:
        advice += "You are on track to meet your savings goal."
    else:
        advice += "You may need to adjust your savings goal or reduce expenses."

    return advice


# Example usage
monthly_income = 100000
monthly_expenses = 75000
savings_target = 20000

print(financial_advice(monthly_income, monthly_expenses, savings_target))
