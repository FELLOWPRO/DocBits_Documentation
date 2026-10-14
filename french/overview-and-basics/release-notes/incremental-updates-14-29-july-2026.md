# Notes de version DocBits — 14–29 juillet 2026

_Ce qui change avec la mise à niveau de production DocBits du 29 juillet 2026
(mise à jour du canal Nova), couvrant tout ce qui a été livré depuis la version
du 14 juillet. Chaque service indique la version désormais en ligne, suivie des
nouveautés ou corrections expliquées en langage clair. Les services non
répertoriés n'ont connu aucune modification visible par le client._

---

## Points forts

- **Authentification à deux facteurs.** Les comptes DocBits peuvent désormais
  être protégés par un second facteur : une application d'authentification
  (TOTP), un code à usage unique par e-mail, ou une clé d'accès via Touch ID,
  Windows Hello, YubiKey et équivalents. Des codes de secours couvrent la perte
  d'un appareil, et un appareil de confiance peut ignorer le second facteur
  pendant un certain temps. Chaque utilisateur peut l'activer pour lui-même ;
  les administrateurs peuvent l'imposer à toute l'organisation. Voir le
  [guide Authentification à deux facteurs](../two-factor-authentication.md).
- **Tickets de support depuis l'écran d'erreur.** En cas de problème, vous
  pouvez désormais ouvrir un ticket de support directement depuis
  l'enregistrement d'erreur. Le ticket contient déjà le contexte technique ;
  inutile de le décrire vous-même.
- **Import e-mail dans la bonne région.** Les organisations américaines
  disposent d'adresses d'import entrantes dans leur propre région, et les
  boîtes Microsoft 365 hébergées sur des clouds nationaux (GCC, 21Vianet et
  similaires) se configurent désormais via une sélection Cloud Instance.
- **Statut de rapprochement des bons de commande plus clair.** Les factures
  dont le tableau de lignes n'a pas pu être mappé portaient l'étiquette
  « bon de commande introuvable », ce qui orientait les recherches vers le
  mauvais problème. Elles reçoivent désormais leur propre statut « tableau
  incomplet », avec le détail, colonne par colonne, de ce qui n'a pas été
  mappé.
- **Mappage des codes de taxe pour les e-documents.** Une nouvelle page de
  paramètres met en correspondance vos codes de taxe ERP pour les documents
  électroniques, et les exports vérifient ce mappage en amont au lieu
  d'échouer dans l'ERP.
- **Retrait du niveau IA Turbo.** Le modèle Turbo a atteint sa fin de vie.
  Les utilisateurs qui l'avaient sélectionné ont été basculés automatiquement
  vers Fast ; aucune action requise.

---

## Web App — en ligne : `10.46.2`

### Connexion

- **Authentification à deux facteurs :** configurez une application
  d'authentification, des codes par e-mail ou une clé d'accès depuis votre
  profil, imprimez des codes de secours et marquez un appareil comme fiable
  pour ne pas être sollicité à chaque fois. Les utilisateurs de clés d'accès
  peuvent se connecter entièrement sans mot de passe. Les administrateurs
  d'organisation disposent d'un commutateur d'obligation et d'une vue
  d'ensemble de l'adoption indiquant qui s'est enrôlé.
- **Comptes supprimés :** la connexion avec un compte supprimé l'indique, au
  lieu d'échouer sur une erreur générique.
- **SSO :** correction d'une erreur à la connexion lorsqu'une autre région
  était sélectionnée. Les sessions SSO expirent désormais au moment indiqué
  par le fournisseur d'identité, et non selon un minuteur local fixe.

### Travailler avec les documents

- **Documents supprimés :** l'ouverture d'un document supprimé entre-temps
  affiche un message clair au lieu d'erreurs de script.
- **Field Validation :** le champ de numéro de page est plus large et saute à
  la page avec Entrée. Un champ rendu en lecture seule par un script affiche
  toujours sa connexion de champ. Une fenêtre d'avertissement qui affichait du
  JavaScript brut montre désormais le message réel, et l'écran ne se fige plus
  sur les documents comportant de longs tableaux de lignes d'e-documents.
- **Extraction de tableaux :** la suppression d'une colonne libère son nom
  pour réutilisation, et les en-têtes supprimés ne réapparaissent plus dans le
  tableau enregistré.
