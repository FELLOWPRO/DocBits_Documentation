# Notes de version DocBits — 4–14 juillet 2026

_Un tour d'horizon de ce qui change pour vous dans cette version de DocBits.
Chaque service ci-dessous indique la version désormais en cours de déploiement,
suivie des nouveautés ou corrections expliquées en langage clair — sans numéros
de ticket ni jargon d'ingénierie. Les services non répertoriés n'ont connu
aucune modification visible par le client durant cette période._

---

## Points forts

- **Connexion multi-organisations.** Les utilisateurs appartenant à plusieurs
  organisations disposent désormais d'un véritable sélecteur d'organisation à
  la connexion, d'un commutateur d'organisation dans l'en-tête et d'un
  paramètre d'organisation par défaut. Les sessions sont liées de manière
  sécurisée à une seule organisation à la fois, et l'application suit
  automatiquement la région de l'organisation active. Une connexion effectuée
  sur la mauvaise région bascule désormais automatiquement vers la bonne au
  lieu d'échouer.
- **Canaux de version (frozen / latest).** Les organisations peuvent désormais
  être figées sur une version stable (« frozen ») tandis que d'autres
  reçoivent les dernières mises à jour — permettant des déploiements
  contrôlés. La boîte de dialogue Versions des services affiche une nouvelle
  colonne *Release*, et les administrateurs gèrent le canal depuis les
  Informations de l'entreprise. Plusieurs services affichent des sauts de
  version plus importants durant cette période uniquement en raison de la
  nouvelle numérotation par canal — ces sauts ne comportent aucun changement
  fonctionnel.
- **Moteurs de règles configurables.** Trois nouveaux systèmes de règles
  arrivent dans l'API (chacun désactivé par défaut, activable par
  organisation) : des **règles de validation** qui contrôlent les valeurs
  extraites et signalent les échecs directement sur le document, des **règles
  de transformation** qui nettoient ou réécrivent automatiquement les valeurs
  extraites des champs et des tableaux, et une **sélection de mise en page par
  règles** qui choisit la bonne mise en page du document selon des règles
  plutôt que selon sa provenance.
- **Transparence de l'import e-mail.** Le journal d'import des e-mails affiche
  désormais une ligne dépliable par pièce jointe, indique quels documents ont
  été créés (avec des boutons qui mènent directement à ceux-ci sur le tableau
  de bord), signale les éléments ignorés et scindés, et permet de télécharger
  l'e-mail d'origine au format `.eml`.
- **Extraction de tableaux par IA.** Un nouveau mode d'extraction IA
  structurée pour les tableaux, avec une case à cocher « Use AI » par tableau
  et par colonne dans les paramètres du type de document.
- **Stabilité de la Web App.** Correction d'une boucle de rechargement infinie
  après l'expiration d'une session, correction du Layout Builder qui était
  cassé, et les tableaux d'extraction disposent désormais d'une poignée de
  redimensionnement en hauteur.
- **Nouveau : Auth Bridge Service.** Un nouveau service maintient les données
  de connexion en synchronisation continue entre les régions UE et US, avec
  auto-réparation et surveillance intégrées.

---

## API Service — en ligne : `12.57.8`

