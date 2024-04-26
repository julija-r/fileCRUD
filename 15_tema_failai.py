# 1. Susikurkite vieną keletą failų, pamėginkite juos nuskaityti taikant įvairas
# metodikas (viską vienu metu, po atskirą eilutę, sudedant į dictionary, ir
# pan.).

test1 = open('./test1.txt')
nuskaitytas_test1 = test1.read()
print(nuskaitytas_test1)
test1.close()

test1 = open("test1.txt","r+",encoding="utf8")
# test1.write("\nsninga balandi")
failas = test1.readline()
print(failas)
failas = test1.readline()
print(failas)
test1.close()

with open("test2.txt", "r+", encoding="utf8") as test2:
    for line in test2.readlines():
        print(line)

with open("test2.txt", "r+", encoding="utf8") as test2_1:
    print(test2_1.readlines())

# 3. Susikurkite duomenų failą, iš kurio nusiskaitytumėte informaciją apie
# automobilius. Išskaičiuokite keletą norimų dalykų (pvz. metų vidurkį) ir
# skaičiavimų rezultatus išveskite rezultatų faile.

year = []
year_sum = 0

with open("auto.txt", "r") as auto:
    lines = auto.read().split("\n")
    for line in lines[1:]:
        print(line.split(";")[1])
        year.append(int(line.split(";")[1]))
        year_sum += int(line.split(";")[1])
    print(year_sum/len(year))

# 4. Susikurkite pasirinktą csv failą ir užpildykite jį duomenimis. Pamėginkite jį
# nuskaityti su reader ir su DictReader. Iš šio failo duomenų išsiskaičiuokite
# bent 2 pasirinktus dalykus (pvz studentų vidurkių vidurkį, rasti žemiausią
# studentą, ar pan.). Nuskaitytus duomenis ir gautus rezultatus išveskite
# ekrane.

from csv import reader, writer, DictReader

with open("student.csv", "r") as student:
    student_reader = reader(student)
    for line in student_reader:
        print(line)

age_sum = 0
av_grade_sum = 0
len = 0

with open("student.csv",encoding="utf-8-sig") as student2:
    student2DictReader = DictReader(student2)
    for row in student2DictReader:
        print(row)
        print(row['vardas'],row['pavarde'])
        age_sum += int(row['amzius'])
        av_grade_sum += float(row['vidurkis'])
        len += 1
    print(f'average age = {age_sum/len}\naverage grade = {av_grade_sum/len}')

#Revolut statement 2023-09-01_2024-04-25

count_jan_transactions_out = 0
count_jan_transactions_in = 0
january_balance = 0

with open("revolut_account-statement_2023-09-01_2024-04-25.csv", encoding="utf-8-sig") as revolut_statement:
    revolut_statement_read = DictReader(revolut_statement)
    for row in revolut_statement_read:
        if row['Started Date'].startswith("1/"):
            if row['IN/OUT'] == "OUT":
                count_jan_transactions_out +=1
                january_balance -= float(row["amount abs"])
            else:
                count_jan_transactions_in += 1
                january_balance += float(row["amount abs"])
    print(f'OUT: {count_jan_transactions_out},\n'
          f'IN: {count_jan_transactions_in},\n'
          f'balance: {round(january_balance, 2)}')

with open("revolut_january.csv", "w") as revolut_january:
    revolut_january.write(f'count_jan_transactions_out,{count_jan_transactions_out}\n')
    revolut_january.write(f'count_jan_transactions_in,{count_jan_transactions_in}\n')
    revolut_january.write(f'january_balance,{round(january_balance, 2)}\n')