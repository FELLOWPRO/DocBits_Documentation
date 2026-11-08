# Étape suivante et rejet d'un document

> Dans cette version, certains textes de l’interface peuvent encore être en anglais ou mal traduits. Le guide explique leur sens ; les captures montrent l’interface sans modification.

Après la lecture du [rapport de validation](validation-report.md), le rapport vous indique quoi faire. Vous pouvez aussi rejeter le document.

## Que faire ensuite

<figure><img src="../../../../../.gitbook/assets/einvoice-report-next-step-fr-20261104-v2.png" alt="Évaluation, étape suivante et actions du rapport."><figcaption><p>Évaluation, étape suivante et actions du rapport.</p></figcaption></figure>

L'**Évaluation** indique en une phrase si la facture est conforme. Le bloc **Étape suivante** vous dit quoi faire :

| Résultat | Étape suivante |
| --- | --- |
| Au moins une **erreur** | Demandez à l'expéditeur une facture corrigée, ou rejetez le document. Une facture corrigée est un nouveau document. |
| Uniquement des **avertissements** | Vous pouvez poursuivre avec le document. |

Les boutons à la fin du rapport :

* **Rejeter le document** : ouvre la boîte de dialogue de rejet (voir ci-dessous).
* **Rapport (HTML)** et **Rapport (XML)** : téléchargent le rapport, par exemple pour l'envoyer au fournisseur.
* **Fermer** : revient au document.

## Rejeter un document

<figure><img src="../../../../../.gitbook/assets/einvoice-reject-dialog-fr-20261104-v2.png" alt="Boîte de dialogue de rejet de la facture fictive. Le rejet a été annulé."><figcaption><p>Boîte de dialogue de rejet de la facture fictive. Le rejet a été annulé.</p></figcaption></figure>

1. Dans le rapport, cliquez sur **Rejeter le document**.
2. Vérifiez le **Motif**. DocBits le remplit à partir des erreurs du rapport. Vous pouvez modifier le texte.
3. Cliquez sur **Rejeter le document** pour confirmer. Le statut passe à **Rejeté**. Le motif est enregistré comme note et le rapport reste associé au document.

Cliquez sur **Annuler** pour laisser le document tel quel.

> Seuls les utilisateurs autorisés à modifier les documents voient **Rejeter le document**. Le bouton est masqué lorsque le document est déjà rejeté ou terminé.
