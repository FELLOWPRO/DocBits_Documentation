# Feuille de route DocBits

_État de la planification au 7 octobre 2026. Chaque version indique la date
sandbox prévue (à partir de laquelle les clients peuvent la tester) et la date
de production prévue. Les thèmes décrivent ce qui est prévu pour la version,
pas ce qui a déjà été livré ; le périmètre et les dates peuvent évoluer. Les
correctifs urgents entre deux versions sont documentés dans les
[Notes de version](release-notes/README.md)._

| Version | Sandbox | Production |
|---|---|---|
| R1.1 | 16 octobre 2026 | 4 novembre 2026 |
| R1.2 | 16 février 2027 | 3 mars 2027 |
| R1.3 | 1er juin 2027 | 16 juin 2027 |
| R1.4 | 5 octobre 2027 | 20 octobre 2027 |

---

## R1.1 — Sandbox 16 octobre 2026 · Production 4 novembre 2026

**Règles de transformation et mises en page**

- Un moteur de règles pour les valeurs extraites des champs et des colonnes :
  définir, remplacer ou dériver des valeurs avec des groupes de conditions
  imbriqués, avec un écran de paramètres pour gérer les règles. La condition
  « fait partie de » accepte plusieurs valeurs, la liste des règles peut être
  recherchée par identifiant de règle, et les règles s'exécutent aussi après la
  recherche dans les données de base.
- Les règles de sélection de mise en page reçoivent les mêmes conditions
  imbriquées et un journal d'exécution facultatif. La sélection de la mise en
  page fonctionne indépendamment de la provenance du document.
- Manage Layouts, Custom Validation Rules et Transformation Rules n'ont plus
  besoin de l'interrupteur bêta.
- Des règles de priorité claires pour les libellés des champs d'en-tête et des
  colonnes de tableau. Les utilisateurs peuvent créer leurs propres clés de
  traduction pour les paramètres de champ et les colonnes de tableau.
- Une colonne de tableau peut être attribuée à nouveau après sa suppression, et
  le tableau des prix d'articles fournisseur affiche toutes ses colonnes.

**Écrans d'approbation et de validation**

- Les trois tableaux de lignes de l'écran d'approbation (lignes de facture,
  lignes de comparaison, correspondance des bons de commande) partagent un
  même style.
