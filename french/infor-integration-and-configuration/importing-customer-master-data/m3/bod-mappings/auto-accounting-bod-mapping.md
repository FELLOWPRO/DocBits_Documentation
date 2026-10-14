# Auto Accounting BOD Mapping

Le workflow Auto-Accounting de DocBits consomme deux BODs d'Infor M3 pour enrichir les factures de frais avec des dimensions comptables valides :

- **`Sync.CodeDefinition`** — fournit la liste des valeurs valides par dimension comptable (centre de coût, projet, groupe de comptes, …).
- **`Sync.ChartOfAccounts`** — fournit le plan comptable avec le profil de dimensions attaché à chaque compte.

{% file src="../../../../.gitbook/assets/Sync.CodeDefinition.pdf" %}
CodeDefinition — Référence d'origine du mappage BOD (PDF)
{% endfile %}

## Sync.CodeDefinition

→ Table de données de base DocBits : **m3flexdimension**

#### Cas 1 : Le même ID apparaît dans plusieurs Dimensions

```json
{
    "ID": "concat(substring(//DataArea/CodeDefinition/CodeValue/@listID,21),'_',//DataArea/CodeDefinition/DocumentID/ID)",
    "Dimension": "substring(//DataArea/CodeDefinition/CodeValue/@listID,21)",
    "ListID": "//DataArea/CodeDefinition/ListID",
    "CodeValue": "//DataArea/CodeDefinition/CodeValue",
    "Description": "//DataArea/CodeDefinition/Description"
}
```

#### Cas 2 : L'ID apparaît dans une seule Dimension

```json
{
    "ID": "//DataArea/CodeDefinition/DocumentID/ID",
    "Dimension": "substring(//DataArea/CodeDefinition/CodeValue/@listID,21)",
    "ListID": "//DataArea/CodeDefinition/ListID",
    "CodeValue": "//DataArea/CodeDefinition/CodeValue",
    "Description": "//DataArea/CodeDefinition/Description"
}
```

### Référence des champs

| Champ DocBits | Description |
|---|---|
| `ID` | Clé primaire dans `m3flexdimension`. Dans le **Cas 1**, le code dimension est préfixé devant l'`DocumentID/ID` de M3 pour conserver l'unicité des entrées quand le même code apparaît dans plusieurs dimensions ; le **Cas 2** utilise l'ID M3 brut. |
| `Dimension` | Nom de la dimension (ex. centre de coût, projet). Extrait depuis `CodeValue/@listID` via `substring(..., 21)` — voir la note ci-dessous. |
| `ListID` | Valeur `ListID` complète et non rognée. Conservée à côté de `Dimension` pour préserver le préfixe d'espace de noms d'origine à des fins d'audit et d'outils en aval. |
| `CodeValue` | Valeur réelle du code dimension (ex. numéro de centre de coût `1000`). |
| `Description` | Description lisible du code (ex. « Marketing »). |

### À propos de l'expression `substring(..., 21)`

Le second argument de la fonction XPath `substring()` est une position de début en base 1 — **ce n'est pas** une valeur `listID`. M3 émet `@listID` avec un préfixe de type espace de noms long de 20 caractères (par exemple `lng.m3.dimension.D1`), de sorte que `substring(value, 21)` renvoie le code dimension après ce préfixe (`D1` dans l'exemple). Si votre M3 émet un préfixe d'une longueur différente, l'offset doit être ajusté — merci de nous transmettre un BOD d'exemple avant de configurer Auto-Accounting sur un tenant non standard.

La source canonique de la valeur du code dimension est `/SyncCodeDefinition/DataArea/CodeDefinition/DocumentID/ID`. La forme `substring(@listID, 21)` est conservée ici comme repli pour les tenants où `DocumentID/ID` n'est pas renseignée. Aligner le mappage pour préférer `DocumentID/ID` et filtrer par `CodeDefinitionVariant='Accounting Dimension'` (voir section suivante) est une amélioration prévue. <!-- tracked in DOCB-12315 -->

### Quelles variantes de `CodeDefinition` DocBits traite-t-il ?

`Sync.CodeDefinition` est un BOD générique que M3 émet pour de nombreux objets différents (dimensions comptables, codes de statut, listes de classification …). Pour le workflow Auto-Accounting, seules les entrées portant `Property/NameValue[@name='CodeDefinitionVariant']='Accounting Dimension'` sont pertinentes. Jusqu'à ce que le processor applique ce filtre nativement, nous recommandons de filtrer sur `CodeDefinitionVariant` dans votre DataFlow ION avant que le BOD n'atteigne DocBits — sinon les BODs `CodeDefinition` non-dimensions sont ingérés dans `m3flexdimension` et encombrent le sélecteur dans l'UI des factures de frais. <!-- tracked in DOCB-12315 -->

### Comment les dimensions alimentent les factures de frais

Quand une facture est classée comme facture de frais, DocBits propose des lignes comptables basées sur le plan comptable (voir ci-dessous). Pour chaque dimension requise par le compte nominal proposé, l'UI offre les valeurs stockées dans `m3flexdimension` — pré-remplies à partir des derniers BODs `Sync.CodeDefinition`. L'utilisateur AP choisit la bonne valeur ou accepte la suggestion automatique, et le résultat est exporté vers M3 via le BOD `Sync.SupplierInvoice` correspondant.

## Sync.ChartOfAccounts

→ Table de données de base DocBits : **ChartOfAccounts**

```json
{
    "ID": "//DataArea/ChartOfAccounts/IDs/ID",
    "NominalAccount": "//DataArea/ChartOfAccounts/BaseChartOfAccounts/GLNominalAccount",
    "AccountType": "//DataArea/ChartOfAccounts/BaseChartOfAccounts/AccountType",
    "Description": "//DataArea/ChartOfAccounts/BaseChartOfAccounts/Description",
    "DimensionProfile": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/ID",
    "Dimension1": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[0]/ListID",
    "Usage1": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[0]/Usage",
    "Dimension2": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[1]/ListID",
    "Usage2": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[1]/Usage",
    "Dimension3": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[2]/ListID",
    "Usage3": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[2]/Usage",
    "Dimension4": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[3]/ListID",
    "Usage4": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[3]/Usage",
    "Dimension5": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[4]/ListID",
    "Usage5": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[4]/Usage",
    "Dimension6": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[5]/ListID",
    "Usage6": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[5]/Usage",
    "Dimension7": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[6]/ListID",
    "Usage7": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[6]/Usage"
}
```