- **Approbations :** l'ouverture d'un document tout juste mis en attente mène
  au bon écran d'approbation. Les utilisateurs ne peuvent plus approuver une
  étape Sales Tax pour laquelle leur groupe n'a pas d'autorisation, et
  l'historique des approbations affiche à nouveau toutes les entrées.
  L'historique nomme également la personne qui a réellement approuvé, y
  compris lorsqu'un administrateur a approuvé au nom du destinataire.
- **Fournisseurs :** la page Accounting n'affiche plus de faux avertissement
  « Supplier is missing » (fournisseur manquant), et la suppression d'un
  fournisseur issu uniquement de l'extraction ne laisse plus la boîte de
  dialogue bloquée.
- **Données de base :** les tableaux de la page de données de base défilent à
  nouveau.
- **Tâches et notifications :** la suppression d'une tâche n'est plus réservée
  aux administrateurs. Le droit des non-administrateurs à supprimer leurs
  propres tâches est désormais un paramètre d'organisation, et les
  utilisateurs ayant une tâche sur un document qu'ils ne peuvent pas ouvrir
  obtiennent une vue limitée à la tâche au lieu d'une erreur.

### Tableau de bord et recherche

- **Export :** les exports utilisent le tableau de bord que vous avez
  sélectionné, et l'application vous prévient avant l'export d'un tableau de
  bord comportant des modifications non enregistrées.
- **Recherche :** Invoice Type est disponible comme champ de recherche, avec
  sa liste de valeurs. Lorsqu'un ensemble de résultats dépasse ce que la
  fenêtre du tableau de bord peut afficher, la pastille de comptage le signale
  au lieu de tronquer silencieusement.
- **Journal d'import :** les documents scindés se retrouvent via leur document
  parent, et la colonne Failed Filenames ne liste plus que les fichiers
  réellement en échec ou ignorés.

### Paramètres et administration

- **Tickets de support :** créez un ticket directement depuis un
  enregistrement d'erreur. Les tickets embarquent l'environnement et le canal
  de version, et la capture d'écran ne se bloque plus.
- **Groupes et autorisations :** les documents non classifiés peuvent être
  accordés comme autorisation, au même titre que n'importe quel type de
  document.
- **Workflow Builder :** les cartes nouvellement créées ou renommées, les
  modèles d'e-mail et les autres éléments de liste déroulante apparaissent
  immédiatement, sans recharger la page.
- **Arbres de décision :** dans le concepteur, les libellés des champs de
  document suivent la langue de l'interface au lieu d'afficher toujours le nom
  anglais.
- **Types de document :** nouveau paramètre Structured Extraction dans la
  section extraction.
- **Codes de taxe E-Doc :** nouvelle page de paramètres pour mettre en
  correspondance vos codes de taxe ERP pour les documents électroniques (voir
  Points forts).
- **Auto Accounting :** les dimensions s'affichent de façon fiable et non plus
  par intermittence.
- **Sélection du modèle IA :** le niveau Turbo retiré a disparu de la liste
  déroulante ; les sélections existantes affichent Fast.
- **Boîte de dialogue Versions des services :** désormais défilable, elle
  inclut le service Auth Bridge et affiche les noms des canaux de version
  Vesta et Nova.
- **Page d'import :** ne plante plus pour les organisations dont l'entrée
  d'abonnement est vide.

### Corrections mineures

Les notifications toast vides sont supprimées, la boîte de dialogue de
création/modification d'idée défile, les cases à cocher mal alignées des
paramètres de champ sont réalignées, les suppressions de documents bloquées
expliquent pourquoi, et les paramètres E-Document gèrent proprement le passage
de Default à Custom.

## API Service — en ligne : `12.68.1`

- **Authentification à deux facteurs :** tous les chemins de connexion par mot
  de passe passent par le contrôle du second facteur ; aucune route
  d'intégration ne le contourne.
- **Codes de taxe E-Doc :** mappage des codes de taxe ERP pour les documents
  électroniques, avec un contrôle central avant l'export afin que les codes
  manquants soient détectés tôt.
- **Contrôle d'accès :** les administrateurs peuvent accorder aux utilisateurs
  non administrateurs la visibilité des documents non classifiés.
