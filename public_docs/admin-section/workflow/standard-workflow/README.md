# Flux de travail standard

<figure><img src="../../../.gitbook/assets/docbits_workflow_purchase_order_4.svg" alt="DocBits Workflow Achat Commande 4"><figcaption></figcaption></figure>

#### Aperçu des composants du flux de travail :

* **Courriel de facture AP** : Le processus commence probablement par une facture reçue par e-mail.
* **DocBits** : Cet outil peut être utilisé pour des tâches initiales de gestion de documents telles que la capture et la numérisation des factures.
* **Révision financière** : Les factures font l'objet d'une révision financière où des décisions sont prises concernant leur validité et leur exactitude.

#### Étapes du flux de travail :

1. **Révision initiale** :
* Les factures sont reçues et traitées initialement à l'aide de DocBits.
* Elles sont ensuite examinées par l'équipe financière pour s'assurer qu'elles sont retirées du flux de travail si elles sont complètes, ou poussées pour un traitement ultérieur.
2. **Factures avec et sans bon de commande (PO vs Non-PO)** :
* Le flux de travail distingue entre les factures liées aux bons de commande et les factures sans bon de commande.
* Les factures sans bon de commande sont acheminées pour une approbation ou un rejet ultérieur en fonction de critères prédéfinis tels que l'ID du fournisseur, la quantité, le prix unitaire et le numéro d'article.
3. **Concordance et discordance** :
* Les factures sont vérifiées par rapport aux bons de réception pour s'assurer que les détails correspondent (comme l'ID du fournisseur et la quantité).
* En cas de discordances, la facture est soumise à un examen ultérieur et peut être rejetée.
4. **Révision financière et de l'acheteur** :
* Pour les factures liées aux bons de commande, un processus de concordance détaillé est effectué impliquant une révision par l'acheteur.
* Des ajustements aux bons de commande ou aux bons de réception peuvent être nécessaires.
5. **Décisions finales** :
* Les factures qui passent toutes les vérifications sont approuvées et intégrées dans les systèmes financiers pour la conservation des enregistrements.
* Les factures rejetées déclenchent des notifications, et une nouvelle facture peut être demandée par l'acheteur.
6. **Intégration avec Infor IDM & LN+M3** :
* Les factures approuvées sont probablement envoyées à l'IDM d'Infor pour la gestion des documents et à LN pour la notation dans le grand livre.
* Cette intégration garantit que tous les enregistrements financiers sont à jour et que le flux de travail s'intègre de manière transparente dans le système ERP plus large.

#### Points de décision :

* Tout au long du flux de travail, il existe divers points de décision où une facture peut être approuvée, rejetée ou renvoyée pour des informations supplémentaires. Des notifications sont envoyées après des retards, garantissant un traitement en temps opportun.

Ces flux de travail seront inclus dans le flux de travail standard.
