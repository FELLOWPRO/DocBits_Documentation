# Paramètres et surcharges

[AI Table](README.md) · [Structured Output pour les tableaux](structured-output.md)

## Paramètres pour les administrateurs

Ouvrez **Settings → Document Processing → Document Types → Classification and Extraction**, onglet **General**, section **Extraction**.

<figure><img src="../../../.gitbook/assets/structured-output-settings-fr-20261104.png" alt="Contrôles d'extraction actuels. Structured Output est désactivé dans cette configuration existante, donc aucun aperçu de schéma n'est affiché. Aucun paramètre d'extraction n'a été modifié."><figcaption><p>Contrôles d'extraction actuels. Structured Output est désactivé dans cette configuration existante, donc aucun aperçu de schéma n'est affiché. Aucun paramètre d'extraction n'a été modifié.</p></figcaption></figure>

* **Table Extraction** active le tableau classique.
* **AI Table extraction** active ou désactive le tableau IA pour l'organisation.
* **Use Structured Extraction (AI)** : l'interrupteur définit la valeur par défaut de sortie structurée de l'organisation. Les colonnes demandées dépendent de la sélection Use AI à trois états ; les surcharges de modèle et l'entraînement fournisseur comptent aussi. Lisez la configuration complète, l'aperçu et le guide d'exemple. [Structured Output pour les tableaux](structured-output.md).
* **Save extraction rules (Admin only)** : lorsqu'il est activé, seuls les administrateurs de l'organisation peuvent enregistrer et exporter les règles d'extraction.

<figure><img src="../../../.gitbook/assets/ai-table-settings-extraction-admin-only-fr.png" alt="Interrupteur Save extraction rules (Admin only)"><figcaption><p><strong>Save extraction rules (Admin only)</strong> détermine qui peut utiliser <strong>Save as training</strong>.</p></figcaption></figure>

### Use AI par colonne

Sélection IA à trois états : Default hérite de la valeur par défaut IA du type de document, Yes demande explicitement la colonne et No l'exclut du schéma de base. C'est distinct de Required, Read Only et Hidden. [Structured Output pour les tableaux](structured-output.md).


Structured Output a un paramètre d'organisation/de modèle distinct du niveau de modèle. Modifiez-le dans More options sur le document ; la confirmation enregistre la surcharge et redémarre ce document. Les indicateurs de la liste des paramètres sont en lecture seule. Supprimer une entrée de préférence peut retirer plusieurs surcharges à la fois. [Structured Output pour les tableaux](structured-output.md).
