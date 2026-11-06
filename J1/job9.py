nom="ballon"
prix_unitaire=25.0
quantite_stock=10

print("Nom du Produit :", nom)
print("Prix unitaire :", prix_unitaire, "€")
print("Quantité en stock :", quantite_stock)

quantite_achat=int(input("Combien de produits voulez_vous acheter ? "))
quantite_stock=quantite_stock-quantite_achat
prix_unitaire=prix_unitaire*1.10

print("/n---Mise à jour du produit---")
print("Nom du produit :", nom)
print("Nouveau prix unitaire :", round(prix_unitaire, 2), "€")
print("quantitté restante en stock :", quantite_stock)
      