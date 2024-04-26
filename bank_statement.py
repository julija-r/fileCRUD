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
    outcome
    bank_data_read = DictReader(bank_data)
    for row in bank_data_read:
        if row[Data].startswith("/1") and row["D/K" == "D"]:



