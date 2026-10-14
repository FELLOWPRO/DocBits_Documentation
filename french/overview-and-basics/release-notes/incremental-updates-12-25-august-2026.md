# Notes de version DocBits — 12–25 août 2026

_Ce qui change avec la mise à niveau de production DocBits du 25 août 2026,
couvrant tout ce qui a été livré depuis la version du 12 août. Chaque service
indique la version déployée, suivie des nouveautés ou corrections expliquées
en langage clair. Les services non répertoriés n'ont connu aucune modification
visible par le client._

---

## Points forts

- **Isolation des organisations renforcée.** Un audit de sécurité a fermé
  plusieurs points où les données d'une organisation pouvaient être lues ou
  modifiées depuis une autre : les scripts de document, les listes
  d'utilisateurs des sous-organisations, les appartenances aux groupes et le
  jeton de traitement qu'un document transporte tout au long du pipeline sont
  désormais tous vérifiés par rapport à l'organisation de l'appelant. Les
  approbations appliquent aussi correctement le principe des quatre yeux : le
  second approbateur doit être une personne différente de la première.
- **Les documents ne restent plus bloqués.** Quatre causes distinctes de
  documents suspendus indéfiniment ont été corrigées : des exports qui
  restaient en « Exporting » après un refus, des redémarrages figés lorsqu'une
  étape de traitement plantait, des scissions par code-barres qui ne rendaient
  jamais compte, et l'écran de comptabilité bloqué sur « Preparing… ». Dans
  chaque cas, le document se termine désormais ou affiche une véritable erreur
  sur laquelle vous pouvez agir.
- **Les avoirs sont reconnus comme des avoirs.** Les avoirs XRechnung 3.0,
  3.0.1 et 3.0.2 en syntaxe CII, les avoirs CII purs et les documents
  ZUGFeRD 2.4 / Factur-X 1.08 sont désormais tous classifiés correctement,
  avec le total lu dans le bon champ. Les documents numérisés qui mentionnent
  à la fois « facture » et « avoir » sont départagés selon le mot-clé le plus
  proche du type de document, et les montants redeviennent positifs lorsque
  vous reclassez un avoir en facture.
- **Le rapprochement des bons de commande fait des calculs fiables.** Les
  tolérances sont comparées en décimales exactes plutôt qu'en valeurs à
  virgule flottante, sont basées sur la valeur du bon de commande, et les
  factures qui référencent plusieurs bons de commande sont rapprochées de
  chacun d'eux. Les colonnes que vous n'avez jamais mappées ne faussent plus
  le contrôle du montant des lignes, et lorsque des colonnes obligatoires
  manquent, l'erreur les nomme.
- **Les exécutions de workflow conservent leur travail.** Un workflow qui
  écrit une valeur de champ l'inscrit désormais sur le document d'une manière
  qu'un export ultérieur ne peut plus annuler silencieusement. Les
  déclencheurs relancés ne perdent plus ce que l'exécution avait déjà
  accompli, et deux déclencheurs visant le même document se mettent en file
  d'attente au lieu de se voler mutuellement le verrou.
- **Les e-mails de réinitialisation de mot de passe partent à nouveau.** Ils
  ne quittaient silencieusement jamais le serveur. Le formulaire de
  réinitialisation affiche aussi un vrai retour après l'envoi, et la réponse
  ne révèle plus si un compte existe.

---

## Web App — `10.55.0`

### Connexion et comptes

- La réinitialisation de mot de passe fonctionne à nouveau de bout en bout :
  l'e-mail arrive, le formulaire confirme l'envoi, et la réponse est identique
  que l'adresse possède un compte ou non.
- Si votre organisation exige l'enrôlement à deux facteurs, l'écran de
  connexion l'indique désormais au lieu d'échouer sans message.
- Les administrateurs ne peuvent plus activer l'obligation de MFA à l'échelle
  de l'organisation avant que l'enrôlement à la connexion soit disponible, ce
  qui pouvait auparavant bloquer l'accès des utilisateurs.

### Écran de validation

