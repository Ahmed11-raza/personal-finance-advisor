def get_user_input():
    print("=== Personal Finance Advisor (Pakistan-focused) ===\n")
    income = float(input("Enter your monthly income (PKR): "))
    
    print("\nEnter your monthly expenses (main categories):")
    expenses = {}
    categories = ["Food", "Rent/Housing", "Transport", "Utilities", "Entertainment", "Other"]
    
    total_exp = 0
    for cat in categories:
        while True:
            try:
                amount = float(input(f"{cat}: "))
                if amount < 0:
                    print("Please enter a positive number.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
        expenses[cat] = amount
        total_exp += amount
    
    goal = float(input("\nYour monthly savings goal (PKR): "))
    
    return income, expenses, total_exp, goal


def analyze_finances(income, expenses, total_exp, goal):
    remaining = income - total_exp
    advice = []
    
    if remaining <= 0:
        advice.append("⚠️ DANGER: Your expenses are higher than or equal to your income!")
        advice.append("Reduce spending immediately — start with high categories like Food or Entertainment.")
    else:
        advice.append(f"Remaining after expenses: {remaining:,.0f} PKR")
        
        # Percentage-based smart advice
        if total_exp / income > 0.80:
            advice.append("Warning: You spend >80% of income — this is risky long-term.")
        if expenses.get("Food", 0) / income > 0.35:
            advice.append("Food spending high (>35%) — consider meal prepping to save.")
        if expenses.get("Entertainment", 0) / income > 0.15:
            advice.append("Entertainment high — try low-cost or free activities.")
        
        if remaining >= goal:
            advice.append("✅ You're on track! You can meet your savings goal this month.")
        else:
            months_estimate = goal / remaining if remaining > 0 else float('inf')
            if months_estimate != float('inf'):
                advice.append(f"At current rate, reaching your goal will take approx. {months_estimate:.1f} months.")
            else:
                advice.append("Goal impossible with current negative balance — cut expenses first.")
    
    return advice, remaining


# Run the program
if __name__ == "__main__":
    income, expenses, total_exp, goal = get_user_input()
    advice_list, remaining = analyze_finances(income, expenses, total_exp, goal)
    
    print("\n" + "="*50)
    print("YOUR FINANCIAL ADVICE SUMMARY:")
    for line in advice_list:
        print("→ " + line)
    print("="*50)
