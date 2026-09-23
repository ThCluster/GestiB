import json
from pathlib import Path
import csv

# --- Partie 1 : créer boutique.json ---
boutique = {
    "nom": "Chez Awa",
    "proprietaire": "Awa Koné",
    "produits": [   
        {"nom": "Riz", "prix": 2500},
        {"nom": "Huile", "prix": 1800}
    ]
}

chemin_boutique = Path("data") / "boutique.json"

with open(chemin_boutique, "w", encoding="utf-8") as fichier:
    json.dump(boutique, fichier, ensure_ascii=False, indent=4)

# --- Partie 2 : écrire dans journal.txt ---
chemin_journal = Path("data") / "journal.txt"

with open(chemin_journal, "a", encoding="utf-8") as fichier:
    fichier.write("Vente enregistrée : Riz x5\n")
    
# --- Partie 3 : ajouter une vente dans ventes.csv ---
chemin_ventes = Path("data") / "ventes.csv"

# Est-ce que le fichier existe déjà ? (pour savoir si on doit écrire les titres)
fichier_existe = chemin_ventes.exists()

with open(chemin_ventes, "a", newline="", encoding="utf-8") as fichier:
    ecrivain = csv.writer(fichier)
    if not fichier_existe:
        ecrivain.writerow(["produit", "quantite", "prix"])  # titres, une seule fois
    ecrivain.writerow(["Riz", 5, 2500])