- Le curseur de zoom monte désormais jusqu'à 150 % (il s'arrêtait à 80 %), et
  zoomer dans un tableau fonctionne au-delà de la largeur du conteneur au lieu
  de ne rien faire.
- Les champs de montant vides comptent comme 0 au lieu de déclencher un
  message d'erreur, et un double clic sur l'image du document est ignoré
  lorsqu'aucun champ n'est sélectionné.
- Le bandeau affiché lorsqu'une autre session détient le verrou du document
  n'avait aucun texte ; il s'explique désormais. Étiqueter un tableau ne
  déclenche plus de faux avertissement « document modifié en externe » à
  propos de votre propre modification.
- Dans le tableau IA, un remappage de colonne qui démapperait une autre
  colonne demande d'abord confirmation, et les valeurs qui ne sont pas des
  nombres sont signalées dans les colonnes AMOUNT et NUMBER.
- L'onglet « Extracted table » renvoie à nouveau vers l'entraînement manuel
  des tableaux lorsqu'il est vide.
- Les numéros d'article du tableau de comparaison des lignes sont affichés
  comme des identifiants, et non arrondis comme des montants.
- Les champs d'approbateur résolvent les identifiants d'utilisateurs et de
  groupes en noms, si bien qu'ils n'affichent jamais un identifiant brut et ne
  restent jamais vides. Les échéances de tâches sont converties via un chemin
  unique tenant compte de l'UTC, de sorte que chaque utilisateur voit la même
  date.
- Les documents renvoyés en validation affichent un indicateur de chargement
  au lieu d'un écran figé pendant leur préparation.

### Comptabilité

- Les lignes ventilées conservent leur signe % après appui sur Entrée, et
  0 % est accepté comme valeur.
- Dans le filtre de comptes, Entrée valide le premier compte correspondant au
  lieu de ne rien faire.
- Les caractères de flexdimension sont mappés par identifiant de dimension, de
  sorte que les dimensions atterrissent dans la bonne colonne même lorsque
  l'ordre diffère.
- Une préparation comptable en échec se rétablit avec un message d'erreur au
  lieu de rester bloquée indéfiniment sur « Preparing… », et la réouverture
  d'un document ne sert plus les données périmées du document précédent.

### Rapprochement des bons de commande

- Ouvrir PO Matching sans que toutes les colonnes obligatoires soient mappées
  est à nouveau possible ; lorsqu'un élément nécessaire manque, le message
  nomme les colonnes exactes.
- Les colonnes qui ne sont mappées à rien sont masquées à l'ouverture de
  l'écran, après une unique demande de confirmation, et elles n'entrent plus
  dans le calcul du montant des lignes.
- La quantité rapprochée se rafraîchit après l'enregistrement, et la fenêtre
  de colonne manquante vous dirige vers Field Validation, où vous pouvez
  corriger le problème.

### Tableau de bord et recherche

- Les colonnes basées sur des listes déroulantes (type de facture, statut et
  similaires) affichent leur libellé dans la langue de votre interface au lieu
  de la valeur brute stockée.
- La recherche en texte libre accepte les parenthèses comme du texte
  ordinaire ; elle rejetait auparavant la requête. L'opérateur de filtre
  « différent de » reste sélectionné, et la modification manuelle d'un filtre
  ne corrompt plus le nom du champ.
- La sélection d'une sous-organisation dans la recherche rapide insère son
  nom, et non son uuid, et l'autocomplétion des sous-organisations ne liste
  plus de doublons.
- Le tableau de bord peut désormais récupérer jusqu'à 10 000 documents par
  fenêtre de recherche, de sorte que les grands ensembles de résultats se
  paginent correctement.
- Le panneau des documents en double affiche les mêmes colonnes résolues que
  la liste principale, et les valeurs de filtre fournisseur composées de
  plusieurs mots survivent à l'appui sur Entrée.

### Tâches

- L'e-mail d'affectation part lorsqu'une tâche est affectée, une seule fois.
  Modifier une tâche ou la marquer comme terminée ne le renvoie plus, et la
  date « assigned on » reste la date de l'affectation. Les e-mails de tâches
  s'affichent également correctement dans Outlook.

### Workflow Builder

