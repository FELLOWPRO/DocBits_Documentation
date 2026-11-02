# TransactionConfig Pro Template

## Configuration du traitement des documents financiers

_TransactionConfig Pro Template_ présente des exemples de mappage de documents financiers : factures, notes de débit et notes de crédit. Le gestionnaire de règles peut utiliser des règles et expressions `conflict_resolution` configurées pour déterminer les actions de traitement. Cette documentation ne prouve pas qu’un modèle prédéfini soit déployé dans votre environnement.

Les mappages de champs, les types de transactions et les décisions du processus doivent être configurés pour l’intégration Infor M3/LN concernée. Ces exemples expliquent cette configuration ; ils ne garantissent ni des résultats exacts, ni une intégration sans adaptation, ni la conformité aux normes financières internationales.

### Domaines de configuration

* **Mappage :** Définir les champs source et cible pour chaque type de transaction et vérifier les données produites.
* **Personnalisation :** Configurer les règles du processus métier et des approbations.
* **Automatisation :** Automatiser uniquement les décisions explicitement couvertes par les règles et expressions actives.
* **Intégration :** Vérifier le mappage d’export et les exigences du système Infor M3/LN cible.
* **Conformité :** Examiner séparément les exigences comptables et fiscales ; la configuration seule ne garantit pas la conformité juridique.

## Cas illustratifs de résolution des conflits

Le scénario suivant illustre un mappage configuré ; il ne constitue pas un modèle par défaut dont le déploiement aurait été vérifié. La sortie réelle, les montants, les signes et les types de documents dépendent des règles et expressions `conflict_resolution` actives, du mappage d’export et des décisions d’approbation. Toute note de débit ou de crédit décrite ci-dessous est soumise à cette configuration ; cet exemple ne garantit ni son émission automatique ni la conformité juridique.

### [Cas 1, 2, 3 : Quantité et prix unitaire dans la tolérance](case-1-2-3-quantity-and-unit-price-within-tolerance.md)

**Scénario:** La quantité et le prix facturés respectent les tolérances configurées par rapport au PO.

**Action illustrative:** Le mappage illustratif accepte les valeurs facturées et calcule quantité × prix unitaire.

### [Cas 4, 5 : Quantité dans la tolérance, prix hors tolérance (approuvé)](case-4-5-quantity-within-tolerance-unit-price-outside-tolerance-approved.md)

**Scénario:** La quantité respecte la tolérance ; l’écart de prix la dépasse et a été approuvé.

**Action illustrative:** Le mappage illustratif retient le prix du PO et affecte l’écart approuvé à des frais de ligne si cela est configuré.

### [Cas 6 : Quantité dans la tolérance, prix inférieur à la limite (rejeté)](case-6-quantity-within-tolerance-unit-price-outside-negative-tolerance-rejected.md)

**Scénario:** La quantité respecte la tolérance ; le prix est inférieur à la plage autorisée et a été rejeté.

**Action illustrative:** Le mappage illustratif retient le prix du PO. L’écart signé n’est pas automatiquement une note de crédit ; le type et le signe de l’ajustement dépendent du mappage.

### [Cas 7 : Quantité dans la tolérance, prix supérieur à la limite (rejeté)](case-7-quantity-within-tolerance-unit-price-outside-tolerance-positive-rejected.md)

**Scénario:** La quantité respecte la tolérance ; l’écart de prix positif a été rejeté.

**Action illustrative:** Le mappage illustratif retient le prix du PO. Toute note ou tout ajustement de l’écart dépend du mappage d’export.

### [Cas 8a, 9a : Quantité hors tolérance (approuvée), prix dans la tolérance](case-8a-9a-quantity-outside-tolerance-approved-unit-price-within-tolerance.md)

**Scénario:** L’écart de quantité est approuvé et le prix reste dans la tolérance.

**Action illustrative:** Le mappage illustratif utilise la quantité facturée approuvée et le prix unitaire facturé.

### [Cas 11a : Quantité supérieure à la limite (rejetée), prix dans la tolérance](case-11a-quantity-outside-tolerance-positive-rejected-unit-price-within-tolerance.md)

**Scénario:** La quantité dépasse la limite et a été rejetée ; le prix respecte la tolérance.