- **Piste d'audit des suppressions :** les documents enregistrent qui les a
  supprimés et quand.
- **Tableaux de bord personnels :** correction des paramètres de partage qui
  ne s'enregistraient pas.
- **Recherche du tableau de bord :** Invoice Type rejoint les champs de
  recherche étendus, et les documents créés par une scission code-barres ou QR
  se retrouvent via leur document parent.
- **Fraîcheur du tableau de bord :** l'actualisation d'un tableau ou le
  retraitement d'un document vide le cache du tableau de bord ; la liste
  n'affiche donc plus les valeurs antérieures à la modification.
- **Téléversements :** les téléversements répétés du même fichier lors d'une
  nouvelle tentative réseau ne créent plus de documents en double.
- **Recherche fournisseur :** les résultats arrivent dès que les données sont
  prêtes, au lieu d'attendre un délai fixe.
- **Export Infor :** les prix unitaires conservent quatre décimales. Les
  exports M3 peuvent inclure des frais de ligne à montant nul, et les lignes
  de coût LN négatives sont envoyées comme avoirs positifs. L'export attend
  également la fin d'un workflow en cours au lieu de s'exécuter en plein
  milieu.
- **Approbations :** une approbation n'est liée à une demande d'approbation
  que si l'approbateur en est le destinataire. Les modifications effectuées
  par un workflow de sa propre initiative sont attribuées à l'utilisateur
  System plutôt qu'à la dernière personne ayant touché au document.
- **Stabilité de connexion :** une défaillance temporaire dans la validation
  des jetons ne déconnecte plus les utilisateurs ; l'application réessaie. Les
  documents bénéficient du même traitement et n'échouent plus purement et
  simplement sur un incident d'authentification passager.
- **Classification :** les règles de source comparent désormais tous les
  champs de source du document, et non des positions fixes.
- **Stabilité de la validation :** un champ sans nom ne fait plus planter la
  validation du document.
- **Modèles IA :** le niveau Turbo (retiré) est basculé vers Fast partout, y
  compris pour les variantes affinées, avec un garde-fou empêchant qu'un
  modèle retiré puisse jamais s'exécuter.
- **Tâches en arrière-plan :** un planificateur bloqué est détecté et
  redémarré, si bien que les tâches récurrentes ne peuvent plus s'arrêter en
  silence.

## Auth Service — en ligne : `1.75.3`

- **Authentification à deux facteurs :** le socle technique de l'entrée des
  Points forts. Applications d'authentification, codes à usage unique par
  e-mail, clés d'accès et appareils de confiance, ainsi que codes de secours,
  obligation par organisation et connexion sans mot de passe par clé d'accès.
  L'enrôlement déconnecte vos autres sessions, le changement de mot de passe
  révoque les appareils de confiance, et les points de terminaison de
  vérification sont limités en débit, avec verrouillage et protection contre
  la réutilisation des codes.
- **Historique de connexion :** les connexions via SSO/SAML apparaissent
  désormais dans l'historique de connexion, et l'horodatage de dernière
  connexion est enregistré de manière fiable pour chaque type de connexion.
  Consulter l'historique de connexion d'un autre utilisateur exige le niveau
  d'administration approprié.
- **Comptes hérités :** la suppression d'un compte utilisateur hérité
  fonctionne à nouveau, au lieu de ne rien faire en silence.
- **Administration des utilisateurs en masse :** ajout en masse d'utilisateurs
  existants aux sous-organisations et aux groupes via CSV, avec correspondance
  par adresse e-mail. Correction également d'un plantage sur les lignes CSV
  inégalement remplies et d'une erreur serveur lors de l'ajout simultané de
  deux nouveaux utilisateurs ou plus.
- **Listes de membres :** les utilisateurs supprimés n'apparaissent plus dans
  les listes de membres des sous-organisations.
- **Authentification unique :** une série de correctifs de durcissement. Les
  jetons expirés renvoient désormais une réponse « expiré » nette, les
  organisations sans configuration SAML reçoivent une vraie réponse
  « introuvable » au lieu d'un mauvais flux de connexion, la déconnexion
  aboutit toujours même si la demande de déconnexion ne peut pas être
  vérifiée, et plusieurs plantages liés à une configuration de fournisseur
  d'identité manquante ont disparu. La durée de vie du jeton renvoyée par le
  fournisseur est transmise à l'application.
