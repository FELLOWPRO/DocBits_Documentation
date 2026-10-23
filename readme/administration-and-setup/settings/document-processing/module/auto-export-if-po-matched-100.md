# Export automatique en cas de rapprochement PO à 100%

### Présentation

L’option **Auto Export if PO matched 100%**, dans le module des commandes d’achat (PO), permet à un rapprochement complet avec la commande d’autoriser la poursuite du traitement de la facture ou du document courant vers l’export automatique. La commande sert de référence de comparaison ; cette option n’exporte pas la commande elle-même.

### Fonctionnement

Lorsque l’option est activée, le résultat du rapprochement du document courant avec le PO est contrôlé. Un rapprochement à 100% satisfait cette condition, sans garantir un export immédiat. La validation du document, le processus d’export configuré, les approbations requises et les tâches en attente peuvent encore bloquer ou retarder l’export. Un rapprochement incomplet bloque l’export automatique au titre de cette condition.

### Avantages

* **Efficacité :** Peut réduire les interventions manuelles pour les factures entièrement rapprochées qui satisfont les autres exigences.
* **Contrôle :** Ajoute le résultat du rapprochement PO aux conditions d’export.
* **Délai de traitement :** Peut accélérer le traitement des factures admissibles ; le délai dépend des autres conditions du processus.

### Utilisation

1. **Activer la fonction :**
   * Accédez à **Paramètres** → **Traitement des documents** → **Module** → **Commande d’achat**.
   * Activez le curseur **Auto Export if PO matched 100%**.

<figure><img src="../../../../.gitbook/assets/100%PO.png" alt="Page des paramètres avec la navigation Traitement des documents et le tableau d'export affichant les colonnes Type, Sous-Organisations, Titre et Actions"><figcaption></figcaption></figure>

2. **Surveiller le traitement :**
   * Vérifiez les états de rapprochement, de validation et d’export de la facture courante.
   * Si elle n’est pas exportée malgré un rapprochement à 100%, vérifiez la configuration d’export, les approbations et les tâches en attente.
3. **Vérifier la configuration :**
   * Assurez-vous que les critères de rapprochement et les paramètres d’export correspondent au processus prévu.
   * Examinez régulièrement les factures exportées et les exceptions.

### Quand utiliser cette fonction ?

* **Volumes élevés de factures :** Lorsque de nombreuses factures peuvent être rapprochées de façon fiable avec des commandes.
* **Achats récurrents :** Lorsque quantités, prix et autres critères sont stables.
* **Traitement urgent :** Lorsque les factures admissibles doivent avancer automatiquement une fois toutes les conditions remplies.

Lorsque le rapprochement avec les commandes est actif pour le type de document, l’option distincte `ALLOW_AUTO_EXPORT_FOR_NON_MATCHABLE_PO_LINES` autorise aussi le statut `NO_MATCHABLE_PO_LINES`. Elle n’autorise pas globalement les autres rapprochements incomplets.