- Le dernier panneau latéral ouvert (flux d'activité ou historique
  d'approbation) est mémorisé par utilisateur.
- Fusionner des documents depuis l'écran d'approbation avec l'outil de
  téléversement de documents.
- Les règles de validation personnalisées traitent les frais de port de manière
  générique, affichent un message sur le champ au lieu d'une erreur générale
  lorsqu'un champ obligatoire est vide, et les règles qui signalaient un faux
  négatif sont corrigées. Les règles par défaut du système peuvent être
  dupliquées.
- Un écart entre la quantité et le montant net d'un tableau extrait par IA est
  signalé, une facture avec un bon de commande rapproché n'est plus classée
  comme facture de frais, et une date reformatée par une règle est acceptée.
- Un écran d'approbation qui restait bloqué sur la superposition de chargement
  après une approbation ou un rejet est corrigé. Une barre de chargement
  remplace la simple icône de chargement, et les URL de page sont plus lisibles.
- Ouvrir un lien de document après l'expiration de la session mène à la page de
  connexion au lieu d'une erreur 404.

**Détection des doublons**

- Les champs personnalisés apparaissent dans le résultat de la détection des
  doublons, et les paramètres de doublons peuvent être recherchés.
- « Block Duplicate Document Export » bloque l'export d'un doublon détecté.

**Workflows et tâches**

- Un bouton « Nouveau workflow », des journaux pour les workflows avancés, un
  écran de journal du watchdog plus clair, et les étapes de workflow qui
  modifient un champ ou une case à cocher s'appliquent de manière fiable.
- L'ajout d'une ligne dans un arbre de décision conserve les noms d'utilisateur
  au lieu d'afficher des identifiants.
- Chaque changement de statut d'un document est journalisé.
- La création d'un nouveau modèle d'e-mail fonctionne à nouveau.
- La liste des tâches affiche ses tâches dès le premier chargement.

**Import**

- L'import d'e-mails ne déplace un message hors de la boîte de réception
  qu'une fois le téléversement confirmé, traite un transfert relivré comme une
  seule livraison, enregistre qui a effectué le dernier enregistrement et
  liste une pièce jointe une seule fois avec le motif lorsqu'elle échoue.
- L'import FTP et SFTP reçoit une véritable option de suppression après
  import, à côté du déplacement et de l'archivage. Les mots de passe ne sont
  plus corrompus lors de la modification d'une configuration, le test de
  connexion fonctionne pour les nouvelles connexions SFTP, et une connexion
  SFTP échouée ou un mauvais identifiant affiche un message précis au lieu
  d'une erreur générale.
- Les administrateurs sont informés dans le Settings Assistant lorsqu'un
  import FTP ou e-mail configuré cesse de fonctionner.
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
- Une facture de frais avec deux taux de TVA conserve ses deux lignes
  comptables.

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

**Tableau de bord, comptes et abonnement**

- Le tableau de bord peut contenir jusqu'à 10 000 documents par recherche, et
  un filtre de date personnalisé est appliqué correctement.
- La date d'échéance de l'escompte et la date d'échéance de la facture sont
  disponibles comme champs de mise en page et renseignées à l'import.
- Les utilisateurs partagés d'un tableau de bord sont conservés lors de son
  enregistrement, et « Mis à jour par » affiche la bonne personne.
- Les documents archivés peuvent de nouveau quitter le statut « Archivé ».
- Les utilisateurs peuvent de nouveau se connecter après une réinitialisation
  de mot de passe.
- La page du plan d'abonnement affiche l'utilisation du plan et de ses
  fonctionnalités.

**Export et EDI**

- Une étape d'export Infor M3 supplémentaire pour les informations de facture
  complémentaires.
- Une liste de colisage comportant plusieurs numéros de conteneur est exportée
  sous la forme d'un enregistrement par conteneur.
- La réimportation d'une livraison reçue n'échoue plus sur une clé en double,
  et les BOD de livraison reçue sont appliqués dans le bon ordre.
- Les mappages EDI pour la facture, le bon de commande et la confirmation de
  commande sont mis à jour.
- Le test de connexion d'une nouvelle configuration d'export Infor IDM ou
  Infor LN fonctionne.

**Sécurité**

- Le contrôle d'organisation des clés API est appliqué sur chaque
  environnement.

---

## R1.2 — Sandbox 16 février 2027 · Production 3 mars 2027

**Approbation et correspondance des bons de commande**

- Un état « En attente de saisie » met un document en pause jusqu'à ce que
  quelqu'un réponde, sans casser le workflow ni l'historique d'audit, et les
  approbateurs peuvent poser des questions sans interrompre le flux
  d'approbation.
- Un document peut être réassigné à un autre utilisateur (première phase).
- Les factures d'acompte peuvent être rapprochées avant la réception des
  marchandises tandis que « Correspondance sur la quantité reçue » reste actif.
- L'écran de correspondance ne propose que les lignes de bon de commande
  viables, et les correspondances multilignes qui sautent la comparaison des
  prix affichent toujours le prix unitaire sur l'écran d'approbation.
- Un indicateur de disponibilité de réception compare les quantités facturées
  et reçues.
- Confirmations de commande : éléments de coût affichés pendant que
  l'approbation est en attente, positions de surcharge codées par couleur dans
  la correspondance des bons de commande, et la colonne de numéro d'article
  dans les lignes de facture.
- Les lignes RMA fournisseur sont prises en charge.

**Import et classification**

- Le type de fournisseur est dérivé des lignes de la facture.
- Le formulaire de ticket de support accepte les pièces jointes et rattache
  automatiquement l'organisation.

**Paramètres et automatisation**

- Le script « Définir la sous-organisation » devient une règle de
  transformation.
- Les colonnes standard peuvent être retirées d'un type de document.

**Export**

- L'historique des exports liste à nouveau les documents exportés.
- Les factures de fret s'exportent vers Infor LN.
- Les noms de fichiers d'export sont configurables.
- Intégration fiscale Vertex étendue.

---

## R1.3 — Sandbox 1er juin 2027 · Production 16 juin 2027

**Rule Manager Auto Accounting**

- Les règles attribuent automatiquement les comptes et les dimensions, par
  sous-organisation et type de document, avec un écran d'audit qui montre
  quelle règle s'est déclenchée.
- Une règle peut rechercher des données de base et renseigner plusieurs champs
  à la fois, ou renseigner une valeur à partir d'une colonne de ligne de
  tableau.
- Les champs et les dimensions peuvent être effacés individuellement, les
  lignes peuvent être supprimées (y compris les lignes sans montant), et les
  règles continuent de fonctionner sur les champs passés de texte à liste
  déroulante.
- Les prédictions prennent en charge plusieurs codes de taxe et dimensions, les
  pièces comptables et les références de comptabilisation. Les écrans Auto
  Accounting sont disponibles en plusieurs langues.

**Correspondance des bons de commande**

- L'icône de correspondance navigue, fait défiler et met en surbrillance d'un
  onglet à l'autre, y compris pour les correspondances un-à-plusieurs.
- Conversion d'unités avec alias (par exemple KG et TO), un écart d'arrondi
  configurable avec un compte d'arrondi, et des calculs à quatre décimales
  affichés avec trois.

**Ergonomie**

- L'ordre d'exécution des scripts de document est visible dans l'interface.
- Entrée et Tab permettent de passer d'un champ à l'autre au clavier.

**Export**

- Un document incomplet dans Infor LN est supprimé après un export échoué.
- Le connecteur de base de données inclut toutes les tables pertinentes.

---

## R1.4 — Sandbox 5 octobre 2027 · Production 20 octobre 2027

**Auto Accounting sur l'écran d'approbation**

- Les approbateurs peuvent utiliser Auto Accounting directement sur l'écran
  d'approbation.
- L'approbation peut être conditionnée à des champs comptables tels que le
  compte général ou le pays, avec une correction en comptabilité fournisseurs
  lorsqu'un document est renvoyé.
- Une liste déroulante de codes de taxe dans Auto Accounting sans avoir à
  configurer plusieurs lignes de taxe.
- Les dimensions sont stockées dans une nouvelle structure afin que les grands
  ensembles de dimensions se chargent plus rapidement, et le Rule Manager
  bénéficie d'un tour de retours.

**Approbation**

- Un flux d'approbation amélioré, la délégation à un autre utilisateur pendant
  l'approbation, et un bouton « Exporter et suivant ».

**Correspondance des bons de commande et garde-fous à l'export**

- Les factures rapprochées en excès, dont la quantité facturée dépasse la
  quantité reçue, sont reconnues sur l'écran de correspondance, et les unités
  de mesure sont converties lors du rapprochement de la facture.
- Les codes de frais (péage, transport, énergie) sont reconnus et leur coût
  réparti.
- L'export est bloqué avec un avertissement lorsque la quantité rapprochée
  dépasse la quantité reçue ou s'en écarte trop, ou lorsque la date de
  comptabilisation est antérieure à la date d'entrée en entrepôt.

**Import et paramètres**

- Un mécanisme de relance pour l'import FTP, e-mail et e-mail entrant, avec
  retraitement automatique et manuel, et l'adresse de l'expéditeur est
  disponible depuis l'import d'e-mails.
- Les paramètres peuvent être recherchés dans l'ensemble des options et des
  sous-pages.
- La configuration du serveur de messagerie permet de remplacer un secret
  OAuth ou un secret client expiré sans reconfigurer la boîte aux lettres.
- La table de correspondance des numéros d'article fournisseur (table de
  conversion des numéros d'article) peut être alimentée par un import CSV.
- L'historique d'approbation peut être exporté via l'export SFTP.

**DocNet Agents**

- Saisie de commandes : une commande client devient une commande de vente dans
  Infor M3 ou Infor LN (première version, documents texte).

<!-- Generated from Jira "Release No." (customfield_10392) on 2026-10-07 by the
     docbits-roadmap skill. Releases up to R1.4 only; R1.5 and later are not
     published yet. Themes only; ticket keys, customer names and internal work
     are deliberately left out. Rerun the skill to refresh. -->
