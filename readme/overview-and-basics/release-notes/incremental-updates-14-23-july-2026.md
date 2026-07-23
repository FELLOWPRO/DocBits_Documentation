# Notes de version DocBits — 14–23 juillet 2026

_Ce qui change avec la mise à niveau de production DocBits du 23 juillet 2026
(mise à jour du canal Nova), couvrant tout ce qui a été livré depuis la version
du 14 juillet. Chaque service indique la version désormais en ligne, suivie des
nouveautés ou corrections expliquées en langage clair. Les services non
répertoriés n'ont connu aucune modification visible par le client._

---

## Points forts

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
- **Les modifications de scripts sont protégées par mot de passe.** Les
  scripts personnalisés peuvent modifier la façon dont les documents sont
  traités ; chaque modification de script exige donc désormais un mot de passe
  qui change toutes les heures. Demandez le mot de passe en vigueur à votre
  administrateur.
- **Retrait du niveau IA Turbo.** Le modèle Turbo a atteint sa fin de vie.
  Les utilisateurs qui l'avaient sélectionné ont été basculés automatiquement
  vers Fast ; aucune action requise.

---

## Web App — en ligne : `10.45.1`

### Travailler avec les documents

- **Documents supprimés :** l'ouverture d'un document supprimé entre-temps
  affiche un message clair au lieu d'erreurs de script.
- **Field Validation :** le champ de numéro de page est plus large et saute à
  la page avec Entrée. Un champ rendu en lecture seule par un script affiche
  toujours sa connexion de champ.
- **Extraction de tableaux :** la suppression d'une colonne libère son nom
  pour réutilisation, et les en-têtes supprimés ne réapparaissent plus dans le
  tableau enregistré.
- **Approbations :** les utilisateurs ne peuvent plus approuver une étape
  Sales Tax pour laquelle leur groupe n'a pas d'autorisation, et l'historique
  des approbations affiche à nouveau toutes les entrées. L'historique nomme
  également la personne qui a réellement approuvé, y compris lorsqu'un
  administrateur a approuvé au nom du destinataire.
- **Fournisseurs :** la page Accounting n'affiche plus de faux avertissement
  « Supplier is missing » (fournisseur manquant), et la suppression d'un
  fournisseur issu uniquement de l'extraction ne laisse plus la boîte de
  dialogue bloquée.
- **Tâches et notifications :** l'option de suppression est masquée pour les
  utilisateurs sans droits d'administration.

### Tableau de bord et recherche

- **Export :** les exports utilisent le tableau de bord que vous avez
  sélectionné, et l'application vous prévient avant l'export d'un tableau de
  bord comportant des modifications non enregistrées.
- **Recherche :** Invoice Type est disponible comme champ de recherche, avec
  sa liste de valeurs.
- **Journal d'import :** les documents scindés se retrouvent via leur document
  parent, et la colonne Failed Filenames ne liste plus que les fichiers
  réellement en échec ou ignorés.

### Connexion

- **Comptes supprimés :** la connexion avec un compte supprimé l'indique, au
  lieu d'échouer sur une erreur générique.
- **SSO :** correction d'une erreur à la connexion lorsqu'une autre région
  était sélectionnée.

### Paramètres et administration

- **Tickets de support :** créez un ticket directement depuis un
  enregistrement d'erreur. Les tickets embarquent l'environnement et le canal
  de version, et la capture d'écran ne se bloque plus.
- **Workflow Builder :** les cartes nouvellement créées ou renommées, les
  modèles d'e-mail et les autres éléments de liste déroulante apparaissent
  immédiatement, sans recharger la page.
- **Types de document :** nouveau paramètre Structured Extraction dans la
  section extraction.
- **Codes de taxe E-Doc :** nouvelle page de paramètres pour mettre en
  correspondance vos codes de taxe ERP pour les documents électroniques (voir
  Points forts).
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

## API Service — en ligne : `12.64.3`

- **Sécurité des scripts :** les modifications de scripts exigent un mot de
  passe à durée limitée (voir Points forts).