- La recherche, l'ordre de tri et la pagination de la liste des workflows
  restent cohérents pendant que vous filtrez.
- Le commutateur « run workflow on change » du concepteur de mise en page
  conditionne désormais réellement l'exécution, et son activation exige de
  choisir un workflow.

### Paramètres et administration

- Le lien de téléchargement de WatchDog et la commande d'installation pointent
  vers l'environnement dans lequel vous vous trouvez, et non plus toujours
  vers la production.
- Arbres de décision : le champ de document sélectionné reste en surbrillance
  à la réouverture du sélecteur, les libellés tronqués reçoivent une
  infobulle, et des noms d'utilisateurs (et non des identifiants bruts)
  s'affichent lors de l'ajout d'une ligne.
- La case System Admin est modifiable lors de la modification d'un
  utilisateur.
- Analytics : les Core Web Vitals sont rendus à partir des vraies données de
  mesure, et la vue du service de journaux fonctionne.
- « Use Default Template » dans le gestionnaire de mises en page copie la mise
  en page par défaut comme prévu.
- Les libellés de champs personnalisés n'écrasent plus les traductions
  intégrées des champs standard.
- Devis du portail fournisseurs : l'envoi d'un devis avec une valeur REF1 hors
  de la liste autorisée est bloqué.
- MediOrder bénéficie de la détection des documents en double sur son écran de
  validation.

## API Service — `12.82.3`

### Sécurité et isolation des organisations

- Le changement d'organisation active est validé par rapport à votre
  appartenance réelle et échoue de manière sûre, et un point de terminaison de
  test interne qui pouvait être détourné pour franchir les frontières entre
  organisations a été fermé.
- Les scripts de document ne peuvent plus être lus ni écrasés d'une
  organisation à l'autre, ni via l'appel qui applique un script à un document,
  ni via un identifiant de version étranger lors de l'enregistrement.
- Les listes d'utilisateurs des sous-organisations et les listes de membres de
  groupes ne renvoient que des personnes de l'organisation de l'appelant, et
  l'ajout simultané de plusieurs utilisateurs à un groupe n'ignore plus tous
  les utilisateurs sauf le premier.
- Un identifiant d'accès provenant de la mauvaise organisation est refusé
  avant de pouvoir devenir le jeton de traitement d'un document, et les
  requêtes de recherche en texte intégral s'exécutent au nom de l'utilisateur
  appelant plutôt que d'une identité de service.
- Le principe des quatre yeux est appliqué aux approbations : le second
  approbateur doit être différent de la personne qui a approuvé en premier.
- La liste du PO Dashboard en direct est limitée aux sous-organisations de
  l'utilisateur.

### Pipeline de documents

- Les documents refusés à l'export ne restent plus indéfiniment en
  « Exporting », et les erreurs d'export portent toujours un message au lieu
  d'un message vide.
- Lorsqu'une étape de traitement plante, le document passe en état d'erreur au
  lieu de rester bloqué en « restart in progress » sans issue.
- Une scission par code-barres qui échoue ou expire marque le document en
  Erreur au lieu d'afficher silencieusement « Running », et une scission qui
  ne produit aucun document enfant conserve le document parent et le signale
  au lieu de tout supprimer.
- Une relance en échec ne peut plus écraser un document dont le traitement
  s'est terminé entre-temps.
- Les documents redémarrés sans interaction utilisateur et les documents
  enfants issus d'une scission s'exécutent désormais sous un jeton
  d'organisation durable, de sorte qu'un traitement de longue durée ne meurt
  plus avec une session expirée.
- Une réponse de modèle de mise en page vide n'est plus mise en cache pendant
  six heures, ce qui faisait disparaître les mises en page jusqu'à
  l'expiration du cache.

### Extraction et e-documents

- Les montants écrits avec un signe moins final (« 100,00- ») sont interprétés
  comme négatifs au lieu d'être ignorés.
- Les documents suisses sont détectés comme suisses (CHF, numéros de TVA CHE,
  IBAN CH) au lieu de retomber sur les conventions allemandes, et les dates
  écrites avec des tirets typographiques sont analysées correctement.
