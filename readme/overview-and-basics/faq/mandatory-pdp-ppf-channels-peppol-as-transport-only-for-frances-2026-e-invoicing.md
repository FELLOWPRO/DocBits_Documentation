# Facturation électronique en France : plateformes agréées et PEPPOL

## Règles et calendrier actuels

Pour les factures B2B domestiques françaises entrant dans le champ de la réforme entre entreprises assujetties à la TVA, l’échange doit passer par une **plateforme agréée (PA, anciennement PDP)**. Le **portail public de facturation (PPF)** assure les fonctions d’annuaire public et de collecte des données fiscales ; il ne constitue pas une plateforme alternative d’échange de ces factures.

* **1er septembre 2026 :** Toutes les entreprises concernées doivent pouvoir recevoir des factures électroniques. Les grandes entreprises (GE) et les entreprises de taille intermédiaire (ETI) doivent également émettre des factures électroniques et satisfaire à leurs obligations d’e-reporting à cette date.
* **1er septembre 2027 :** Les obligations d’émission et d’e-reporting s’appliquent aux petites et moyennes entreprises (PME) et aux microentreprises.

L’obligation applicable dépend du champ de l’opération et de la catégorie d’entreprise. Consultez les sources officielles sur les [plateformes agréées](https://www.impots.gouv.fr/facturation-electronique-et-plateformes-agreees), le [calendrier de mise en œuvre](https://www.impots.gouv.fr/professionnel/questions/partir-de-quand-suis-je-concerne-par-la-reforme-de-la-facturation) et la [réponse ministérielle](https://www.senat.fr/questions/base/2026/qSEQ260107185.html).

## PEPPOL et interopérabilité

PEPPOL peut assurer le transport et l’interopérabilité entre systèmes et plateformes connectés. Son utilisation ne remplace pas l’obligation de recourir à une PA pour les échanges de factures soumis à la réforme française. Une connexion PEPPOL ne suffit pas, à elle seule, à démontrer le respect des obligations d’échange et de transmission des données.

## Contexte technique historique

Les six schémas et les descriptions d’API ci-dessous sont conservés comme contexte technique provenant d’anciens documents PPF/PDP. Ils utilisent l’ancienne terminologie et l’ancienne architecture ; ils ne décrivent pas une possibilité actuelle d’échanger les factures B2B obligatoires via le PPF. Vérifiez les spécifications actuelles des PA et des services publics avant de réaliser une intégration.

<figure><img src="../../.gitbook/assets/Picture 1.png" alt="Diagramme du cycle de vie d'une facture du fournisseur jusqu'aux états Submitted, Received by the platform et Made available, avec les résultats Rejected, Refused, Disputed, Partially approved, In hand et Completed"><figcaption></figcaption></figure>

### Ancien modèle de services API

L’ancien modèle décrivait l’accès aux fonctions disponibles depuis les outils informatiques des structures partenaires, selon deux modes :

* **Systèmes d’information (SI) :** Les API étaient intégrées aux systèmes des émetteurs, des destinataires ou de leurs opérateurs de dématérialisation (OD). Certaines API étaient destinées aux systèmes PDP, comme alternative à l’intégration EDI.
* **Logiciels tiers :** Les éditeurs pouvaient ajouter une couche de communication au SI du client. Les anciennes références à une connexion au PPF appartiennent à ce modèle historique et ne constituent pas une voie actuelle d’échange de factures.

<figure><img src="../../.gitbook/assets/Picture 6.png" alt="Diagramme d'un Issuer OD-PDP et d'un Receiver OD-PDP liés par des portails de services et des logiciels tiers, avec une étape de contrôle et de récupération des données entre eux"><figcaption></figcaption></figure>

### Ancien schéma d’interconnexion

Ce schéma illustre l’ancien contexte d’interconnexion des plateformes. Une implémentation actuelle doit respecter les exigences des PA ; aucune obligation générale de faire passer tous les échanges par un réseau de transport unique n’est affirmée ici.

<figure><img src="../../.gitbook/assets/Picture 2.png" alt="Diagramme des trois couches de contrôle numérotées : contrôles techniques, contrôles applicatifs et contrôles fonctionnels et métier, chacune alimentant une étape de processus suivante"><figcaption></figcaption></figure>

### Ancien raccordement d’un concentrateur

L’ancien modèle décrivait une solution web ou applicative dans laquelle **le concentrateur effectuait les appels API pour le compte de ses clients**. Il prévoyait un compte technique par partenaire et, pour le concentrateur, une application sous PISTE et un raccordement au PPF. Il s’agit de détails d’architecture historiques, pas d’une procédure actuelle d’intégration vérifiée.

<figure><img src="../../.gitbook/assets/Picture 5.png" alt="Diagramme du modèle en hub montrant un partenaire avec un compte technique, le hub, une application sous PISTE et une connexion"><figcaption></figcaption></figure>

### Références historiques

L’ancienne documentation citait [le calendrier et le résumé juridique antérieurs](https://www.ey.com/en_gl/technical/tax-alerts/france-revises-schedule-for-adopting-e-invoicing-reform), [les spécifications de 2022](https://www.avalara.com/blog/en/europe/2022/09/france-publishes-updated-specifications-for-e-invoicing-and-e-reporting.html), [une présentation de la réforme en 2025](https://www.avalara.com/blog/en/europe/2025/01/e-invoicing-reform-france.html), [le contexte d’interconnexion](https://nymus.be/fr/facturation-electronique-en-france/), [le contexte PEPPOL](https://edicomgroup.com/blog/status-of-b2b-electronic-invoicing-in-france) et [le contexte des échanges](https://nymus.be/fr/facturation-electronique-en-france/). Ces liens et les derniers schémas sont conservés à titre historique. Pour les obligations actuelles et la distinction entre l’échange via les PA et les fonctions publiques du PPF, utilisez les sources officielles ci-dessus. L’ancienne référence à l’article 91 de la loi de finances pour 2024 n’établit pas une option actuelle d’échange via le PPF.

<div><figure><img src="../../.gitbook/assets/Picture 3.png" alt="Diagramme de la réception d'un flux EDI et du flux 2 via API passant des contrôles fonctionnels de format sémantique, d'annuaire et de cohérence des données avant l'incorporation des données de facturation et un résultat de facture transmise"><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/Picture 4.png" alt="Diagramme d'un flux EDI et d'un flux API passant des contrôles fonctionnels et des règles métier spécifiques avant le rejet ou le refus de la facture ou une facture reçue et mise à disposition"><figcaption></figcaption></figure></div>
