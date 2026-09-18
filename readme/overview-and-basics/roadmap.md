# Feuille de route DocBits

_État de la planification au 18 septembre 2026. Chaque version indique la date
sandbox prévue (à partir de laquelle les clients peuvent la tester) et la date
de production prévue. Les thèmes décrivent ce qui est prévu pour la version,
pas ce qui a déjà été livré ; le périmètre et les dates peuvent évoluer. Les
correctifs urgents entre deux versions sont documentés dans les
[Notes de version](release-notes/README.md)._

| Version | Sandbox | Production |
|---|---|---|
| R1.1 | 5 octobre 2026 | 14 octobre 2026 |
| R1.2 | 23 novembre 2026 | 2 décembre 2026 |
| R1.3 | 8 février 2027 | 17 février 2027 |
| R1.4 | 7 avril 2027 | 15 avril 2027 |
| R1.5 | 18 mai 2027 | 27 mai 2027 |
| R1.6 | 6 juillet 2027 | 15 juillet 2027 |
| R1.7 | 21 septembre 2027 | 30 septembre 2027 |
| R2.0 | à annoncer | à annoncer |

---

## R1.1 — Sandbox 5 octobre 2026 · Production 14 octobre 2026

**Règles de transformation et mises en page**

- Un moteur de règles pour les valeurs extraites des champs et des colonnes :
  définir, remplacer ou dériver des valeurs avec des groupes de conditions
  imbriqués, avec un écran de paramètres pour gérer les règles. Les règles de
  sélection de mise en page reçoivent les mêmes conditions imbriquées.
- La sélection de la mise en page fonctionne indépendamment de la provenance du
  document.
- Des règles de priorité claires pour les libellés des champs d'en-tête et des
  colonnes de tableau.
- Une colonne de tableau peut être attribuée à nouveau après sa suppression, et
  le tableau des prix d'articles fournisseur affiche toutes ses colonnes.

**Écrans d'approbation et de validation**

- Les trois tableaux de lignes de l'écran d'approbation (lignes de facture,
  lignes de comparaison, correspondance des bons de commande) partagent un
  même style, et la vue de comparaison affiche le numéro d'article qui
  appartient à la ligne.
