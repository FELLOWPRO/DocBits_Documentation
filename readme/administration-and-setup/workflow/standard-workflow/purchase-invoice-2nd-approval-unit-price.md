# Facture d’achat : deuxième approbation du prix unitaire

Cet exemple de workflow dirige une facture d’achat vers un utilisateur chargé d’examiner un écart de prix unitaire. Les noms ci-dessous sont les expressions techniques de l’exemple ; ils ne définissent pas une configuration obligatoire pour toutes les organisations.

## Conditions

* **Document Type is Invoice** : limiter le déclencheur aux factures.
* **Document Status is Pending Second Approval** : traiter les documents au statut de deuxième approbation prévu par l’exemple.
* **Document Field Invoice Sub Type is Equals Purchase Invoice** : limiter le sous-type à la facture d’achat.
* **Logic Unit Price in order confirmation Not Equals purchase order** : examiner le cas où la comparaison configurée entre confirmation et commande signale un écart de prix unitaire.

Vérifiez les champs, les unités et les données de commande utilisés par cette comparaison. Son résultat ne prouve pas à lui seul une erreur comptable ou une fraude.

## Action et repli

**Assign user from field Buyer Name, use user User as fallback** affecte le document à l’utilisateur résolu depuis `Buyer Name`, avec l’utilisateur explicitement configuré comme repli. `User` représente ici le paramètre de repli ; ce n’est pas une garantie qu’un administrateur sera choisi automatiquement.

L’affectation demande un examen. Elle ne vaut ni approbation, ni correction du prix, ni exportation. Un champ vide, une identité non résolue ou un repli invalide doit être vérifié dans votre configuration.

## Vérifier l’exemple

Testez un écart avec un acheteur résoluble, puis un acheteur absent avec un repli valide. Contrôlez l’affectation réelle du document. Ajoutez un cas sans écart et un cas avec repli invalide pour vérifier les limites. Ces tests décrivent les contrôles à effectuer ; ils n’ont pas été exécutés dans cette page.
