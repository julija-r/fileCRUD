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