- **Codes de taxe E-Doc :** mappage des codes de taxe ERP pour les documents
  électroniques, avec un contrôle central avant l'export afin que les codes
  manquants soient détectés tôt.
- **Contrôle d'accès :** les administrateurs peuvent accorder aux utilisateurs
  non administrateurs la visibilité des documents non classifiés.
- **Tableaux de bord personnels :** correction des paramètres de partage qui
  ne s'enregistraient pas.
- **Recherche du tableau de bord :** Invoice Type rejoint les champs de
  recherche étendus, et les documents créés par une scission code-barres ou QR
  se retrouvent via leur document parent.
- **Téléversements :** les téléversements répétés du même fichier lors d'une
  nouvelle tentative réseau ne créent plus de documents en double.
- **Recherche fournisseur :** les résultats arrivent dès que les données sont
  prêtes, au lieu d'attendre un délai fixe.
- **Export Infor :** les prix unitaires conservent quatre décimales. Les
  exports M3 peuvent inclure des frais de ligne à montant nul, et les lignes
  de coût LN négatives sont envoyées comme avoirs positifs.
- **Approbations :** une approbation n'est liée à une demande d'approbation
  que si l'approbateur en est le destinataire.
- **Stabilité de connexion :** une défaillance temporaire dans la validation
  des jetons ne déconnecte plus les utilisateurs ; l'application réessaie.
- **Classification :** les règles de source comparent désormais tous les
  champs de source du document, et non des positions fixes.
- **Stabilité de la validation :** un champ sans nom ne fait plus planter la
  validation du document.
- **Modèles IA :** le niveau Turbo (retiré) est basculé vers Fast partout, y
  compris pour les variantes affinées, avec un garde-fou empêchant qu'un
  modèle retiré puisse jamais s'exécuter.

## Auth Service — en ligne : `1.72.8`

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
  d'identité manquante ont disparu.
- **Jetons de session :** correction de jetons de session à courte durée de
  vie rejetés comme invalides alors qu'ils n'étaient pas expirés.
- **Outillage de gestion :** la région de l'organisation est visible dans
  l'API de gestion, l'utilisateur système d'une organisation peut être
  réattribué, et l'administration des plans et de la consommation dispose de
  points de terminaison dédiés. Ces changements concernent l'outillage interne
  DocBits, pas l'application cliente.

## Email Service — en ligne : `1.39.9`

- **Import dans la bonne région :** les domaines d'e-mail entrants existent
  par région, et les messages arrivant dans la mauvaise région sont transférés
  vers la bonne. Les organisations américaines ne dépendent plus du chemin
  entrant européen.
- **Microsoft 365 :** les tenants de cloud national se configurent via une
  sélection Cloud Instance, ce qui répare les imports O365 pour les clients
  américains. Un tenant invalide produit désormais une erreur de connexion
  claire au lieu d'une erreur serveur, et des identifiants de tenant
  incomplets échouent immédiatement avec un message plutôt qu'en silence.
- **Hygiène de la boîte de réception :** les e-mails sans pièce jointe sont
  déplacés hors de la boîte de réception au lieu de s'y accumuler.
- **Pas de doublons en cas de nouvelle tentative :** les téléversements vers
  l'API documentaire portent une clé d'idempotence, si bien qu'une livraison
  retentée ne peut pas créer deux fois le même document.
- **Nommage des sources :** les sources O365 avec un dossier configuré
  incluent l'adresse e-mail du compte dans leur nom, afin de distinguer les
  sources similaires.
- **Entretien du journal d'import :** les entrées du journal d'import sont
  conservées 90 jours, puis nettoyées automatiquement.

## PO Match Service — en ligne : `1.59.1`

- **Statut « tableau incomplet » :** les factures dont le tableau de lignes
  n'a pas pu être mappé reçoivent leur propre statut au lieu du trompeur
  « bon de commande introuvable » (voir Points forts). Le tableau de bord
  l'affiche avec l'icône de non-correspondance.
- **Détail d'erreur amélioré :** les échecs de mappage de tableau nomment la
  colonne précise qui n'a pas été mappée.