- **Jetons de session :** correction de jetons de session à courte durée de
  vie rejetés comme invalides alors qu'ils n'étaient pas expirés.
- **Outillage de gestion :** la région de l'organisation est visible dans
  l'API de gestion, l'utilisateur système d'une organisation peut être
  réattribué, et l'administration des plans et de la consommation dispose de
  points de terminaison dédiés. Ces changements concernent l'outillage interne
  DocBits, pas l'application cliente.

## Email Service — en ligne : `1.40.2`

- **Import dans la bonne région :** les domaines d'e-mail entrants existent
  par région, et les messages arrivant dans la mauvaise région sont transférés
  vers la bonne. Les organisations américaines ne dépendent plus du chemin
  entrant européen.
- **Microsoft 365 :** les tenants de cloud national se configurent via une
  sélection Cloud Instance, ce qui répare les imports O365 pour les clients
  américains. Un tenant invalide produit désormais une erreur de connexion
  claire au lieu d'une erreur serveur, et des identifiants de tenant
  incomplets échouent immédiatement avec un message plutôt qu'en silence.
- **Test de connexion :** le test d'une boîte IMAP qui ne répond pas échoue
  avec un message de dépassement de délai après quelques secondes, au lieu
  d'aboutir à un délai d'attente de passerelle.
- **Hygiène de la boîte de réception :** les e-mails sans pièce jointe sont
  déplacés hors de la boîte de réception au lieu de s'y accumuler.
- **Pas de doublons en cas de nouvelle tentative :** les téléversements vers
  l'API documentaire portent une clé d'idempotence, si bien qu'une livraison
  retentée ne peut pas créer deux fois le même document.
- **Nommage des sources :** les sources O365 avec un dossier configuré
  incluent l'adresse e-mail du compte dans leur nom, afin de distinguer les
  sources similaires. L'adresse de la boîte aux lettres est lue depuis le
  compte authentifié plutôt que depuis un champ saisi à la main.
- **Entretien du journal d'import :** les entrées du journal d'import sont
  conservées 90 jours, puis nettoyées automatiquement.

## PO Match Service — en ligne : `1.59.3`

- **Statut « tableau incomplet » :** les factures dont le tableau de lignes
  n'a pas pu être mappé reçoivent leur propre statut au lieu du trompeur
  « bon de commande introuvable » (voir Points forts). Le tableau de bord
  l'affiche avec l'icône de non-correspondance.
- **Détail d'erreur amélioré :** les échecs de mappage de tableau nomment la
  colonne précise qui n'a pas été mappée.
- **Plus rapide sur les grosses factures :** le rapprochement fondé sur des
  règles regroupe les candidats par numéro d'article et lit les paramètres de
  tolérance une fois par organisation au lieu d'une fois par ligne.
- **Comportement d'API plus propre :** les requêtes portant sur des règles PO
  inexistantes renvoient une vraie réponse « introuvable », et les entrées de
  cache corrompues sont écartées au lieu de provoquer des erreurs répétées.
- **Rapprochement sur le total :** correction d'un bug dans le rapprochement
  avec le total du bon de commande.

## Fulltext Service — en ligne : `1.39.1`

- **Formats de nombres européens :** les montants écrits avec une virgule
  décimale (`1.234,56`) sont normalisés avant indexation, si bien que les
  recherches et filtres sur les montants fonctionnent quel que soit le format.
- **Comptages de résultats honnêtes :** lorsqu'une recherche correspond à plus
  de documents que la fenêtre du tableau de bord n'en renvoie, la réponse le
  signale au lieu de présenter une liste tronquée comme complète.
- **Compteurs ERP :** correction d'une erreur de jeton qui pouvait interrompre
  le flux de comptage en direct sur le tableau de bord.
- **Résilience de l'indexation :** l'indexation encaisse désormais les
  défaillances passagères de la base de données et du service
  d'authentification (nouvelle tentative automatique, repli sur la base
  primaire) et écarte les messages de file malformés au lieu de les retenter
  indéfiniment.

## OCR Service — en ligne : `1.10.3`