- **Règles de validation (nouveau, par organisation) :** un moteur de règles
  configurable par l'administrateur contrôle les valeurs extraites (totaux,
  champs obligatoires, et plus encore) et marque les échecs directement sur le
  document, en indiquant quelle règle s'est déclenchée. Les règles peuvent
  être testées à blanc avant activation, peuvent être activées par type de
  document, et sont livrées avec un catalogue de règles par défaut (toutes
  désactivées tant que vous n'y adhérez pas).
- **Règles de transformation (nouveau, par organisation) :** nettoyage ou
  réécriture automatique des valeurs extraites des champs et des tableaux
  pendant le traitement — configurable par type de document ou pour toute
  l'organisation.
- **Sélection de mise en page par règles (nouveau) :** les mises en page des
  documents peuvent désormais être choisies par des règles configurables au
  lieu d'être liées à la provenance du document. Le comportement existant basé
  sur la provenance est migré automatiquement, les modèles de mise en page
  peuvent être renommés, et les titres de mise en page en double sont
  empêchés.
- **Exports du tableau de bord plus rapides :** les exports déclenchés depuis
  le tableau de bord sont désormais transmis à un worker dédié au lieu
  d'attendre un cycle d'interrogation, et démarrent donc rapidement.
- **Correction du blocage d'export de la détection de doublons :** le blocage
  d'export pour les doublons présumés fonctionne à nouveau.
- **Paramètres qui ne se conservaient pas :** correction de préférences
  enregistrées qui, parfois, n'étaient pas persistées lorsqu'une ancienne
  copie supprimée du même paramètre existait.
- **Documents contenant des caractères inhabituels :** correction d'erreurs
  d'enregistrement causées par des caractères NUL invisibles dans les données
  extraites.
- **« Modifié par » correct :** les documents importés automatiquement en tant
  que documents électroniques n'affichent plus un utilisateur système comme
  dernier éditeur — le champ reste vide tant qu'une personne ne modifie pas
  réellement le document.
- **PDF numérisés avec une bonne couche de texte :** une nouvelle option
  permet à DocBits de faire confiance au texte déjà intégré dans une page
  numérisée au lieu de relancer l'OCR — plus rapide et souvent plus précis.
- **Factures électroniques :** détection plus robuste du XML intégré lorsque
  le fichier d'origine doit être revérifié.
- **Tâches :** nouveau paramètre d'organisation permettant aux
  non-administrateurs d'utiliser le filtre « Tous » dans la liste des tâches.
- **Rapprochement des lignes :** le comportement de correspondance approchée
  (fuzzy matching) est désormais configurable par ligne.
- **Stabilité :** les connexions WebSocket se ferment proprement en cas
  d'erreur au lieu de lever des exceptions serveur ; la synchronisation du
  cache des autorisations se vérifie et se répare elle-même ; la version du
  service est désormais visible sur le point de terminaison de santé.

## Auth Service — en ligne : `1.71.1`

- **Connexion multi-organisations :** la connexion demande désormais dans
  quelle organisation entrer lorsqu'un utilisateur appartient à plusieurs,
  les sessions sont liées à cette organisation, et de nouveaux points de
  terminaison permettent de sélectionner, de changer et de définir une
  organisation par défaut. Les appartenances d'organisation en double ou en
  conflit ont été nettoyées et sont désormais empêchées au niveau de la base
  de données, avec des recherches d'appartenance plus rapides.
- **Corrections de l'organisation par défaut :** la connexion sélectionne
  automatiquement votre organisation par défaut (et non une organisation
  arbitraire), et le changement d'organisation par défaut prend effet
  immédiatement au lieu d'afficher des données de profil obsolètes.
- **Déconnexion corrigée :** résolution d'une erreur serveur (HTTP 500) à la
  déconnexion et rétablissement du point de terminaison de révocation des
  jetons.
- **Sécurité des jetons :** la vérification et la mise en cache des jetons
  respectent désormais l'organisation pour laquelle un jeton a été émis, et
  la révocation des jetons est centralisée.
- **Canaux de version :** le canal de version de l'organisation est stocké
  ici, gérable par les administrateurs de l'organisation, et exposé à
  l'application et à la couche de routage.

## Auth Bridge Service — en ligne : `0.2.4.2` _(nouveau service)_

- **De quoi s'agit-il :** un nouveau service qui réplique en continu les
  données d'authentification entre les régions UE et US, afin que les comptes
  et les connexions restent cohérents d'une région à l'autre.
- **Auto-réparation :** il détecte et répare les dérives de données entre les
  régions — y compris en veillant à ce que les suppressions se propagent — et
  se rétablit automatiquement après une perte de connexion au lieu de perdre
  des données.
- **Sécurité et surveillance :** une boucle de réplication bidirectionnelle
  antérieure a été arrêtée et est désormais activement détectée et bloquée ;
  le suivi des erreurs et les alertes sont en place ; et le service indique sa
  version dans la boîte de dialogue Versions des services.

## Docflow Service — en ligne : `2.6.1`

- **Les cartes de workflow acceptent les valeurs vides :** les cartes de type
  case à cocher et partenaire n'échouent plus lorsqu'un champ est
  légitimement vide ; les contrôles de type de carte sont plus stricts et
  plus prévisibles.
- **Les workflows se relancent lors de changements réels :** le verrou de
  workflow respecte de nouveau le statut du document issu du déclencheur, et
  suit désormais aussi la version du document — ainsi, un document dont les
  données ont réellement changé peut repasser par le workflow même avec le
  même statut, tandis que les vrais doublons restent bloqués.
- **Workflows avancés plus grands :** la limite du nombre de nœuds de
  workflow a été relevée et est désormais configurable par environnement.
- **Export alternatif :** les exports alternatifs déclenchés par workflow sont
  désormais étiquetés comme tels afin que les systèmes en aval puissent les
  distinguer.
- **Résilience :** le service se reconnecte automatiquement lorsqu'une
  connexion à la base de données est interrompue en cours d'utilisation,
  tolère un courtier de messages plus lent au lieu d'échouer, et les requêtes
  API en échec sont désormais journalisées avec leur contexte complet et des
  identifiants d'exécution traçables.

## Email Service — en ligne : `1.38.4`

- **Journal d'import, refondu pour la traçabilité :** chaque e-mail importé
  enregistre désormais quels documents en ont été créés, avec des lignes de
  détail par pièce jointe.
- **Téléchargement de l'e-mail d'origine :** le message d'origine peut être
  téléchargé au format `.eml` directement depuis le journal d'import.
- **Récupération des pièces jointes :** le mécanisme de récupération après
  corruption gère désormais aussi les messages en texte brut, si bien que
  davantage d'e-mails entrants endommagés sont récupérés au lieu d'être
  ignorés.

## Extraction Service — en ligne : `1.51.6`

- **Taxe/net plus jamais inversés :** correction d'un cas sur les documents
  américains où le montant de la taxe pouvait être attribué comme supérieur
  au montant net lorsque plusieurs paires candidates étaient trouvées.
- **Plusieurs taux de taxe par fournisseur :** l'extraction gère désormais les
  fournisseurs dont les factures comportent différents taux de taxe sur un
  même document.
- **Extraction de tableaux par IA (nouveau, en option) :** points de
  terminaison d'extraction IA structurée pour les tableaux, activés par
  organisation via un indicateur de fonctionnalité.
- **Appels IA plus rapides :** ajustement de la configuration du modèle IA
  utilisé pendant l'extraction pour éviter des temps de traitement inutiles.
- **Correction de plantage :** résolution d'une erreur sur les documents
  produisant une liste de candidats vide pendant l'extraction.

## Fulltext Service — en ligne : `1.37.2`

- **Migrations de l'index de recherche réparées :** rétablissement de
  définitions de migration qui avaient dérivé, afin de garder les mises à
  niveau de l'index de recherche fiables.
- Travaux de routage internes pour la nouvelle infrastructure de canaux de
  version.

## PO Match Service — en ligne : `1.58.2`

- **Rapprochement plus tolérant :** le rapprochement des bons de commande
  n'échoue plus sur des données inhabituelles — les numéros d'article non
  textuels, les quantités manquantes et les montants non textuels sont
  désormais gérés correctement au lieu de provoquer des erreurs.

## Web App — en ligne : `10.41.8`

- **Expérience multi-organisations :** nouvelle page de sélection
  d'organisation à la connexion, icône dédiée de changement d'organisation
  dans l'en-tête, paramètres d'organisation par défaut, et l'application suit
  la région de votre organisation active. Une connexion effectuée sur la
  mauvaise région bascule silencieusement vers la bonne région et vous
  redirige vers le sélecteur d'organisation si nécessaire.
- **Fin des rechargements sans fin :** correction d'une boucle de
  rechargement infinie qui pouvait survenir lorsque le serveur rejetait un
  jeton de session stocké — l'application force désormais un véritable
  renouvellement du jeton au lieu de recharger indéfiniment.
- **Layout Builder corrigé :** le Layout Builder fonctionne à nouveau, et la
  sélection de mise en page est découplée de la provenance du document (en
  cohérence avec la nouvelle sélection par règles dans l'API).
- **Tableaux d'extraction :** les tableaux de lignes disposent désormais
  d'une poignée de redimensionnement afin de donner plus de place au tableau
  pendant la validation.
- **Journal d'import e-mail :** nouveaux badges de statut « ignoré » et de
  scission, lignes dépliables par pièce jointe, téléchargement de l'e-mail
  d'origine, et boutons d'identifiant de document qui mènent directement au
  tableau de bord filtré sur ce document.
- **Recherche du tableau de bord :** la liste déroulante des valeurs de
  requête affiche désormais le libellé localisé pour les champs de type liste
  de valeurs, et les exemples de l'aide à la recherche ont été retravaillés.
- **Fiabilité des paramètres :** les préférences utilisateur se chargent
  désormais de manière fiable lors d'une connexion via SSO, et la
  confirmation d'enregistrement ne s'affiche que lorsque l'enregistrement a
  réellement réussi.
- **Tâches :** le filtre « Tous » peut être rétabli pour les
  non-administrateurs via un nouveau paramètre d'organisation.
- **Journaux Watchdog :** plus de limite à 10 000 entrées, plus des
  améliorations générales d'ergonomie.
- **Tickets de support :** le formulaire de support préremplit votre adresse
  e-mail à partir de votre profil.
- **Paramètres des types de document :** nouvelle case à cocher « Use AI »
  sur les tableaux et les colonnes pour contrôler l'extraction de tableaux
  assistée par IA.
- **Boîte de dialogue Versions des services :** nouvelle colonne *Release*
  indiquant le canal de chaque service (frozen/latest), routée de manière à
  rester rapide pour les organisations figées.
- **Field Validation :** correction d'une erreur lors du retour à Field
  Validation depuis un autre écran, et le bouton « Scripts » ne redirige plus
  vers une page 404.

---

## Renumérotation de version uniquement (aucun changement fonctionnel)

**Auto Accounting** (`1.20.1`), **Barcode Service** (`1.17.1`), **OCR
Service** (`1.9.1`), **FTP Service** (`1.31.1`), **Operator Service**
(`1.40.2`) et **Ideas Service** (`0.3.1`) ont été renumérotés dans le cadre de
la nouvelle infrastructure de canaux de version. Leurs sauts de version
apparemment importants ne comportent aucun changement de fonctionnalité ni de
comportement durant cette période. **Docnet Service** (`1.54.6`) est inchangé
depuis le 19 juin.

<!-- Generated by the docbits-changelog skill (version-boundary mode: exact
     git ranges between the ALT (2026-07-03/04) and NEU (2026-07-09..14)
     version-bump commits supplied by the user, per service). -->
