
#find currencies
def currency(file, colName):
    currency = set()
    for row in file:
        currency.add(row[colName])
    print(currency)
    print("----------")

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
    print("----------")

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
    print("----------")

def outcomeByMonth(fileName, DateColName, ValueColName, IN_OUTcolName, valueIfOUT):
    outcome_jan = 0
    outcome_feb = 0
    outcome_mar = 0
    outcome_apr = 0
    outcome_may = 0
    outcome_jun = 0
    outcome_jul = 0
    outcome_aug = 0
    outcome_sep = 0
    outcome_oct = 0
    outcome_nov = 0
    outcome_dec = 0
    for row in fileName:
        if "-01-" in row[DateColName] and row[IN_OUTcolName] == valueIfOUT:
            outcome_jan += float(row[ValueColName])
        if "-02-" in row[DateColName] and row[IN_OUTcolName] == valueIfOUT:
            outcome_feb += float(row[ValueColName])
        if "-03-" in row[DateColName] and row[IN_OUTcolName] == valueIfOUT:
            outcome_mar += float(row[ValueColName])
        if "-04-" in row[DateColName] and row[IN_OUTcolName] == valueIfOUT:
            outcome_apr += float(row[ValueColName])
        if "-05-" in row[DateColName] and row[IN_OUTcolName] == valueIfOUT:
            outcome_may += float(row[ValueColName])
        if "-06-" in row[DateColName] and row[IN_OUTcolName] == valueIfOUT:
            outcome_jun += float(row[ValueColName])
        if "-07-" in row[DateColName] and row[IN_OUTcolName] == valueIfOUT:
            outcome_jul += float(row[ValueColName])
        if "-08-" in row[DateColName] and row[IN_OUTcolName] == valueIfOUT:
            outcome_aug += float(row[ValueColName])
        if "-09-" in row[DateColName] and row[IN_OUTcolName] == valueIfOUT:
            outcome_sep += float(row[ValueColName])
        if "-10-" in row[DateColName] and row[IN_OUTcolName] == valueIfOUT:
            outcome_oct += float(row[ValueColName])
        if "-11-" in row[DateColName] and row[IN_OUTcolName] == valueIfOUT:
            outcome_nov += float(row[ValueColName])
        if "-12-" in row[DateColName] and row[IN_OUTcolName] == valueIfOUT:
            outcome_dec += float(row[ValueColName])
    print(f'outcome_jan = {outcome_jan}\n'
          f'outcome_feb = {outcome_feb}\n'
          f'outcome_mar = {outcome_mar}\n'
          f'outcome_apr = {outcome_apr}\n'
          f'outcome_may = {outcome_may}\n'
          f'outcome_jun = {outcome_jun}\n'
          f'outcome_jul = {outcome_jul}\n'
          f'outcome_aug = {outcome_aug}\n'
          f'outcome_sep = {outcome_sep}\n'
          f'outcome_oct = {outcome_oct}\n'
          f'outcome_nov = {outcome_nov}\n'
          f'outcome_dec = {outcome_dec}')
    print("----------")

# def incomeByMonth(fileName, DateColName, ValueColName, IN_OUTcolName, valueIfIN):
#     income_jan = 0
#     income_feb = 0
#     income_mar = 0
#     income_apr = 0
#     income_may = 0
#     income_jun = 0
#     income_jul = 0
#     income_aug = 0
#     income_sep = 0
#     income_oct = 0
#     income_nov = 0
#     income_dec = 0
#     for row in fileName:
#         if "-01-" in row[DateColName] and row[IN_OUTcolName] == valueIfIN:
#             income_jan += float(row[ValueColName])
#         if "-02-" in row[DateColName] and row[IN_OUTcolName] == valueIfIN:
#             income_feb += float(row[ValueColName])
#         if "-03-" in row[DateColName] and row[IN_OUTcolName] == valueIfIN:
#             income_mar += float(row[ValueColName])
#         if "-04-" in row[DateColName] and row[IN_OUTcolName] == valueIfIN:
#             income_apr += float(row[ValueColName])
#         if "-05-" in row[DateColName] and row[IN_OUTcolName] == valueIfIN:
#             income_may += float(row[ValueColName])
#         if "-06-" in row[DateColName] and row[IN_OUTcolName] == valueIfIN:
#             income_jun += float(row[ValueColName])
#         if "-07-" in row[DateColName] and row[IN_OUTcolName] == valueIfIN:
#             income_jul += float(row[ValueColName])
#         if "-08-" in row[DateColName] and row[IN_OUTcolName] == valueIfIN:
#             income_aug += float(row[ValueColName])
#         if "-09-" in row[DateColName] and row[IN_OUTcolName] == valueIfIN:
#             income_sep += float(row[ValueColName])
#         if "-10-" in row[DateColName] and row[IN_OUTcolName] == valueIfIN:
#             income_oct += float(row[ValueColName])
#         if "-11-" in row[DateColName] and row[IN_OUTcolName] == valueIfIN:
#             income_nov += float(row[ValueColName])
#         if "-12-" in row[DateColName] and row[IN_OUTcolName] == valueIfIN:
#             income_dec += float(row[ValueColName])
#     print(f'income_jan = {income_jan}\n'
#           f'income_feb = {income_feb}\n'
#           f'income_mar = {income_mar}\n'
#           f'income_apr = {income_apr}\n'
#           f'income_may = {income_may}\n'
#           f'income_jun = {income_jun}\n'
#           f'income_jul = {income_jul}\n'
#           f'income_aug = {income_aug}\n'
#           f'income_sep = {income_sep}\n'
#           f'income_oct = {income_oct}\n'
#           f'income_nov = {income_nov}\n'
#           f'income_dec = {income_dec}')
#     print("----------")




