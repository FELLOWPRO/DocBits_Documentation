# Opération de Type de Document

<figure><img src="../../../.gitbook/assets/workflow_card_condition_doc_type_is_isnot_v1-fr-fr.png" alt="Opération de Type de Document, Version 1" width="634"><figcaption><p>Version 1</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/workflow_card_condition_doc_type_is_isnot_v2-fr-fr.png" alt="Opération de Type de Document, Version 2" width="634"><figcaption><p>Version 2</p></figcaption></figure>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-doc-type/v1/fr.mp4" %}

**Vidéo:** Carte: Type de document est / n'est pas · 0:31 · [Sous-titres (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-doc-type/v1/fr.vtt)

<details>

<summary>Transcription</summary>

**Type de document est / n'est pas** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-doc-type/v1/fr.mp4#t=0.25)

La carte Type de document vérifie le type d'un document. Choisissez Est ou N'est pas, puis le type, par exemple Facture. N'est pas correspond à tous les types sauf celui choisi.

**Exemple : seulement les factures** · [0:17](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-doc-type/v1/fr.mp4#t=17.183)

Par exemple, un Workflow uniquement pour les factures : Type de document est Facture comme carte Quand, puis une carte d'attribution. Pour les avoirs, les devis ou les commandes, ce Workflow ne démarre pas.

</details>

## **Objectif:**

Cette carte de flux de travail est spécifiquement conçue pour effectuer des opérations prédéfinies sur des documents catégorisés par type. Elle rationalise la gestion de diverses formes de documents au sein d'un système ERP, garantissant que chaque type est traité selon ses exigences uniques et les politiques organisationnelles.

## **Fonctionnalités:**

* **Validation du Type de Document**: Cette carte vérifie si un document correspond à un type particulier, permettant aux utilisateurs de confirmer sa catégorisation.
* **Opérateur**: Les utilisateurs peuvent définir des conditions pour déterminer le type de document. Les opérateurs disponibles incluent:
  * **Est**: Confirme que le document correspond au type de document spécifié.
  * **N'est pas**: Veille à ce que le document ne corresponde pas au type de document spécifié.
* **Types de Document**: Les types de documents pris en charge comprennent:
  * **Facture**
  * **Note de Débit**
  * **Note de Crédit**
  * **Bon de Commande**
  * **Confirmation de Commande**
  * **Avis d'Expédition Avancée**

## **Utilisation**:

Cette carte est utile pour les gestionnaires de documents et les administrateurs qui doivent s'assurer que les documents sont correctement classés pour un traitement rationalisé. La validation des types de documents améliore l'automatisation des flux de travail, permet des actions spécifiques aux documents et maintient les enregistrements organisés.

## **Scénario Exemple**:

* Un utilisateur télécharge un document étiqueté comme "Note de Débit." En utilisant l'opérateur "Est", la carte confirme que le type de document est effectivement "Note de Débit", permettant au système d'appliquer des règles de traitement pertinentes et de le catégoriser de manière appropriée.

En déployant la carte "Type de Document", les organisations peuvent automatiser la classification des documents, garantir la cohérence dans la gestion des documents et améliorer l'efficacité des flux de travail de gestion des documents.
