import json

def convert(code, code2, montant):
    with open("codes_currency.json") as f:
        donnee_de_conversion = json.load(f)
    taux_echange = donnee_de_conversion[f"{code}\n"][f"{code2}"]
    return float(montant)*taux_echange

if __name__ == '__main__':
    print("#### CONVERSION DEVIS ####")
    montant = input("Entrer le montant: ")
    code = input("Entrer le code devis de ce montant: ")
    code2 = input("Enter sont nouveau code: ")
    nouveau_montant = convert(code, code2, montant)

    print(f"Resultat: {montant}{code} = {nouveau_montant}{code2}")