- Les avoirs XRechnung 3.0, 3.0.1 et 3.0.2 en syntaxe CII sont classifiés
  comme avoirs, avec le total lu dans le champ du total général ; il en va de
  même pour les avoirs CII purs. Une version ZUGFeRD 2.4 / Factur-X 1.08
  déclarée l'emporte sur l'identifiant de profil générique, et les types
  XRechnung sans précision se résolvent vers leur équivalent UBL ou CII au
  lieu d'échouer.
- Les champs à liste de valeurs (listes déroulantes) tels que Tax Country et
  Tax Code conservent leur valeur lors de la transformation des champs ; ils
  étaient vidés.
- Extraction de tableaux : un échec dans une colonne exclusivement numérique
  reste confiné à cette colonne au lieu de faire échouer tout le tableau,
  l'extraction de tableaux par IA reçoit un délai d'expiration qui survit aux
  exécutions multi-lots, et deux plantages sur des formes de tableau
  inhabituelles (lignes sans position de page, nombres de colonnes
  irréguliers) sont corrigés.
- Les motifs des règles de source correspondent sans distinction de casse.

### Export

- Un contrôle de taxe qui échoue pendant l'aperçu d'export renvoie une erreur
  lisible au lieu d'une erreur serveur, sur les deux points de terminaison
  d'aperçu.
- L'export SFTP peut envoyer le document original en plus du document
  converti.
- Lorsque des configurations d'export existent à plusieurs niveaux, la plus
  spécifique l'emporte de manière cohérente.
- Les exports BOD peuvent transporter des attributs de type de colonne via le
  mappage.

### Import et données de base

- Le journal d'import e-mail est complet : les e-mails entrants rejetés ou en
  échec reçoivent toujours une ligne de journal avec un motif exact. Plus
  aucune perte silencieuse.
- Les imports BOD de bons de commande gardent les sous-lignes attachées à la
  bonne ligne ; un indicateur reporté les attachait auparavant à la mauvaise.
