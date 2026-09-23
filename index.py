import pandas as pd

# Données brutes remplies de petites erreurs !
donnees = {
    "produit": ["  garba ", "ALLOCO", "  garba ", "Kedjenou", None],  # Espaces, minuscules, doublon et trou !
    "prix": [1000, 500, 1000, 2500, 1500],
    "quantite": [30, 50, 30, None, 10]  # Un trou (None = NaN) !
}

df = pd.DataFrame(donnees)
print("--- TABLEAU DE DÉPART ---")
print(df)


# Enlever les espaces avant/après et mettre en majuscules
df["produit"] = df["produit"].str.strip().str.upper()


# Enlever les espaces avant/après et mettre en majuscules
df["produit"] = df["produit"].str.strip().str.upper()

# Remplir la quantité manquante par 0
df["quantite"] = df["quantite"].fillna(0)

# Supprimer les lignes strictement identiques
df = df.drop_duplicates()

# Calcul du chiffre d'affaires
df["ca"] = df["prix"] * df["quantite"]

# Trier par prix du plus grand au plus petit (ascending=False)
df = df.sort_values(by="prix", ascending=False)

print("\n--- TABLEAU NETTOYÉ ET TRIÉ ---")
print(df)