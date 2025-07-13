# A script to calculate the projected savings with interest of a user

# Variables to receive user's monthly income and expenses respectively
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your monthly expenses: "))

# Calculating the monthly savings
monthly_savings = monthly_income - monthly_expenses

# calculating the projected savings and interest rate after 1 year
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print("Your monthly savings are:", "$",monthly_savings)
print("Projected savings after one year with interest, is:", "$",projected_savings)