- Le dernier panneau latéral ouvert (flux d'activité ou historique
  d'approbation) est mémorisé par utilisateur.
- Fusionner des documents depuis l'écran d'approbation avec l'outil de
  téléversement de documents.
- Les règles de validation personnalisées traitent les frais de port de manière
  générique, et les règles qui signalaient un faux négatif sont corrigées.
- Une barre de chargement remplace la simple icône de chargement ; des URL de
  page plus lisibles.

**Détection des doublons**

- Les champs personnalisés apparaissent dans le résultat de la détection des
  doublons, et les paramètres de doublons peuvent être recherchés.

**Workflows et tâches**

- Un bouton « Nouveau workflow », des journaux pour les workflows avancés, un
  écran de journal du watchdog plus clair, et les étapes de workflow qui
  modifient un champ ou une case à cocher s'appliquent de manière fiable.
- L'ajout d'une ligne dans un arbre de décision conserve les noms d'utilisateur
  au lieu d'afficher des identifiants.
- Chaque changement de statut d'un document est journalisé.
- La création d'un nouveau modèle d'e-mail fonctionne à nouveau.

**Import**

- L'import d'e-mails ne déplace un message hors de la boîte de réception
  qu'une fois le téléversement confirmé, traite un transfert relivré comme une
  seule livraison, enregistre qui a effectué le dernier enregistrement et
  accepte les e-mails signés S/MIME.
- L'import FTP reçoit une véritable option de suppression après import, à côté
  du déplacement et de l'archivage.
- Le téléversement depuis l'application scanner fonctionne à nouveau.
- Les fichiers BOD de bons de commande téléversés dans la région US restent
  dans la région US.

**Traitement des documents et extraction**

- Lorsque le service de codes-barres se bloque, le document affiche l'erreur
  au lieu de rester indéfiniment en « Processing ».
- Un nouveau niveau de modèle IA moins coûteux (« Eco ») pour l'extraction.
- Avec l'extraction IA structurée, les numéros d'article fournisseur entraînés
  restent entraînés, et le numéro d'article et le numéro d'article fournisseur
  ne sont plus intervertis.
- Les modèles d'e-documents UBL sont ajustés ; corrections d'extraction pour
  les montants, les taux de taxe, les prix unitaires et les numéros de bon de
  commande sur certaines mises en page de fournisseurs.
- Des formats de date supplémentaires sont reconnus.

**Correspondance des bons de commande**

- La correspondance exige une colonne de quantité, utilise le prix par quantité
  d'unité de base, et le repli sur la dernière ligne peut être activé ou
  désactivé par client.
- Les lignes de bon de livraison peuvent être sélectionnées individuellement.
- L'écran des e-documents ne se fige plus sur les factures de plus de 250
  lignes.

**Touchless Intelligence**

- Plus de détails dans le rapport Touchless, et la case à cocher Touchless
  reflète le paramètre enregistré.

**Tableau de bord**

- Le tableau de bord peut contenir jusqu'à 10 000 documents par recherche.
- La date d'échéance de l'escompte et la date d'échéance de la facture sont
  disponibles comme champs de mise en page et renseignées à l'import.
- Les utilisateurs partagés d'un tableau de bord sont conservés lors de son
  enregistrement, et « Mis à jour par » affiche la bonne personne.
- Les documents archivés peuvent de nouveau quitter le statut « Archivé ».

**Export et EDI**

- Une étape d'export Infor M3 supplémentaire pour les informations de facture
  complémentaires.
- Une liste de colisage comportant plusieurs numéros de conteneur est exportée
  sous la forme d'un enregistrement par conteneur.
- La réimportation d'une livraison reçue n'échoue plus sur une clé en double,
  et les BOD de livraison reçue sont appliqués dans le bon ordre.
- Les mappages EDI pour la facture, le bon de commande et la confirmation de
  commande sont mis à jour.

**Sécurité**

- Le contrôle d'organisation des clés API est appliqué sur chaque
  environnement.

---

## R1.2 — Sandbox 23 novembre 2026 · Production 2 décembre 2026

**Approbation et correspondance des bons de commande**

- Un état « En attente de saisie » met un document en pause jusqu'à ce que
  quelqu'un réponde, sans casser le workflow ni l'historique d'audit, et les
  approbateurs peuvent poser des questions sans interrompre le flux
  d'approbation.
- Les factures d'acompte peuvent être rapprochées avant la réception des
  marchandises tandis que « Correspondance sur la quantité reçue » reste actif.
- Un indicateur de disponibilité de réception compare les quantités facturées
  et reçues.
- Confirmations de commande : éléments de coût affichés pendant que
  l'approbation est en attente, positions de surcharge codées par couleur dans
  la correspondance des bons de commande, et la colonne de numéro d'article
  dans les lignes de facture.
- Les colonnes non mappées n'alimentent plus le calcul du montant du tableau.
- Les lignes RMA fournisseur sont prises en charge.

**Import et classification**

- L'adresse de l'expéditeur est disponible depuis l'import d'e-mails.
- Le type de fournisseur est dérivé des lignes de la facture.

**Paramètres et automatisation**

- Le script « Définir la sous-organisation » devient une règle de
  transformation.
- Les colonnes standard peuvent être retirées d'un type de document.

**Export**

- L'historique des exports liste à nouveau les documents exportés.
- Les factures de fret s'exportent vers Infor LN.

---

## R1.3 — Sandbox 8 février 2027 · Production 17 février 2027

**Rule Manager Auto Accounting**

- Les règles attribuent automatiquement les comptes et les dimensions, par
  sous-organisation et type de document, avec un écran d'audit qui montre
  quelle règle s'est déclenchée.
- Une règle peut renseigner une valeur à partir d'une colonne de ligne de
  tableau.
- Les champs et les dimensions peuvent être effacés individuellement, les
  lignes peuvent être supprimées (y compris les lignes sans montant), et les
  règles continuent de fonctionner sur les champs passés de texte à liste
  déroulante.

**Correspondance des bons de commande**

- L'icône de correspondance navigue, fait défiler et met en surbrillance d'un
  onglet à l'autre, y compris pour les correspondances un-à-plusieurs.
- Conversion d'unités avec alias (par exemple KG et TO), un écart d'arrondi
  configurable avec un compte d'arrondi, et des calculs à quatre décimales
  affichés avec trois.

**Export**

- Noms de fichiers d'export configurables.
- Un document incomplet dans Infor LN est supprimé après un export échoué.
- Le connecteur de base de données inclut toutes les tables pertinentes.

---

## R1.4 — Sandbox 7 avril 2027 · Production 15 avril 2027

**Import**

- Un mécanisme de relance pour l'import FTP, e-mail et e-mail entrant, avec
  retraitement automatique et manuel.

**DocNet Agents**

- Saisie de commandes : une commande client devient une commande de vente dans
  Infor M3 ou Infor LN (première version, documents texte).

**Approbation**

- Un flux d'approbation amélioré, la délégation à un autre utilisateur pendant
  l'approbation, et un bouton « Exporter et suivant ».

**Correspondance des bons de commande**

- Seules les lignes de bon de commande viables sont proposées sur l'écran de
  correspondance.
- Les factures rapprochées en excès, dont la quantité facturée dépasse la
  quantité reçue, sont reconnues sur l'écran de correspondance, et les unités
  de mesure sont converties lors du rapprochement de la facture.

**Autres**

- Tour de retours sur le Rule Manager.
- Le formulaire de ticket de support accepte les pièces jointes et rattache
  automatiquement l'organisation.
- Intégration fiscale Vertex étendue.

---

## R1.5 — Sandbox 18 mai 2027 · Production 27 mai 2027

**Auto Accounting**

- Action de recherche du Rule Manager : faire correspondre les données de base
  et attribuer plusieurs champs à la fois.
- Les prédictions prennent en charge plusieurs codes de taxe et dimensions, les
  pièces comptables et les références de comptabilisation.
- Écrans Auto Accounting en plusieurs langues.

**Approbation et correspondance des bons de commande**

- Réassigner un document à un autre utilisateur.
- L'ordre des colonnes de l'écran de correspondance des bons de commande est
  enregistré par utilisateur.
- Les codes de frais (péage, transport, énergie) sont reconnus et leur coût
  réparti.

**Garde-fous à l'export**

- L'export est bloqué avec un avertissement lorsque la quantité rapprochée
  dépasse la quantité reçue ou s'en écarte trop, ou lorsque la date de
  comptabilisation est antérieure à la date d'entrée en entrepôt.

**Ergonomie**

- L'ordre d'exécution des scripts de document est visible dans l'interface.
- Entrée et Tab permettent de passer d'un champ à l'autre au clavier.

---

## R1.6 — Sandbox 6 juillet 2027 · Production 15 juillet 2027

**Paramètres**

- Les paramètres peuvent être recherchés dans l'ensemble des options et des
  sous-pages.
- La configuration du serveur de messagerie permet de remplacer un secret
  OAuth ou un secret client expiré sans reconfigurer la boîte aux lettres.
- La table de correspondance des numéros d'article fournisseur (table de
  conversion des numéros d'article) peut être alimentée par un import CSV.

**Auto Accounting**

- Les dimensions sont stockées dans une nouvelle structure afin que les grands
  ensembles de dimensions se chargent plus rapidement.

---

## R1.7 — Sandbox 21 septembre 2027 · Production 30 septembre 2027

**Auto Accounting sur l'écran d'approbation**

- Les approbateurs peuvent utiliser Auto Accounting directement sur l'écran
  d'approbation.
- L'approbation peut être conditionnée à des champs comptables tels que le
  compte général ou le pays, avec une correction en comptabilité fournisseurs
  lorsqu'un document est renvoyé.
- Une liste déroulante de codes de taxe dans Auto Accounting sans avoir à
  configurer plusieurs lignes de taxe.

---

## R2.0 — Sandbox à annoncer · Production à annoncer

**Auto Accounting**

- Les champs adossés à une liste acceptent aussi la saisie libre.
- Les champs obligatoires sont validés.
- Les prédictions du modèle renseignent automatiquement les champs comptables
  (mode hybride avec le modèle de prédiction entraîné), avec une piste d'audit
  de ce que le modèle a renseigné.

<!-- Generated from Jira "Release No." (customfield_10392) on 2026-09-18 by the
     docbits-roadmap skill. Themes only; ticket keys, customer names and
     internal work are deliberately left out. Rerun the skill to refresh. -->
