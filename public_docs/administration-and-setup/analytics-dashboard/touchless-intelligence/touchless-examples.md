# Exemples pratiques : prix et quantité

<!-- touchless-admin-video-v2-20261104:start -->
**Chapitre vidéo (version de contrôle):** [Suivre un document](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence-preview-admin/v2/fr.html#chapter=07).
<!-- touchless-admin-video-v2-20261104:end -->

## Exemple pratique : extraction correcte, données Infor différentes

Il s'agit d'un cas illustratif, distinct des captures d'écran. La facture indique **10 unités à 10,00 € l'unité**, pour un total de **100,00 €**. DocBits extrait correctement les trois valeurs. La commande Infor importée indique **10 unités à 9,00 € l'unité**, pour un total de **90,00 €**. Supposez que les contrôles de correspondance configurés bloquent cet écart de prix.

1. **Vérifiez l'extraction :** comparez la facture d'origine avec la quantité, le prix unitaire et le montant de ligne extraits. Ils correspondent : aucune erreur d'extraction n'est donc démontrée pour ces valeurs.
2. **Vérifiez la source :** comparez la commande importée avec la commande Infor actuelle, y compris l'unité de prix et l'heure d'import. Un import obsolète et une commande Infor incorrecte exigent des corrections différentes.
3. **Clarifiez la valeur métier :** dans cet exemple, les achats confirment que 10,00 € ont été convenus et corrigent la commande Infor. Si 9,00 € était le prix convenu, c'est la facture du fournisseur qui devrait être clarifiée.
4. **Vérifiez l'import corrigé :** contrôlez que les valeurs de commande correctes ont bien atteint DocBits avant de réessayer.
5. **Consignez l'action AP :** AP redémarre manuellement cette facture dans DocBits ; après une fin réussie, elle est **AP assisted**. Une extraction correcte et un processus non touchless peuvent être vrais en même temps.
6. **Vérifiez les factures suivantes :** contrôlez que la correspondance et l'export aboutissent désormais sans nouvelle correction ni redémarrage. La facture déjà touchée reste touchée ; les factures suivantes apportent la preuve d'une amélioration.

{% hint style="warning" %}
Ne remplacez pas une valeur de 10,00 € correctement extraite par 9,00 € uniquement pour correspondre à une commande incorrecte, et n'élargissez pas une tolérance juste pour masquer l'écart. Confirmez la valeur convenue et corrigez la donnée ou la configuration responsable. Un blocage de correspondance indique où le processus s'est arrêté, pas qui l'a causé.
{% endhint %}

Voir [Touchless Intelligence](./) pour l'exemple distinct de qualité d'extraction et le calcul AP touchless, et [Trace du document](touchless-document-trace.md) pour les preuves à comparer.

## Trois PO de démonstration créés pour nous : valeurs concordantes, prix et quantité

Ces PO ont été créés spécialement en **Dev**. Le fournisseur, l'article et les factures sont fictifs. Chaque facture contient **10 unités × 10 € = 100 € net**. Les cartes contiennent de véritables extraits d'interface anglaise et des détails numériques agrandis. Elles ne montrent ni connexion Infor client réelle, ni extraction prouvée, ni processus de facture automatique abouti.

| Cas | Facture | PO importé | Ce que la comparaison établit |
| --- | --- | --- | --- |
| PO01 / RE01 : valeurs concordantes | 10 × 10 € = 100 € | 10 × 10 € = 100 € | Les valeurs source concordent ; Pure Touchless exige encore une extraction correcte et une fin confirmée sans intervention ni approbation |
| PO02 / RE02 : écart de prix | 10 × 10 € = 100 € | 10 × 9 € = 90 € | Écart de 10 € sur la ligne ; le prix unitaire diffère d'environ 11,11 % par rapport au prix du PO. Les règles réellement actives décident si cela bloque |
| PO03 / RE03 : écart de quantité | 10 × 10 € = 100 € | 8 × 10 € = 80 € | 2 unités supplémentaires, soit 25 % de la quantité commandée. Vérifiez la quantité ouverte/reçue et la quantité de comparaison configurée |

<figure><img src="../../../.gitbook/assets/touchless-owned-po-match-fr.png" alt="Carte d'explication FELLOW avec le véritable PO Dev anglais PO01 indiquant une quantité de dix, un prix unitaire de dix et un montant de cent"><figcaption><p>Valeurs concordantes dans le PO01 fictif. La ligne native agrandie montre la quantité, le prix unitaire et le montant. La concordance seule ne prouve ni une extraction correcte ni Pure Touchless.</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/touchless-owned-po-price-fr.png" alt="Carte d'explication FELLOW avec le véritable PO Dev anglais PO02 indiquant dix unités à neuf et un montant de quatre-vingt-dix face à une facture de cent"><figcaption><p>Exemple de prix PO02 : la commande importée indique bien 10 × 9 = 90, contre 10 × 10 = 100 sur la facture fictive. Vérifiez le prix convenu, l'unité de prix et l'import. Une intervention humaine enregistrée suivie d'une fin réussie correspond à AP assisted.</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/touchless-owned-po-quantity-fr.png" alt="Carte d'explication FELLOW avec le véritable PO Dev anglais PO03 indiquant huit unités à dix, un montant de quatre-vingts, face à dix unités facturées"><figcaption><p>Exemple de quantité PO03 : le PO importé contient 8 unités, la facture 10. La quantité reçue est vide dans ce test et ne prouve aucune livraison. Ces cartes expliquent la comparaison ; elles ne prouvent pas une correspondance réussie.</p></figcaption></figure>

## Pages associées

* [Touchless Intelligence](./)
* [Indicateurs et calcul](../../touchless-metrics.md)
* [Utiliser le tableau de bord](touchless-dashboard.md)
* [Diagnostic fournisseur et clusters de problèmes](../../touchless-supplier-diagnosis.md)
* [Diagnostic du rapprochement avec le BC](../../touchless-po-matching-diagnosis.md)
* [Trace du document](touchless-document-trace.md)
* [Propositions de modification et rapports](touchless-change-proposals.md)
* [Expliquer et améliorer Touchless avec MCP](touchless-mcp.md)

<!-- Documentation review 2026-11-04: extraction quality vs process outcomes; KPI and terminal-outcome definitions checked against DocBits_API c51f350c728acb8ac964098d15f7b006bce273f4, module/automation_intelligence/kpi.py and bucket.py. Existing native screenshots retained and checked separately from illustrative examples. -->
<!-- Completion review 2026-11-04: owned synthetic PO examples, MCP schema/read evidence, human-action classification, KPI labels and screenshot proof limits. -->
