import csv

# for questions 1-7
def transactions(file_name):
    income = {}
    outcome = {}
    monthly_data = {}
    currencies = set()

    with open(file_name, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            currency = row["Valiuta"]
            suma = float(row["Suma"])
            dk = row["D/K"]
            date = row["Data"]
            month = date[:7]  # Extract 'YYYY-MM'
            currencies.add(currency)

            # Initialize income and outcome dictionaries
            if currency not in income:
                income[currency] = 0.0
                outcome[currency] = 0.0

            if dk == "K":
                income[currency] += suma
            else:
                outcome[currency] += suma

            # Initialize monthly_data nested dictionary
            if month not in monthly_data:
                monthly_data[month] = {'income': {}, 'outcome': {}, 'balance': {}}

            if currency not in monthly_data[month]['income']:
                monthly_data[month]['income'][currency] = 0.0
                monthly_data[month]['outcome'][currency] = 0.0
                monthly_data[month]['balance'][currency] = 0.0

            if dk == "K":
                monthly_data[month]['income'][currency] += suma
                monthly_data[month]['balance'][currency] += suma
            else:
                monthly_data[month]['outcome'][currency] += suma
                monthly_data[month]['balance'][currency] -= suma

    outcome_monthly = {month: data['outcome'] for month, data in monthly_data.items()}
    income_monthly = {month: data['income'] for month, data in monthly_data.items()}
    balance = {month: data['balance'] for month, data in monthly_data.items()}

    return currencies, income, outcome, outcome_monthly, income_monthly, balance, monthly_data

# for question 8
def percentage_values(nested_dictionary, total_income, total_outcome):
    for month, data in nested_dictionary.items():
        print(f"{month}:")
        for dk, currencies in data.items():
            if dk != "balance":
                print(f" {dk}:")
                for currency, amount in currencies.items():
                    if dk == "income":
                        total = total_income.get(currency, 1)  # Total income for the currency
                    else:
                        total = total_outcome.get(currency, 1)  # Total outcome for the currency
                    if total != 0:
                        percentage = (amount / total) * 100
                    else:
                        percentage = 0
                    print(f"  {currency}: {amount} ({percentage:.2f}%)")