- **Ordre de lecture stable :** le texte est lu dans un ordre déterministe ;
  un même document est donc extrait de la même façon à chaque fois.
- **Documents volumineux :** le budget de temps OCR s'adapte à la taille du
  document ; les très gros fichiers n'échouent plus par dépassement de délai.
- **Caractères inhabituels :** un nettoyeur élimine les caractères que le
  moteur OCR ne peut pas représenter, corrigeant les échecs sur les documents
  contenant des symboles exotiques.
- **Moins d'échecs transitoires :** les erreurs temporaires de connexion au
  stockage sont retentées automatiquement, et un processus de travail bloqué
  est détecté selon qu'il consomme réellement du travail.

## Extraction Service — en ligne : `1.53.3`

- **Factures américaines à taxe nulle :** correction d'un cas où la bonne
  paire net/taxe était écartée quand le montant de la taxe est de zéro.
- **Extraction de tableaux :** les tableaux restent modifiables quand le
  mappage configuré attend plus de colonnes que le document n'en fournit, et
  un plantage sur des données de ligne inhabituelles est corrigé.
- **Ordre de lecture stable :** en miroir de la modification OCR ci-dessus,
  afin que l'extraction voie l'ordre des jetons produit par l'OCR.
- **Modèles IA :** retrait du niveau Turbo, en miroir de l'API Service.

## Docflow Service — en ligne : `2.7.3`

- **Rapprochement des bons de commande dans les workflows :** les valeurs de
  comparaison manquantes sont traitées comme des données manquantes et non
  comme une non-correspondance.
- **Cartes de confirmation de commande :** l'acheteur et le responsable sont
  résolus de manière fiable.
- **Cartes de devis :** le journal consigne désormais les cas où un prix
  proposé existe mais se situe en dehors de la plage de dates autorisée, ce
  qui ressemblait auparavant à une donnée manquante.
- **Frais de transport :** quand aucune des deux parties n'a de frais, le cas
  est résolu par la carte opérateur au lieu de rester bloqué.
- **Sécurité :** les jetons d'API de workflow sont validés par rapport à
  l'organisation à laquelle ils appartiennent.
- **Déclenchement plus rapide :** la vérification des workflows actifs est
  mise en cache, et les processus de travail en arrière-plan redémarrent
  proprement au lieu de laisser derrière eux des processus bloqués.

## Barcode Service — en ligne : `1.18.1`

- **Scissions de longue durée :** la connexion à la file de tâches est
  maintenue pendant les longs traitements de codes-barres ; la scission de
  gros lots ne cale plus juste avant la fin.

## FTP Service — en ligne : `1.31.2`

- **Entretien du journal d'import :** même conservation de 90 jours et même
  nettoyage automatique que pour l'Email Service.

## Auth Bridge Service — en ligne : `0.4.1`

- **Alertes de réplication justes :** le pont de réplication des comptes
  EU/US mesure un blocage à partir de la dernière progression réelle et non
  de la première erreur, et ne compte comme progression qu'une véritable
  activité de réplication. Les fausses alertes nocturnes « pont bloqué » ont
  disparu. Rien ne change dans l'application.

## Operator Service — en ligne : `1.42.1`

- **Stabilité des processus de travail :** un processus de travail bloqué est
  détecté selon qu'il consomme du travail, et les échanges inutiles entre
  processus sont désactivés.

---

## Inchangés dans cette version

**Auto Accounting** (`1.21.1`) a été reconstruit sans aucun changement visible
par le client. **Docnet** (`1.55.1`) et **Ideas** (`0.3.1`) ne comportent aucun
changement sur cette période.

<!-- Generated by the docbits-changelog skill. Boundary: versions live in the
     prod namespace on 28 Jul 2026 (Web App 10.41.8, API 12.57.8, Auth 1.71.1)
     up to the versions live in the sandbox namespace the same day, which is
     what the 29 July upgrade promotes. Re-check the version headers on the
     morning of the upgrade in case anything else lands on sandbox first.
     Manage Layouts and Custom Validation Rules stay excluded: DOCB-13719 gates
     both behind a beta query parameter, so they are not generally available in
     10.46.2. The hourly password for script changes (DOCB-13673) was added and
     then reverted inside this window, so it must not be announced. -->
