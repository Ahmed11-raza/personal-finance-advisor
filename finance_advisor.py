def get_user_input():
    print("=== Personal Finance Advisor (Pakistan-focused) ===\n")
    income = float(input("Enter your monthly income (PKR): "))
    
    print("\nEnter your monthly expenses (main categories):")
    expenses = {}
    categories = ["Food", "Rent/Housing", "Transport", "Utilities", "Entertainment", "Other"]
    
    total_exp = 0
    for cat in categories:
        amount = float(input(f"{cat}: "))
        expenses[cat] = amount
        total_exp += amount
    
    goal = float(input("\nYour monthly savings goal (PKR): "))
    
    return income, expenses, total_exp, goal


def analyze_finances(income, expenses, total_exp, goal):
    remaining = income - total_exp
    advice = []
    
    if remaining <= 0:
        advice.append("⚠️ DANGER: Your expenses are higher than or equal to your income!")
        advice.append("You need to reduce spending immediately.")
    else:
        advice.append(f"Remaining after expenses: {remaining:,.0f} PKR")
        
        # Simple rule-based "AI" advice
        if total_exp / income > 0.8:
            advice.append("You spend more than 80% of income — risky situation!")
        if expenses.get("Food", 0) / income > 0.35:
            advice.append("Food expenses high (>35%) — try to optimize meal planning.")
        if expenses.get("Entertainment", 0) / income > 0.15:
            advice.append("Entertainment spending high — consider free activities.")
        
        if remaining >= goal:
            advice.append("✅ Great! You're on track to meet your savings goal.")
        else:
            months_needed = (goal - remaining) / remaining if remaining > 0 else float('inf')
            advice.append(f"You may need to adjust goal or cut expenses.")
            if months_needed != float('inf'):
                advice.append(f"Estimated time to goal at current rate: ~{months_needed:.1f} months")
    
    return advice, remaining


# Main program
income, expenses, total_exp, goal = get_user_input()
advice_list, remaining = analyze_finances(income, expenses, total_exp, goal)

print("\n" + "="*50)
print("Your Financial Advice:")
for line in advice_list:
    print("→ " + line)
print("="*50)


