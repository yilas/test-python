capital = 1000
annee = 0
test = 1

while capital < 200000:
    capital *= 1.03
    annee += 1
    print(f"capital={capital:.2f}\tannee={annee}")

print(f"Nombre d'annees : {annee}")
