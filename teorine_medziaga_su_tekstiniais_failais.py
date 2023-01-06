with open("failiuksas.txt", "w") as failas: # "w" skirta irasyti failui
    failas.write("ka tu, ka vakare")

with open("failiuksas.txt", "r") as failas: # "r" perskaito uzduota faila
    print(failas.read())

with open("failiuksas1.txt", "w", encoding="UTF-8") as failas1: # encoding = UTF=8 kad galima butu irasyti lietuviskas raides tame faile
    failas1.write("ką tu, ka vakare")

with open("failiuksas1.txt", "r", encoding="UTF-8") as failas1: # "r" perskaito uzduota faila
    print(failas1.read())

with open("failiuksas2.txt", "a", encoding="UTF-8") as failas2: # "a" vis prideda is naujo faila
    failas2.write("ką tu, ka vakare")

print("Justinas", end= "") # end= "" neleidzia perkelt kito printo i kita eilute, o \n leidzia perkelt i nauja eilute
print("Guzys", end="")
print("20")