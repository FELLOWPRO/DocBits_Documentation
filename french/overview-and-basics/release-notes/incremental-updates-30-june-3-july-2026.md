# Notes de version DocBits — 30 juin – 3 juillet 2026

_Ce que cette mise à niveau de production a apporté, en langage clair. Chaque
service indique la version désormais en ligne en production. Les services non
répertoriés n'ont connu aucune modification visible par le client durant cette
période._

---

## Points forts

- **Chat IA sur les journaux d'activité.** Un nouveau panneau de chat IA sur la
  page Activity Logs vous permet de poser directement des questions sur
  l'activité des journaux, sans avoir à fouiller dans les entrées brutes.
- **Suivi des e-mails sortants dans le journal d'import.** Le journal d'import
  enregistre désormais les e-mails sortants en plus des entrants, avec des
  pastilles de filtre rapide Erreurs / Entrant / Sortant — les boîtes aux
  lettres en échec répété sont désormais désactivées automatiquement, les
  administrateurs peuvent être notifiés par e-mail en cas d'échec d'import, et
  les nouvelles tentatives vont désormais jusqu'à 15 fois sur environ 5 heures
  avant abandon.
- **Des erreurs d'import e-mail plus claires.** Les échecs de connexion
  affichent désormais la véritable cause sous-jacente, avec des messages
  dédiés pour un certificat invalide ou un mot de passe d'application Gmail
  incorrect.
- **Boucle de connexion corrigée.** Certains utilisateurs pouvaient rester
  bloqués dans une boucle de connexion répétée lors du renouvellement du
  jeton — corrigé.
- **Traitement des documents plus stable.** Correction d'un plantage lors de
  l'extraction de données provenant de valeurs de coordonnées non arrondies,
  la lecture des codes-barres effectue désormais une nouvelle tentative en
  cas d'échec récupérable au lieu d'abandonner silencieusement, et un cas
  rare où un document pouvait être exporté deux fois simultanément est
  corrigé.
- **Améliorations de l'écran de validation.** Vous pouvez désormais zoomer
  davantage sur les documents, les champs ne sont plus vidés par les scripts
  lorsque leur valeur n'a pas réellement changé, et le tableau de bord
  mémorise votre position de page lorsque vous revenez en arrière.

---

## Web App — en ligne : `10.35.7`

- **Panneau de chat IA** ajouté à la page Activity Logs (#15512).
- **Journal d'import :** nouvelles pastilles de filtre rapide Erreurs /
  Entrant / Sortant ; bascule et champ pour les destinataires des
  notifications d'échec dans les paramètres d'e-mail entrant.
- **Écran de validation :** le zoom des documents dépasse désormais la taille
  par défaut précédente ; les champs vidés par les scripts de validation
  conservent désormais correctement leur valeur lorsque le script renvoie la
  même valeur.
- **Tableau de bord :** la position de page est conservée lors du retour au
  tableau ; la poignée de redimensionnement de colonne ne déborde plus de
  l'en-tête du tableau.
- **Écran Auto Accounting :** correction d'une erreur de validation.
- **DocBits Tasks :** correction d'un problème de permissions.
- **Journaux Watchdog :** ajout d'un filtre de plage horaire et d'un
  sélecteur ajustable du nombre de lignes par page.
- **Corrections :** une erreur de graphique (« Element not found ») sur la
  page Boards ; un lien de suppression d'export cassé sur Activity Logs ; des
  corrections de mise en page sur l'écran Layout Builder ; une traduction
  manquante sur le filtre de plage horaire d'Activity Logs.
- **Mise à jour automatique :** renforcement supplémentaire du mécanisme de
  mise à jour automatique de l'application (nettoyage au démarrage plus
  rapide, détection de version plus fiable, purge du cache avant un
  rechargement de récupération).

## API Service — en ligne : `12.48.1`

- **Chargement plus rapide des scripts de document :** les scripts de
  validation sont désormais mis en cache côté serveur (cache de 6 heures) au
  lieu d'être récupérés à chaque fois.
