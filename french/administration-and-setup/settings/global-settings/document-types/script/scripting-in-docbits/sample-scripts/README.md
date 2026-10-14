# Scripts d'Exemple

Scripts d'exemple prêts pour la production pour les cas d'utilisation courants d'automatisation dans DocBits. Chaque exemple inclut le script complet, une explication étape par étape et des liens vers les fonctions utilisées.

## Exemples par Cas d'Utilisation

### Validation de Données
- [Validation Fournisseur par Lookup](lookup-supplier-validation.md) — Valider le fournisseur contre les données maîtres
- [Validation de Somme de Table](table-sum-validation.md) — Vérifier que les totaux des lignes correspondent au montant net

### Automatisation
- [Correspondance Automatique de BC](auto-po-matching.md) — Déclencher la correspondance automatique de BC
- [Auto-Export par Conditions](status-auto-export.md) — Sauter la validation pour les factures à faible risque
- [Calcul de Date d'Échéance](due-date-calculation.md) — Calculer les conditions de paiement avec saut de week-ends

### Règles Métier
- [Détection de Code Fiscal](tax-code-detection.md) — Déterminer le code fiscal à partir du texte intégral et des montants
- [Tâche pour Montant Élevé](task-high-amount.md) — Créer une tâche d'approbation pour les factures importantes
- [Champs Obligatoires Dynamiques](dynamic-required-fields.md) — Ajuster les champs obligatoires selon la devise

### Fulltext & Vector Search
- [Détection de Factures en Double](duplicate-invoice-detection.md) — Trouver des doublons de factures par recherche fulltext
- [Détection de Documents Similaires](similar-document-detection.md) — Signaler des documents similaires par recherche vectorielle
- [Recherche de Texte de Conformité](compliance-text-search.md) — Rechercher des mots-clés de conformité (ex. Reverse Charge)
- [Validation Fournisseur ERP](erp-vendor-validation.md) — Valider le fournisseur contre les données maîtres ERP
- [Remplir les Champs depuis l'Historique](fill-missing-fields-from-history.md) — Remplir automatiquement les champs depuis des documents antérieurs

### Exemples Legacy
- [Calcul des Frais Totaux](calculating-total-charges-script-for-docbits-1.md) — Additionner les montants de fret et d'emballage
- [Supprimer les Lignes Vides](delete-lines-with-empty-quantity-and-amount.md) — Supprimer les lignes avec quantité/montant nul
- [Numéros de Certificat d'Exportation](formatting-export-certificate-reference-numbers-script-for-docbits.md) — Compléter les numéros de référence avec des zéros
- [Numéros de Facture Étendus](generating-extended-invoice-numbers-script-for-docbits-1.md) — Concaténer l'ID de facture et le numéro de BC
- [USD comme Devise par Défaut](usd-as-default-currency.md) — Définir USD comme devise par défaut
