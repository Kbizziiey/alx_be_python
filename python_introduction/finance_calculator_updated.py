# A script to calculate the projected savings with interest of a user

# Variables to receive user's monthly income and expenses, duration of saving and interest rate respectivelt respectively
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your monthly expenses: "))
saving_duration = float(input("Enter the duration of the savings in months: "))
interest_rate = float(input("Enter the interest rate in %: "))

# TO convert the interest rate from percent into fraction
interest_rate_fraction = interest_rate / 100

# Calculating the monthly savings
monthly_savings = float(monthly_income - monthly_expenses)

# calculating the projected savings and interest rate after 1 year
projected_savings = float(monthly_savings * saving_duration + (monthly_savings * saving_duration * interest_rate_fraction))

print("Your monthly savings are:", monthly_savings)
print("Projected savings after one year with interest, is:", projected_savings)


