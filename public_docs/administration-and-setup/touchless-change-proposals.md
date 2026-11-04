# Touchless Intelligence : Propositions de modification et rapports


Une recommandation peut s'accompagner d'une **proposition de modification**, un changement de paramètre unique qui devrait aider. Les administrateurs la traitent en quatre étapes :

1. **Aperçu** : montre la modification (valeur actuelle → valeur proposée) et ce que DocBits en attend. Rien n'est enregistré. **Appliquer** n'est possible qu'après avoir consulté un aperçu.
2. **Appliquer** : enregistre exactement la modification prévisualisée. Elle est consignée dans le journal.
3. **Mesurer** : DocBits compare le taux touchless du même type de document **avant et après**, sur des périodes de même durée. Il faut au moins **20 documents** dans chaque période, sinon il indique *non mesurable*.
4. **Annuler** : rétablit le paramètre si la proposition permet ce retour. Vérifiez sa disponibilité et la valeur restaurée.

{% hint style="warning" %}
Un écart avant/après est une **observation**, pas une preuve de cause. D'autres éléments peuvent changer en même temps (un nouveau fournisseur, un pic saisonnier).
{% endhint %}

**Exemple illustratif.** Après activation du rapprochement et de l’export automatiques, le taux AP Touchless passe de 52 % (210 documents) à 61 % (198 documents), soit +9 points. Il comprend Pure et approbation seule ; il ne mesure pas l’extraction. Vérifiez aussi toute correction Infor dans l’import et les factures suivantes ; ne supposez pas qu’elle figure comme modification de paramètre DocBits. L’avant/après reste une observation, pas une preuve de causalité.


Les administrateurs voient aussi deux sections entre les chiffres clés et les graphiques :

* **Demandes d'amélioration** (Improvement requests) : des suggestions envoyées par les utilisateurs depuis l'assistant de validation, dans deux onglets **Ouvertes** et **Historique**.
* **Propositions de règles apprises** (Learned rule proposals) : des règles que DocBits a apprises des corrections de votre équipe, par exemple « pour le fournisseur X, remplacer la valeur dans le champ Y ». Avant d'en créer une, vérifiez les documents pour lesquels elle remplacerait une valeur que votre équipe avait acceptée. La section **Après l'activation** montre les corrections manuelles du champ cible avant et après la mise en service d'une règle.


<figure><img src="../.gitbook/assets/touchless-consulting-report-fr.png" alt="Le rapport de conseil avec les trois meilleures propositions, un tableau de classement et les problèmes par domaine"><figcaption><p>Le rapport de conseil : meilleures propositions, un classement de tous les bloqueurs avec les documents et l'impact estimé par mois, et les problèmes par domaine. Organisation d'exemple avec des données de démonstration ; les noms de fournisseurs sont fictifs.</p></figcaption></figure>

Les administrateurs trouvent le **rapport de conseil** (Consulting report) en bas de l'onglet. Cliquez sur **Créer le rapport** (Create report) pour le charger. Il combine, pour votre organisation :

* les **modifications ayant le plus grand effet**, classées, chacune avec le domaine, le problème, l'action recommandée, le nombre de documents et l'effet **estimé** par mois,
* **le domaine de chaque problème** (extraction, données de base, rapprochement avec le BC, comptabilisation automatique, paramètres, processus),
* des **contrôles de configuration des tableaux**, par exemple *sortie de tableau structurée non utilisée* ou *type de colonne de tableau incohérent* par type de document et par colonne.

Les valeurs d'effet sont des **estimations**. Si le rapport répond *forbidden*, votre rôle ne l'autorise pas.

Les outils et la classification des actions humaines sont expliqués dans [Touchless avec MCP](touchless-mcp.md).

## Pages connexes

* [Touchless Intelligence](touchless-intelligence.md)
* [Diagnostic fournisseur et clusters de problèmes](touchless-supplier-diagnosis.md)
* [Diagnostic du rapprochement avec le BC](touchless-po-matching-diagnosis.md)

<!-- Touchless documentation alignment 2026-11-04: extraction quality is distinct from process automation. KPI definition checked against DocBits_API c51f350c728acb8ac964098d15f7b006bce273f4; existing native screenshots and video sources preserved except unsafe historical list images. -->

<!-- Completion 2026-11-04: localized MCP examples, AP actions, original-value evidence and owned synthetic PO cards. -->