**Action illustrative:** Le mappage illustratif utilise la quantité approuvée et conserve le prix. Le traitement de l’excédent dépend des règles configurées.

### [Cas 10a : Quantité inférieure à la limite (rejetée), prix dans la tolérance](case-10a-quantity-outside-tolerance-negative-rejected-unit-price-within-tolerance.md)

**Scénario:** La quantité est inférieure à la limite et a été rejetée ; le prix respecte la tolérance.

**Action illustrative:** Le mappage illustratif utilise la quantité approuvée et conserve le prix unitaire.

### [Cas 8b, 9b : Quantité et prix hors tolérance (approuvés)](case-8b-9b-quantity-outside-tolerance-approved-unit-price-outside-tolerance-approved.md)

**Scénario:** Les écarts de quantité et de prix ont tous deux été approuvés.

**Action illustrative:** Le mappage illustratif utilise les valeurs facturées approuvées et les frais de ligne ou ajustements explicitement configurés.

### [Cas 10b : Quantité inférieure à la limite et prix hors tolérance (rejetés)](case-10b-quantity-outside-tolerance-negative-rejected-unit-price-outside-tolerance-rejected.md)

**Scénario:** Ni l’écart négatif de quantité ni l’écart de prix n’a été approuvé.

**Action illustrative:** Le mappage illustratif utilise les valeurs du PO ou les valeurs approuvées. Toute note de débit ou de crédit nécessite le mappage et la décision d’approbation correspondants.

### [Cas 11b : Quantité supérieure à la limite et prix hors tolérance (rejetés)](case-11b-quantity-outside-tolerance-positive-rejected-unit-price-outside-tolerance-rejected.md)

**Scénario:** L’écart positif de quantité et l’écart de prix ont été rejetés.

**Action illustrative:** Le mappage illustratif utilise les valeurs approuvées du PO ; le traitement des excédents dépend de la configuration active.

### [Cas 12, 13 : Frais de ligne par unité dans la tolérance](charge-per-unit-within-tolerance.md)

**Scénario:** Les frais de ligne par unité respectent la tolérance configurée par rapport au PO.

**Action illustrative:** Le mappage illustratif accepte les frais de ligne facturés sans ajustement.

### [Cas 14 : Frais de ligne par unité hors tolérance (approuvés)](charge-per-unit-outside-tolerance-approved-1.md)

**Scénario:** Les frais de ligne par unité dépassent la tolérance et ont été approuvés.

**Action illustrative:** Le mappage illustratif applique les frais de ligne approuvés.

### [Cas 15 : Frais de ligne par unité hors tolérance (rejetés)](charge-per-unit-outside-tolerance-rejected.md)

**Scénario:** Les frais de ligne par unité dépassent la tolérance et ont été rejetés.

**Action illustrative:** Le mappage illustratif retient les frais de ligne du PO ou les frais approuvés. Toute note pour l’écart dépend du mappage d’export.

### [Cas 12, 13 : Frais d’en-tête par unité dans la tolérance](case-12-13-header-charge-charge-per-unit-within-tolerance.md)

**Scénario:** Les frais d’en-tête par unité respectent la tolérance configurée par rapport au PO.

**Action illustrative:** Le mappage illustratif applique les frais d’en-tête facturés sans ajustement.

### [Cas 14 : Frais d’en-tête par unité hors tolérance (approuvés)](charge-per-unit-outside-tolerance-approved.md)

**Scénario:** Les frais d’en-tête par unité dépassent la tolérance et ont été approuvés.

**Action illustrative:** Le mappage illustratif applique les frais d’en-tête approuvés.

### [Cas 15 : Frais d’en-tête par unité hors tolérance (rejetés)](case-15-header-charge-charge-per-unit-outside-tolerance-rejected.md)

**Scénario:** Les frais d’en-tête par unité dépassent la tolérance et ont été rejetés.

**Action illustrative:** Le mappage illustratif retient les frais d’en-tête du PO ou les frais approuvés. Toute note distincte dépend du traitement configuré.

### [Lignes de taxe](tax-lines.md "mention")

**Scénario:** Les montants de taxe de la facture et du PO diffèrent.

**Action illustrative:** Le mappage illustratif utilise les taux et montants de taxe approuvés. La configuration doit être vérifiée au regard des exigences fiscales applicables ; cet exemple ne garantit pas la conformité juridique.
