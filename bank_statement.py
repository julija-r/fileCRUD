#uždaviniams spręsti kurkite savo funkcijas, pasidarykite taip, kad būtų patogu dirbti.
# kokios valiutos buvo naudotos?
# kiek income, outcome?(ignoruojant valiutas)
# kiek income, outcome pagal kiekvieną valiutą?
# kiek buvo išleista kiekvieną mėnesį?
# kiek buvo uždirbta kiekvieną mėnesį?
#koks pinigų likutis kiekvieno mėnesio gale? (sausio pradžioje likutis buvo 0.00)(ignoruojant valiutas)
#koks pinigų likutis kiekvieno mėnesio gale? (sausio pradžioje likutis buvo 0.00) pagal kiekvieną valiutą?
#atvaizduokite per procentinę išraišką pamėnesiui pajamas ir išlaidas procentine išraiška: (žemiau pvz)
#-- sausis:
#-- -- income:
#-- -- Eur: 29%
#-- -- DK: 0%
#-- -- outcome:
#-- -- Eur: 36%
#-- -- DK: 19%

import bank_statement_functions as stmt
from csv import DictReader


# kokios valiutos buvo naudotos?
with open("sampleData.csv") as bank_data:
    bank_data_read = DictReader(bank_data)
    stmt.currency(bank_data_read, "Valiuta")

# kiek income, outcome?(ignoruojant valiutas)

with open("sampleData.csv") as bank_data:
    bank_data_read = DictReader(bank_data)
    stmt.incomeOutcome(bank_data_read, "Suma","D/K", "K", "D")


# kiek income, outcome pagal kiekvieną valiutą?

with open("sampleData.csv") as bank_data:
    bank_data_read = DictReader(bank_data)
    stmt.incomeOutcomeEUR_GBP(bank_data_read, "Suma", "D/K",
                              "K", "D", "Valiuta")

# kiek buvo išleista kiekvieną mėnesį?

with open("sampleData.csv") as bank_data:
    bank_data_read = DictReader(bank_data)
    stmt.outcomeByMonth(bank_data_read, "Data", "Suma", "D/K", "D")

# kiek buvo uždirbta kiekvieną mėnesį?
# with open("sampleData.csv") as bank_data:
#     bank_data_read = DictReader(bank_data)
#     stmt.incomeByMonth(bank_data_read, "Data", "Suma", "D/K", "K")

#koks pinigų likutis kiekvieno mėnesio gale? (sausio pradžioje likutis buvo 0.00)(ignoruojant valiutas)


import csv
balance = {}

with open('sampleData.csv') as bank_data:
    bank_data_read = csv.DictReader(bank_data)
    for row in bank_data_read:
        date = row["Data"]
        month = date.split("-")[1]
        sum = float(row["Suma"])
        in_out = row["D/K"]
        if month not in balance:
            balance[month] = 0.0
        if in_out == "K":
            balance[month] += sum
        else:
            balance[month] -= sum

print("Balansas kiekvieno mėnesio gale:")
for month, final_sum in balance.items():
    print(f"{month}: {final_sum}")

#koks pinigų likutis kiekvieno mėnesio gale? (sausio pradžioje likutis buvo 0.00) pagal kiekvieną valiutą?

balance = {}

with open('sampleData.csv') as bank_data:
    bank_data_read = csv.DictReader(bank_data)
    for row in bank_data_read:
        date = row["Data"]
        months = date.split("-")[1]
        suma = float(row["Suma"])
        in_out = row["D/K"]
        currency = row["Valiuta"]
        if months not in balance:
            balance[months] = {}
        if currency not in balance[months]:
            balance[months][currency] = 0.0
        if in_out == "K":
            balance[months][currency] += sum
        else:
            balance[months][currency] -= sum

print("Balansas kiekvieno mėnesio gale:")
for months, sum_eom in balance.items():
    print(f"{months}:")
    for currency, balance in sum_eom.items():
        print(f'{currency}: {balance}')

#atvaizduokite per procentinę išraišką pamėnesiui pajamas ir išlaidas procentine išraiška: (žemiau pvz)
#-- sausis:
#-- -- income:
#-- -- Eur: 29%
#-- -- DK: 0%
#-- -- outcome:
#-- -- Eur: 36%
#-- -- DK: 19%