- **Confiance des montants plus précise :** le calcul du score de confiance
  tient désormais compte des documents utilisant des conventions de séparateur
  décimal différentes.
- **Fiabilité :** la validation des documents exécute toujours la seule
  version de script active, et la version exécutée est désormais journalisée ;
  un cas rare où un document pouvait être exporté deux fois simultanément est
  corrigé ; les règles d'extraction spécifiques au fournisseur s'appliquent de
  nouveau correctement après une nouvelle OCR forcée.
- **Import e-mail :** ajout du support backend pour la journalisation des
  e-mails sortants et les e-mails de notification d'échec (voir Email
  Service, ci-dessous).

## Auth Service — en ligne : `1.68.5`

- **Correction d'une boucle de connexion** que certains utilisateurs
  pouvaient rencontrer pendant le renouvellement de leur jeton de session.
- **Écrans d'administration d'organisation plus rapides :** les données
  utilisateur et d'abonnement se chargent désormais en masse au lieu d'un
  enregistrement à la fois.
- **Correction d'un rare conflit de base de données** lors de la liaison d'un
  utilisateur à une organisation.

## Email Service — en ligne : `1.37.4`

- **Le journal d'import suit désormais les e-mails sortants** en plus des
  entrants, avec un filtre permettant d'afficher uniquement les imports
  entrants, sortants ou en échec.
- **Les boîtes aux lettres en échec répété sont désormais désactivées
  automatiquement**, et les administrateurs peuvent être notifiés par e-mail
  en cas d'échec d'import ; les nouvelles tentatives vont désormais jusqu'à
  15 fois sur environ 5 heures avant abandon.
- **Messages d'échec de connexion plus clairs :** affiche la véritable cause
  sous-jacente, un message dédié pour un certificat invalide, et un message
  spécifique pour un mot de passe d'application Gmail incorrect.
- **Correction du routage entrant** qui réécrivait de manière incorrecte les
  adresses de serveur pour les comptes de la région UE.
- Plus résilient face aux brèves coupures de connexion Redis.

## Extraction Service — en ligne : `1.49.0`

- **Correction d'un plantage lors de l'extraction** causé par des valeurs de
  coordonnées non arrondies.
- **Confiance des montants plus précise** pour les documents utilisant des
  formats de séparateur décimal mixtes ; les petits écarts d'arrondi du total
  de taxe ne bloquent plus une correspondance.

## Docflow Service — en ligne : `2.4.2`

- **Refonte de l'authentification pour les workflows avancés (basés sur
  Celery)**, avec des garde-fous pour qu'un échec de vérification
  d'authentification ne puisse plus faire planter l'exécution d'un workflow.
- **Réponse plus claire** lorsqu'une étape de workflow tente de s'exécuter
  sur un workflow qui n'existe plus.

## Barcode Service — en ligne : `1.15.7`

- **La lecture des codes-barres effectue désormais automatiquement une
  nouvelle tentative** en cas d'échec récupérable au lieu d'abandonner
  silencieusement.

## OCR Service — en ligne : `1.7.3`

- **Correction d'un échec OCR** causé par un problème de résolution de nom
  d'hôte Redis.
- Les déconnexions Redis liées aux vérifications de santé ne sont plus
  journalisées comme des erreurs, réduisant les fausses alertes.

## PO Match Service — en ligne : `1.55.8`

- **Correction des notes qui n'apparaissaient pas** sur les enregistrements
  PO Match.

---

## Aucune modification visible par le client durant cette période

Stables, sans changement produit notable entre le 30 juin et le 3 juillet :
Auto Accounting (`1.18.7`), Docnet (`1.54.6`), FTP (`1.30.2`), Fulltext
(`1.35.7`), Operator (`1.39.5`). Auto Accounting n'a reçu qu'une maintenance
interne de configuration de déploiement. Ideas Service n'a pas pu être
contacté pour une vérification de version durant cette période.

<!-- Generated by the docbits-changelog skill (version-boundary mode, resolved
     from the prod version table supplied by the user). Window 2026-06-30 →
     2026-07-03. -->
