import bank_statement_functions as functions
from csv import DictReader
file_name = "sampleData.csv"  # Replace with your actual file name
currencies, income, outcome, outcome_monthly, income_monthly, balance, monthly_data = functions.transactions(file_name)

# 1. What currencies were used?
print("Currencies used:")
print(", ".join(currencies))
print("---------------------")

# 2. What's the income and outcome (ignoring currencies)?
print("Total income:")
print(f"{sum(income.values()):.2f}")

print("Total outcome:")
print(f"{sum(outcome.values()):.2f}")
print("---------------------")

# 3. What's the income and outcome for each currency?
print("Total income per curency:")
for currency, amount in income.items():
    print(f"{currency}: {amount:.2f}")

print("Total outcome per currency:")
for currency, amount in outcome.items():
    print(f"{currency}: {amount:.2f}")
print("---------------------")

# 4. What's monthly outcome?
print("Monthly outcome:")
for month, data in outcome_monthly.items():
    print(f"{month}:")
    for currency, amount in data.items():
        print(f"{currency}: {amount:.2f}")
    print("")
print("---------------------")

# 5. What's monthly income?
print("Monthly income:")
for month, data in income_monthly.items():
    print(f"{month}:")
    for currency, amount in data.items():
        print(f"{currency}: {amount:.2f}")
    print("")
print("---------------------")

# 6. What's monthly balance (at the beginning of January balance was 0.00) (ignoring currencies)?
print("Monthly balance:")
for month, data in balance.items():
    print(f"{month}: {sum(data.values())}")
print("---------------------")

# 7. What's the monthly balance (at the beginning of January balance was 0.00) per currency each month?
print("Monthly balance per currency:")
for month, data in balance.items():
    print(f"{month}:")
    for currency, amount in data.items():
        print(f" {currency}: {amount:.2f}")
print("---------------------")

# 8. What's the percentage of income and outcome for each month?
print("Percentage of income and outcome for each month over the period:")
functions.percentage_values(monthly_data, income, outcome)
