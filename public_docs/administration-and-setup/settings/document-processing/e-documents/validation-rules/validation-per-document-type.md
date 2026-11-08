# Validation pour chaque type de document

Les administrateurs décident, pour chaque type de document, si DocBits valide les factures électroniques entrantes et si un contrôle échoué bloque le document. Chaque modification est confirmée et inscrite dans le [journal des modifications](validation-change-log.md).

> Seuls les **administrateurs de l'organisation** peuvent modifier ces paramètres. Les autres utilisateurs voient le tableau en lecture seule, ou ne le voient pas.

## Le tableau

Accédez à **Settings → E-Documents → E-Invoice Validation**. L'onglet **Rules and policy** commence par le tableau **Validation for each document type**.

<figure><img src="../../../../../.gitbook/assets/einvoice-validation-settings-fr-20261104.png" alt="Validation et blocage par type de document. Les noms configurés sont masqués. Exemple sur Dev."><figcaption><p>Validation et blocage par type de document. Les noms configurés sont masqués. Exemple sur Dev.</p></figcaption></figure>

| Interrupteur | Ce qu'il fait |
| --- | --- |
| **Enabled** | DocBits valide chaque facture électronique entrante de ce type de document et enregistre un [rapport de validation](validation-report.md). |
| **Blocking** | Un résultat de type erreur arrête le document. Il obtient le statut **Error**. Lorsque le blocage est désactivé, DocBits enregistre le rapport et le document continue. Vous ne pouvez activer **Blocking** que si **Enabled** est activé. |

Si un type de document a des exceptions pour des sous-types, le tableau affiche une remarque à ce sujet.

## Modifier un paramètre

1. Cliquez sur l'interrupteur que vous voulez modifier.
2. DocBits affiche **Confirm validation change** avec le type de document et la modification, par exemple *QUOTE : activer la validation*.

<figure><img src="../../../../../.gitbook/assets/einvoice-validation-confirm-fr.png" alt="Confirmation d’une modification des paramètres. La modification a été annulée pour cette capture."><figcaption><p>Confirmation d’une modification des paramètres. La modification a été annulée pour cette capture.</p></figcaption></figure>

3. Lisez la remarque : **Les rapports déjà enregistrés restent inchangés.** La modification s'applique uniquement aux nouveaux contrôles, y compris en cas de redémarrage du traitement d'un document.
4. Cliquez sur **Confirm change**, ou sur **Cancel** pour conserver l'ancien paramètre.

Si vous n'avez pas l'autorisation, DocBits affiche un message indiquant qu'un administrateur de l'organisation est requis, et rien ne change.

## Pages associées

* [Validation des factures électroniques](./)
* [Journal des modifications](validation-change-log.md)
* [Configuration de la validation et versions acceptées](validation-setup.md)
* [Rapport de validation](validation-report.md)
* [Activer ou désactiver la validation des factures électroniques](../#activer-ou-desactiver-la-validation-des-factures-electroniques)
