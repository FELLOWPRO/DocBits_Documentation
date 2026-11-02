# Remises

## **Aperçu**

Si votre tableau extrait contient la colonne **Remise** ou **Pourcentage de remise**, **DocBits** appliquera automatiquement la remise correspondante au Prix unitaire lors du traitement dans l'écran de [**correspondance de bon de commande**](./).

## Exceptions

Les remises ne seront pas appliquées automatiquement lorsque la fonctionnalité de correspondances multiples est utilisée. Plus d'informations sur la fonctionnalité de correspondances multiples peuvent être trouvées [ici](./#correspondances-multiples).

## Calcul de la remise

Lorsqu'une **Remise** est présente, le prix unitaire remisé est calculé en soustrayant le montant de la remise du prix unitaire :

```
UNIT_PRICE_DISCOUNTED = UNIT_PRICE - DISCOUNT
```

## Calcul du pourcentage de remise

Lorsqu'un **Pourcentage de remise** est présent, le prix unitaire remisé est calculé en utilisant la formule suivante :

```
UNIT_PRICE_DISCOUNTED = UNIT_PRICE * (1 - DISCOUNT_PERCENT / 100)
```

## Arrondi

Tous les résultats de prix unitaire remisé sont arrondis à quatre décimales pour garantir la cohérence dans le traitement en aval.