- L'import d'un CSV contenant plusieurs nouveaux fournisseurs fonctionne
  (leurs identifiants générés n'entrent plus en collision), les alias de
  conditions d'escompte s'importent et respectent le paramètre « on
  conflict », et le choix IGNORE en cas de conflit s'applique au-delà des
  fournisseurs.
- La suggestion de fournisseur (TF-IDF) conserve son identifiant de
  fournisseur lorsqu'une préférence est mise à jour, de sorte que les
  suggestions ne pointent plus vers le vide.

### Autres corrections

- Les lignes du tableau de bord résolvent les libellés des listes déroulantes
  dans la langue de l'utilisateur, sans bloquer la requête.
- Après modification des champs, le statut de rapprochement PO se met à jour
  au lieu d'afficher l'état antérieur à la modification.
- Les documents Purchase Order Change reçoivent cinq champs à parité avec les
  bons de commande et une mise en page de validation de champs par défaut.
- Les réponses d'erreur de 152 points de terminaison renvoient des messages
  lisibles au lieu d'objets d'exception bruts, et la page d'analyse des
  journaux ne répond plus par une erreur 502 pour les organisations sans index
  de journaux.

## Auth Service — `1.77.9`

- Les e-mails de réinitialisation de mot de passe ne partaient silencieusement
  jamais ; c'est corrigé, ainsi que le problème de sécurité des threads
  sous-jacent.
- Un jeton de rafraîchissement rejoué est rejeté : la vérification de
  référence en base de données s'exécute désormais à chaque fois au lieu
  d'être sautée lors d'un accès au cache.
- Authentification à deux facteurs : une application d'authentification peut
  être enrôlée en parallèle des codes par e-mail, et la suppression de la
  dernière clé d'accès ou la régénération des codes de secours exige au
  préalable une nouvelle vérification du second facteur.
- Un identifiant de sous-organisation valide n'est plus rejeté avec
  « Organization not found », et une clé API créée dans une sous-organisation
  résout son utilisateur technique depuis cette sous-organisation.
- La modification d'une organisation valide l'identifiant de partenaire et ne
  réinitialise plus le type d'organisation par effet de bord.
- Le compteur « Remaining tokens » (jetons restants) de la vue d'abonnement
  est ancré sur l'année contractuelle, et non sur l'année civile.

## Auth Bridge Service — `0.5.7`

- La réplication des comptes entre les régions UE et US se rétablit
  d'elle-même. Un flux de réplication interrompu se rattache sur place, la
  réplication continue de circuler pendant qu'une réconciliation s'exécute, et
  la mémoire de réconciliation est bornée, de sorte que le service ne
  redémarre plus en boucle sur les grandes tables.

## Barcode Service — `1.18.7`

- La lecture des codes-barres s'exécute sous une limite de temps et signale un
  dépassement de délai au lieu de rester suspendue, ce qui laissait auparavant
  le document bloqué en traitement.

## Docflow Service — `2.9.8`

- Les valeurs de champ écrites par une carte de workflow atterrissent sur le
  document dans les deux représentations stockées, de sorte qu'un export
  ultérieur ne les annule plus.
- Un déclencheur relancé conserve le travail déjà effectué par l'exécution,
  les déclencheurs en concurrence sur le même document se mettent en file
  d'attente au lieu de voler le verrou, et une relance escaladée est classée
  en tête de la file.
- Cartes de comparaison de bons de commande : les tolérances se comparent en
  décimales exactes et sont basées sur la valeur du bon de commande, les
  directions de comparaison inversées sont disponibles en option, un groupe
  affecté est signalé comme un groupe au lieu de faire échouer une comparaison
  d'identifiant utilisateur, les identifiants d'affectation se comparent
  correctement comme des UUID, les lignes avec des valeurs numériques vides
  sont ignorées, et une comparaison « received » sans aucune donnée de
  réception signale des données manquantes au lieu de prétendre correspondre.
- La carte Apply Decision Table a été retirée.

## Email Service — `1.41.0`

- Les imports Gmail récupèrent chaque pièce jointe exactement une fois ; les
  doublons issus de récupérations qui se chevauchaient ont disparu.
- Le curseur de lecture d'import n'avance qu'après confirmation de l'import,
  de sorte qu'un plantage en cours d'import ne peut plus faire sauter des
  e-mails.
- Lorsqu'une configuration d'import est désactivée parce qu'une configuration
  similaire existe, cette désactivation est visible et notifiée au lieu d'être
  silencieuse.

## Extraction Service — `1.54.5`

- La question de savoir si un document est un avoir ou une facture est
  tranchée selon le mot-clé le plus proche de la mention du type de document,
  au lieu du premier trouvé.
- Lorsque plusieurs interprétations de taxe sont dans la tolérance, la
  réconciliation exacte est préférée à une quasi-correspondance.
- Après une re-OCR forcée, le type de document et les paramètres régionaux
  sont restaurés, de sorte que l'extraction et l'entraînement de tableaux
  fonctionnent à nouveau sur les documents repassés en OCR.
- Les documents sans type de document ne font plus planter la recherche des
  règles de tableau.

## FTP Service — `1.32.8`

- L'analyse des dossiers effectue un seul aller-retour de listage par dossier
  avec une profondeur bornée, de sorte que les imports depuis de grands
  répertoires FTP sont beaucoup plus rapides et n'expirent plus.

## Fulltext Service — `1.42.3`

- Les documents dont la charge utile de recherche stockée ne contenait aucun
  champ extrait sont réindexés depuis la base de données, de sorte qu'ils
  réapparaissent dans la recherche du tableau de bord.
- La fenêtre de recherche du tableau de bord prend en charge jusqu'à 10 000
  documents.
- Les recherches à facettes n'échouent plus lorsque la recherche sémantique
  est active.

## OCR Service — `1.10.7`

- Le budget temps de l'OCR est dimensionné selon le coût réel par page, de
  sorte que les documents longs se terminent au lieu d'atteindre la limite du
  pipeline.

## PO Match Service — `1.59.8`

- Les lignes de tableau avec une quantité nulle sont ignorées dans les
  contrôles d'écart au lieu de produire de faux écarts.
- Lorsque des colonnes obligatoires du rapprochement PO manquent, le résultat
  les nomme.
