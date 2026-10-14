# Flux de travail standard

<figure><img src="../../../../.gitbook/assets/docbits_workflow_purchase_order_4.svg" alt="DocBits Workflow Achat Commande 4"><figcaption></figcaption></figure>

#### Aperçu des composants du flux de travail :

* **AP Invoice Email** : Le processus commence vraisemblablement par une facture reçue par e-mail.
* **DocBits** : Cet outil peut être utilisé pour les tâches initiales de gestion documentaire telles que la capture et la numérisation des factures.
* **Finance Review** : Les factures font l'objet d'un examen financier au cours duquel des décisions sont prises concernant leur validité et leur exactitude.

#### Étapes du flux de travail :

1. **Examen initial** :
   * Les factures sont reçues et initialement traitées à l'aide de DocBits.
   * Elles sont ensuite examinées par l'équipe financière afin d'être retirées du flux de travail si elles sont complètes, ou transmises pour un traitement ultérieur.
2. **Factures avec PO vs sans PO** :
   * Le flux de travail distingue les factures liées à un PO et les factures sans PO.
   * Les factures sans PO sont acheminées pour approbation ou rejet supplémentaire selon des critères prédéfinis tels que l'ID du fournisseur, la quantité, le prix unitaire et le numéro d'article.
3. **Correspondance et non-correspondance** :
   * Les factures sont vérifiées par rapport aux réceptions de marchandises afin de s'assurer que les détails correspondent (comme l'ID du fournisseur et la quantité).
   * En cas de non-correspondance, la facture fait l'objet d'un examen complémentaire et éventuellement d'un rejet.
4. **Examen par la finance et l'acheteur** :
   * Pour les factures liées à un PO, un processus de correspondance détaillé est mené, impliquant un examen par l'acheteur.
   * Des ajustements aux commandes d'achat ou aux réceptions de marchandises peuvent être nécessaires.
5. **Décisions finales** :
   * Les factures qui passent toutes les vérifications sont approuvées et intégrées aux systèmes financiers à des fins de conservation des enregistrements.
   * Les factures rejetées déclenchent des notifications, et une nouvelle facture peut être demandée par l'acheteur.
6. **Intégration avec Infor IDM et LN+M3** :
   * Les factures approuvées sont vraisemblablement envoyées à l'IDM d'Infor pour la gestion documentaire et à LN pour l'enregistrement comptable.
   * Cette intégration garantit que tous les enregistrements financiers sont à jour et que le flux de travail s'intègre de manière transparente dans le système ERP plus large.

#### Points de décision :

* Tout au long du flux de travail, il existe divers points de décision où une facture peut être approuvée, rejetée ou renvoyée pour information complémentaire. Des notifications sont envoyées après des délais, garantissant un traitement en temps voulu.

Ces flux de travail seront inclus dans le flux de travail standard
