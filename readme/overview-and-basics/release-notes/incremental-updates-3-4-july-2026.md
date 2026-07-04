# Notes de version DocBits — 3–4 juillet 2026

_Ce que cette mise à niveau de production a apporté, en langage clair. Chaque
service indique la version désormais en ligne en production. Les services non
répertoriés n'ont connu aucune modification visible par le client durant cette
période._

---

## Points forts

- **Des déploiements plus propres, sur toute la flotte.** Plusieurs services
  principaux (API, Auto Accounting, Docflow, Extraction, OCR, PO Match)
  s'arrêtent désormais correctement pendant une release, si bien qu'un
  déploiement progressif ne risque plus d'interrompre une requête déjà en
  cours.
- **Améliorations de l'export des factures électroniques.** L'export d'un
  document vers plusieurs configurations d'export à la fois est désormais
  plus fiable — les vérifications anti-doublon d'export s'exécutent
  désormais une seule fois par lot au lieu d'une fois par élément, et un
  nouveau point de terminaison d'export évite que le statut d'export ne
  clignote lorsque plusieurs exports sont déclenchés ensemble. Les documents
  XRechnung/ZUGFeRD bénéficient également d'un mappage de champs plus
  cohérent.
- **Traitement des documents plus stable.** Correction d'un plantage qui
  pouvait faire échouer tout un document OCR lorsqu'une seule page échouait,
  correction de la synchronisation des livraisons de bons de commande qui ne
  récupérait toujours que les 100 premiers enregistrements, et renforcement
  de plusieurs services face aux brèves coupures de connexion à la base de
  données.
- **Pièces jointes e-mail récupérées.** Correction d'un cas où les pièces
  jointes des e-mails pouvaient arriver corrompues ou avec des octets
  manquants lors de l'import entrant.
- **Fiabilité des workflows.** Correction des workflows qui restaient bloqués
  à cause d'un verrou qui ne se libérait pas correctement, et correction de
  la logique de replanification afin que les étapes de workflow ignorées
  soient correctement traitées et journalisées.
- **Nouveau : Ideas Service.** Un nouveau service backend (Ideas, v0.3.0) a
  rejoint la flotte de production.

---

## API Service — en ligne : `12.52.4`

- **Fiabilité OCR :** un plantage sur une seule page ne fait plus échouer
  l'ensemble du document.
- **Export :** les vérifications anti-doublon d'export s'exécutent désormais
  une seule fois par lot au lieu d'une fois par élément ; un nouveau point de
  terminaison d'export évite que le statut d'export ne clignote lorsque
  plusieurs exports s'exécutent en même temps ; les documents
  XRechnung/ZUGFeRD bénéficient d'un mappage de champs canonique plus
  cohérent.
- **Bons de commande :** correction de la synchronisation des livraisons qui
  ne récupérait que les 100 premiers enregistrements par commande.
- **Activity Logs :** correction du bouton de page « Suivant » qui
  redirigeait vers une période sans rapport.
- **Master Data Lookup :** correction d'une erreur serveur (HTTP 500).
- **Indexation de recherche :** ajout d'un marqueur de preuve de livraison et
  d'une nouvelle tentative afin que les documents soient mis en file
  d'attente de manière fiable pour la recherche plein texte.
- Corrections générales de stabilité résolvant plusieurs erreurs de fond
  récurrentes.

## Auth Service — en ligne : `1.68.7`

- Fiabilité et maintenance internes uniquement durant cette période.

## Auto Accounting — en ligne : `1.18.8`

- **Arrêts plus propres** pendant les déploiements, évitant les requêtes en
  cours interrompues.

## Barcode Service — en ligne : `1.15.8`

- Correction de configuration de déploiement interne uniquement durant cette
  période.

## Docflow Service — en ligne : `2.5.3`

- **Nouvelle option d'export** pour envoyer un document vers plusieurs
  configurations d'export à la fois.
- **Correction des workflows qui restaient bloqués** à cause d'un verrou qui
  ne se libérait pas correctement, quel que soit le statut.
- **Correction de la replanification des workflows** afin que les étapes
  ignorées soient correctement traitées et journalisées au lieu d'être
  silencieusement abandonnées.
- **Démarrage plus rapide :** les bases de données sont désormais
  préchauffées en arrière-plan.
- Plus résilient face aux brèves coupures de connexion à la base de données.
- Amélioration de l'analyse des champs de date pour les cartes de workflow.

## Email Service — en ligne : `1.37.9`

- **Correction des pièces jointes entrantes** qui pouvaient arriver
  corrompues ou avec des octets manquants.
- **Erreurs plus claires** lorsqu'un dossier de boîte aux lettres ne peut pas
  être récupéré, au lieu d'un échec générique.

## Extraction Service — en ligne : `1.49.6`

- **Correction de plantages** sur les documents dont le type n'est pas
  reconnu et sur les tableaux de forme inhabituelle/malformée.
- Plus résilient face aux brèves coupures de connexion à la base de données
  en cours de requête.

## FTP Service — en ligne : `1.30.3`

- Mise à niveau interne du framework uniquement durant cette période.

## Fulltext Service — en ligne : `1.36.3`

- **Indexation de recherche :** un balayage périodique répare désormais tout
  document qui n'avait pas atteint l'index de recherche, pour n'importe
  quelle organisation.
- **Synchronisation ERP :** correction d'un verrou bloqué qui pouvait
  empêcher la synchronisation ERP après une nouvelle tentative échouée.

## OCR Service — en ligne : `1.7.8`

- **Correction de l'authentification OCR** afin que les clés API
  d'organisation fonctionnent à nouveau correctement.
- Arrêts plus propres pendant les déploiements.

## Operator Service — en ligne : `1.39.7`

- Corrections internes de fiabilité de déploiement uniquement durant cette
  période.

## PO Match Service — en ligne : `1.56.0`

- **Correction d'un plantage** lors du tri des quantités PO Match incluant
  des valeurs vides.
- Arrêts plus propres pendant les déploiements.

## Web App — en ligne : `10.36.9`

- **Correction d'une erreur** lors du retour à Field Validation depuis un
  autre écran.
- **Correction du bouton « Scripts »** qui redirigeait vers une page 404.
- **Activity Logs :** correction d'un affichage incorrect « Page 2 sur 1 » et
  correction du filtre de sévérité WARN qui ne trouvait aucun résultat.

---

## Aucune modification visible par le client durant cette période

Auth Service, Barcode Service, FTP Service, Operator Service et Docnet
Service (`1.54.6`, inchangé) n'ont reçu qu'une maintenance interne ou de
configuration de déploiement.

<!-- Generated by the docbits-changelog skill (version-boundary mode: exact
     git ranges between the ALT and NEU version-bump commits supplied by the
     user, per service). Window ~2026-07-01 → 2026-07-04. -->
