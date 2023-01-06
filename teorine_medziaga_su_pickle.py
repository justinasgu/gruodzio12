# import pickle
#
# a = 1024
#
# with open("a.pkl", "wb") as pickle_out: # "wb" irasyti i faila
#     pickle.dump(a, pickle_out) #dump yra irasyti i faila kad veiktu wb
#
#
# with open("a.pkl", "rb") as pickle_in: # "rb" perskaityti faila
#     naujas_a = pickle.load(pickle_in) # load kad veiktu rb
#
# print(naujas_a)

import pickle

while True:
    veiksmas = int(input("Pasirinkite veiksmą: 1 - peržiūrėti, 2 - įrašyti, 3 - išeiti"))
    if veiksmas == 1:
        try:
            with open("zmones.pkl", 'rb') as failas:
                print(pickle.load(failas))
        except:
            print("Nėra tokio failo")
            with open("zmones.pkl", 'wb') as failas:
                zmones = []
                pickle.dump(zmones, failas)
    if veiksmas == 2:
        with open("zmones.pkl", 'rb') as failas:
            zmones = pickle.load(failas)
            vardas = input("Įveskite naują vardą")
            with open("zmones.pkl", 'wb') as failas:
                zmones.append(vardas)
                pickle.dump(zmones, failas)
    if veiksmas == 3:
        print("Programa baigta")
        break