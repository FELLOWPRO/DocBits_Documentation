# Configuration des propriétés de champ

Utilisez **Settings → Document Types → Fields** pour contrôler le comportement des champs d'un type de document. Sélectionnez d'abord le type de document ; l'exemple ci-dessous montre **Invoice** dans l'interface anglaise.

<figure><img src="../../../../../.gitbook/assets/dbdc155-field-properties-overview-en.png" alt="Paramètres des champs de Invoice en anglais avec les seuils de reconnaissance, la recherche, les colonnes de propriétés des champs et Save Settings"><figcaption>Paramètres des champs de Invoice dans une organisation sandbox DocBits.</figcaption></figure>

## Trouver un champ et modifier ses propriétés

1. Dans **Search by Name**, saisissez le nom ou le libellé du champ. Cela filtre la liste ; cela ne modifie pas le champ.
2. Trouvez la ligne du champ. Par exemple, **Invoice number** a pour nom technique `invoice_id`.
3. Ajustez les contrôles de cette ligne, puis sélectionnez **Save Settings**. Le même bouton d'enregistrement est disponible au-dessus et en dessous du tableau.

<figure><img src="../../../../../.gitbook/assets/dbdc155-field-properties-filtered-en.png" alt="Champ Invoice number en anglais avec les contrôles Required, Read Only, Hidden, Force Validation, Use AI, OCR et Match Score"><figcaption>La ligne Invoice number après une recherche de `invoice_id`.</figcaption></figure>

| Contrôle | À quoi il sert |
| --- | --- |
| **Required** | Marque les informations qui doivent être présentes pour la validation. Vérifiez le résultat de validation du document après avoir modifié ce paramètre. |
| **Read Only** | Affiche un champ sans permettre aux utilisateurs de modifier sa valeur. |
| **Hidden** | Garde le champ hors de la vue normale du document. |
| **Force Validation** | Exige que le champ réussisse la validation. Configurez les règles détaillées séparément ; cette case à cocher n'est pas un éditeur de règles. |
| **Use AI** | Demande ou arrête l'extraction par IA pour ce champ. La ligne indique si l'extraction est demandée. |
| **OCR** | Saisissez le seuil de confiance OCR du champ. Il s'agit d'un nombre, et non d'un interrupteur ni d'un paramètre de langue. |
| **Match Score** | Saisissez le seuil de correspondance du champ. Il s'agit d'un nombre, et non d'un interrupteur. |

Les curseurs **OCR** et **Match Score** sous **Recognition Settings** appliquent des valeurs à l'ensemble de la liste des champs. Les cases à cocher situées directement sous les titres de colonnes appliquent **Required**, **Read Only**, **Hidden** ou **Force Validation** à l'ensemble de la liste. Vérifiez les lignes concernées avant de sélectionner **Save Settings**. **Restore Defaults** réinitialise la configuration des champs ; utilisez-le uniquement si vous avez l'intention de remplacer vos modifications.

## Autres contrôles de cette vue

- **Create new group** et **Create field** ajoutent un groupe ou un champ. Voir [Adding and Editing Fields](adding-and-editing-fields.md).
- **Master Data Settings** ouvre la [configuration des données de base](master-data-settings.md).
- Les cases à cocher tout à gauche sélectionnent des champs. Le menu adjacent propose **Reassign Field Group** pour les champs sélectionnés.
- Le bouton plus **Formula** ouvre l'éditeur de formules pour ce champ. L'icône **info** affiche les informations du champ. L'icône de suppression n'est pas disponible pour les champs standard.

Pour en savoir plus sur la validation et la correspondance, voir [Setting Validation and Match Score](setting-validation-and-match-score.md).
