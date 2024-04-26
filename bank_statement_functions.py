
#find currencies
def currency(file, colName):
    currency = set()
    for row in file:
        currency.add(row[colName])
    print(currency)

#calculate income and outcome
def incomeOutcome(file, colNameValue, IN_OUTcolName, valueIfIN, valueIfOUT):
    income = 0
    outcome = 0
    for row in file:
        if row[IN_OUTcolName] == valueIfOUT:
            outcome += float(row[colNameValue])
        if row[IN_OUTcolName] == valueIfIN:
            income += float(row[colNameValue])
    print(f'income = {income}, outcome = {outcome}')

def incomeOutcomeEUR_GBP(file, ValueColName, IN_OUTcolName, valueIfIN, valueIfOUT, CurrencyColName):
    income_EUR = 0
    outcome_EUR = 0
    income_GBP = 0
    outcome_GBP = 0
    for row in file:
        if row[IN_OUTcolName] == valueIfOUT and row[CurrencyColName] == "EUR":
            outcome_EUR += float(row[ValueColName])
        if row[IN_OUTcolName] == valueIfIN and row[CurrencyColName] == "EUR":
            income_EUR += float(row[ValueColName])
        if row[IN_OUTcolName] == valueIfOUT and row[CurrencyColName] == "GBP":
            outcome_GBP += float(row[ValueColName])
        if row[IN_OUTcolName] == valueIfIN and row[CurrencyColName] == "GBP":
            income_GBP += float(row[ValueColName])
    print(f'income EUR = {income_EUR}, outcome_EUR = {outcome_EUR}\n'
          f'income GBP = {income_GBP}, outcome_GBP = {outcome_GBP}')