- **Comportement d'API plus propre :** les requêtes portant sur des règles PO
  inexistantes renvoient une vraie réponse « introuvable », et les entrées de
  cache corrompues sont écartées au lieu de provoquer des erreurs répétées.
- **Rapprochement sur le total :** correction d'un bug dans le rapprochement
  avec le total du bon de commande.

## Fulltext Service — en ligne : `1.38.3`

- **Formats de nombres européens :** les montants écrits avec une virgule
  décimale (`1.234,56`) sont normalisés avant indexation, si bien que les
  recherches et filtres sur les montants fonctionnent quel que soit le format.
- **Compteurs ERP :** correction d'une erreur de jeton qui pouvait interrompre
  le flux de comptage en direct sur le tableau de bord.
- **Résilience de l'indexation :** l'indexation encaisse désormais les
  défaillances passagères de la base de données et du service
  d'authentification (nouvelle tentative automatique, repli sur la base
  primaire) et écarte les messages de file malformés au lieu de les retenter
  indéfiniment.

## OCR Service — en ligne : `1.9.9`

- **Documents volumineux :** le budget de temps OCR s'adapte à la taille du
  document ; les très gros fichiers n'échouent plus par dépassement de délai.
- **Caractères inhabituels :** un nettoyeur élimine les caractères que le
  moteur OCR ne peut pas représenter, corrigeant les échecs sur les documents
  contenant des symboles exotiques.
- **Moins d'échecs transitoires :** les erreurs temporaires de connexion au
  stockage sont retentées automatiquement.

## Extraction Service — en ligne : `1.52.0`

- **Factures américaines à taxe nulle :** correction d'un cas où la bonne
  paire net/taxe était écartée quand le montant de la taxe est de zéro.
- **Extraction de tableaux :** les tableaux restent modifiables quand le
  mappage configuré attend plus de colonnes que le document n'en fournit, et
  un plantage sur des données de ligne inhabituelles est corrigé.
- **Modèles IA :** retrait du niveau Turbo, en miroir de l'API Service.

## Docflow Service — en ligne : `2.7.2`

- **Rapprochement des bons de commande dans les workflows :** les valeurs de
  comparaison manquantes sont traitées comme des données manquantes et non
  comme une non-correspondance.
- **Cartes de confirmation de commande :** l'acheteur et le responsable sont
  résolus de manière fiable.
- **Frais de transport :** quand aucune des deux parties n'a de frais, le cas
  est résolu par la carte opérateur au lieu de rester bloqué.
- **Sécurité :** les jetons d'API de workflow sont validés par rapport à
  l'organisation à laquelle ils appartiennent.
- **Déclenchement plus rapide :** la vérification des workflows actifs est
  mise en cache, et les processus de travail en arrière-plan redémarrent
  proprement au lieu de laisser derrière eux des processus bloqués.

## Barcode Service — en ligne : `1.17.4`

- **Scissions de longue durée :** la connexion à la file de tâches est
  maintenue pendant les longs traitements de codes-barres ; la scission de
  gros lots ne cale plus juste avant la fin.

## FTP Service — en ligne : `1.31.2`

- **Entretien du journal d'import :** même conservation de 90 jours et même
  nettoyage automatique que pour l'Email Service.

---

## Inchangés dans cette version

**Auth Bridge** (`0.3.6`), **Auto Accounting** (`1.20.1`), **Docnet**
(`1.55.1`), **Operator** (`1.40.2`) et **Ideas** (`0.3.1`) ne comportent
aucun changement sur cette période.

<!-- Generated by the docbits-changelog skill (version-boundary mode), then
     reconciled on 23 Jul 2026 against the Nova versions actually deployed
     (Web App 10.45.1, API 12.64.3, Auth 1.72.8, Email 1.39.9, PO Match
     1.59.1, OCR 1.9.9, Docflow 2.7.2, FTP 1.31.2). Manage Layouts and
     Custom Validation Rules were removed from this page: DOCB-13719 gated
     both behind a beta query parameter, so they are not generally available
     in 10.45.1. -->
